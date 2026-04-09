"""
paper_monitor.py — Daily paper monitoring script for LLM Wiki

Scans bioRxiv, medRxiv, and PubMed for new relevant papers.
Generates a report in scripts/monitor_reports/monitor-YYYY-MM-DD.md

Usage:
    python3 scripts/paper_monitor.py --days 7 --min-score 2
    python3 scripts/paper_monitor.py --days 3 --min-score 4

Requirements:
    pip3 install requests biopython
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
import urllib.request
import urllib.parse

# ─── Configuration ────────────────────────────────────────────────────────────

WIKI_ROOT = Path(__file__).parent.parent

# PubMed journals to monitor
PUBMED_JOURNALS = [
    "Nature",
    "Science",
    "Cell",
    "Nature Genetics",
    "Nature Medicine",
    "Nature Neuroscience",
    "Nature Methods",
    "Nature Biotechnology",
    "American Journal of Human Genetics",
    "Neuron",
    "Cell Genomics",
    "Genome Biology",
    "Genome Medicine",
    "Genome Research",
    "PLOS Genetics",
    "eLife",
]

# Category keyword definitions: {category: {high: [...], medium: [...], penalty: [...]}}
CATEGORY_KEYWORDS = {
    "genomic-dl": {
        "high": ["dna language model", "nucleotide transformer", "enformer", "basenji",
                 "variant effect prediction", "regulatory element", "genome foundation model"],
        "medium": ["genomic deep learning", "sequence model", "epigenomics", "chromatin accessibility"],
        "penalty": ["protein structure", "scRNA", "single cell"],
    },
    "single-cell-dl": {
        "high": ["scrna-seq deep learning", "single-cell classification", "cell type annotation",
                 "single-cell embedding", "scvi", "totalvi"],
        "medium": ["single-cell rna", "scRNA-seq", "cell clustering", "dimensionality reduction"],
        "penalty": ["bulk rna", "spatial transcriptomics only"],
    },
    "single-cell-foundation": {
        "high": ["geneformer", "scgpt", "single-cell foundation model", "large-scale single-cell",
                 "cell language model", "scbert"],
        "medium": ["foundation model single cell", "pretrained single-cell", "single-cell llm"],
        "penalty": [],
    },
    "protein-ai": {
        "high": ["protein language model", "alphafold", "esm", "rosettafold",
                 "protein structure prediction", "protein design"],
        "medium": ["protein folding", "amino acid embedding", "protein function prediction"],
        "penalty": ["dna", "rna", "genome"],
    },
    "gwas": {
        "high": ["genome-wide association", "gwas", "rare variant", "polygenic risk score",
                 "ewas", "epigenome-wide association"],
        "medium": ["association study", "locus", "snp heritability", "mendelian randomization"],
        "penalty": [],
    },
    "neuroscience": {
        "high": ["autism spectrum disorder", "asd", "schizophrenia", "bipolar disorder",
                 "psychiatric genetics", "adhd genetics"],
        "medium": ["psychiatric disorder", "brain disorder", "neuropsychiatric", "neurodevelopmental"],
        "penalty": [],
    },
    "brain-development": {
        "high": ["cortical development", "neurogenesis", "brain organoid development",
                 "fetal brain", "neural progenitor"],
        "medium": ["brain development", "cortex", "neural circuit development"],
        "penalty": [],
    },
    "brain-atlas": {
        "high": ["brain cell atlas", "biccn", "spatial transcriptomics brain",
                 "single-cell brain atlas", "allen brain"],
        "medium": ["brain cell type", "neuron subtype", "cell atlas"],
        "penalty": [],
    },
    "long-read": {
        "high": ["long-read sequencing", "pacbio", "oxford nanopore", "ont sequencing",
                 "hifi reads", "structural variant long-read"],
        "medium": ["long read", "nanopore", "third-generation sequencing"],
        "penalty": [],
    },
    "lrRNA": {
        "high": ["iso-seq", "mas-seq", "long-read rna-seq", "ont rna", "full-length transcript"],
        "medium": ["long-read transcriptome", "isoform sequencing", "nanopore rna"],
        "penalty": [],
    },
    "methylation-ai": {
        "high": ["methylation deep learning", "methylation transformer", "dna methylation model",
                 "methylation prediction neural", "cpg prediction model"],
        "medium": ["methylation machine learning", "methylation classification model"],
        "penalty": ["gwas", "epidemiology only"],
    },
    "methylation": {
        "high": ["dna methylation", "cpg island", "bisulfite sequencing", "dnmt",
                 "epigenetic clock", "methylation aging"],
        "medium": ["methylation", "epigenetics", "histone modification"],
        "penalty": [],
    },
    "medical-llm": {
        "high": ["medical large language model", "clinical llm", "biomedical nlp",
                 "ehr language model", "clinical note", "medical question answering"],
        "medium": ["medical ai", "clinical nlp", "health llm", "biomedical text"],
        "penalty": [],
    },
    "statistics": {
        "high": ["false discovery rate", "multiple testing correction", "bayesian inference",
                 "causal inference", "mendelian randomization method", "batch effect correction"],
        "medium": ["statistical method", "mixed model", "regression genomics"],
        "penalty": [],
    },
}

# ─── Scoring ──────────────────────────────────────────────────────────────────

def score_paper(title: str, abstract: str) -> tuple[int, str]:
    """Score a paper based on keyword matches. Returns (score, matched_category)."""
    text = (title + " " + abstract).lower()
    best_score = 0
    best_category = "other"

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0
        for kw in keywords.get("high", []):
            if kw.lower() in text:
                score += 2
        for kw in keywords.get("medium", []):
            if kw.lower() in text:
                score += 1
        for kw in keywords.get("penalty", []):
            if kw.lower() in text:
                score -= 1

        if score > best_score:
            best_score = score
            best_category = category

    return best_score, best_category


# ─── Unpaywall ────────────────────────────────────────────────────────────────

def check_open_access(doi: str, email: str = "wiki@research.org") -> str | None:
    """Check if a paper has an open access PDF via Unpaywall API."""
    if not doi:
        return None
    url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={email}"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
            if data.get("is_oa") and data.get("best_oa_location"):
                return data["best_oa_location"].get("url_for_pdf")
    except Exception:
        pass
    return None


# ─── bioRxiv / medRxiv ────────────────────────────────────────────────────────

def fetch_biorxiv(days: int) -> list[dict]:
    """Fetch recent preprints from bioRxiv and medRxiv."""
    papers = []
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

    for server in ["biorxiv", "medrxiv"]:
        url = f"https://api.biorxiv.org/details/{server}/{start_date}/{end_date}/0/json"
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                data = json.loads(resp.read())
                for item in data.get("collection", []):
                    papers.append({
                        "title": item.get("title", ""),
                        "authors": item.get("authors", ""),
                        "abstract": item.get("abstract", ""),
                        "doi": item.get("doi", ""),
                        "date": item.get("date", ""),
                        "source": server,
                        "url": f"https://www.{server}.org/content/{item.get('doi')}",
                        "pdf_url": f"https://www.{server}.org/content/{item.get('doi')}.full.pdf",
                    })
        except Exception as e:
            print(f"  Warning: Could not fetch {server}: {e}", file=sys.stderr)

    return papers


# ─── PubMed ───────────────────────────────────────────────────────────────────

def fetch_pubmed(days: int) -> list[dict]:
    """Fetch recent papers from monitored PubMed journals."""
    papers = []
    since = (datetime.now() - timedelta(days=days)).strftime("%Y/%m/%d")

    # Build journal filter
    journal_query = " OR ".join([f'"{j}"[Journal]' for j in PUBMED_JOURNALS])
    query = f"({journal_query}) AND ({since}[PDAT] : 3000[PDAT])"
    encoded = urllib.parse.quote(query)

    # Search
    search_url = (
        f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        f"?db=pubmed&term={encoded}&retmax=200&retmode=json"
    )
    try:
        with urllib.request.urlopen(search_url, timeout=15) as resp:
            ids = json.loads(resp.read()).get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"  Warning: PubMed search failed: {e}", file=sys.stderr)
        return papers

    if not ids:
        return papers

    # Fetch summaries in batches of 50
    for i in range(0, len(ids), 50):
        batch = ",".join(ids[i:i+50])
        fetch_url = (
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            f"?db=pubmed&id={batch}&retmode=xml&rettype=abstract"
        )
        try:
            with urllib.request.urlopen(fetch_url, timeout=15) as resp:
                xml = resp.read().decode("utf-8")
            # Simple XML parsing (no external deps)
            import re
            articles = xml.split("<PubmedArticle>")
            for article in articles[1:]:
                title = re.search(r"<ArticleTitle>(.*?)</ArticleTitle>", article, re.DOTALL)
                abstract = re.search(r"<AbstractText.*?>(.*?)</AbstractText>", article, re.DOTALL)
                doi_match = re.search(r'<ArticleId IdType="doi">(.*?)</ArticleId>', article)
                date_match = re.search(r"<PubDate>.*?<Year>(\d+)</Year>.*?<Month>(\w+)</Month>", article, re.DOTALL)

                title_text = re.sub(r"<[^>]+>", "", title.group(1)) if title else ""
                abstract_text = re.sub(r"<[^>]+>", "", abstract.group(1)) if abstract else ""
                doi = doi_match.group(1).strip() if doi_match else ""
                date = f"{date_match.group(1)}-{date_match.group(2)}" if date_match else ""

                if title_text:
                    papers.append({
                        "title": title_text.strip(),
                        "authors": "",
                        "abstract": abstract_text.strip(),
                        "doi": doi,
                        "date": date,
                        "source": "pubmed",
                        "url": f"https://pubmed.ncbi.nlm.nih.gov/{ids[i]}/" if doi else "",
                        "pdf_url": None,
                    })
        except Exception as e:
            print(f"  Warning: PubMed fetch batch failed: {e}", file=sys.stderr)

    return papers


# ─── Report Generation ────────────────────────────────────────────────────────

def generate_report(papers: list[dict], min_score: int, days: int) -> str:
    """Generate a markdown report from scored papers."""
    today = datetime.now().strftime("%Y-%m-%d")
    scored = []

    for p in papers:
        score, category = score_paper(p["title"], p["abstract"])
        if score >= min_score:
            oa_pdf = check_open_access(p["doi"]) if p["doi"] else p.get("pdf_url")
            scored.append({**p, "score": score, "category": category, "oa_pdf": oa_pdf})

    scored.sort(key=lambda x: x["score"], reverse=True)

    ready = [p for p in scored if p["score"] >= 4 and p.get("oa_pdf")]
    manual = [p for p in scored if not (p["score"] >= 4 and p.get("oa_pdf"))]

    lines = [
        f"# Paper Monitor Report — {today}",
        f"",
        f"- **Period**: last {days} days",
        f"- **Min score**: {min_score}",
        f"- **Total scanned**: {len(papers)}",
        f"- **Above threshold**: {len(scored)}",
        f"- **Ready to collect**: {len(ready)}",
        f"",
        "---",
        "",
        "## Ready to Collect (score ≥ 4, OA PDF available)",
        "",
    ]

    if ready:
        for p in ready:
            lines += [
                f"### [{p['title']}]({p['url']})",
                f"- **Score**: {p['score']} | **Category**: `{p['category']}` | **Source**: {p['source']}",
                f"- **DOI**: {p['doi']}",
                f"- **PDF**: {p['oa_pdf']}",
                f"- **Abstract**: {p['abstract'][:300]}...",
                f"",
                f"```bash",
                f"curl -L \"{p['oa_pdf']}\" -o \"papers/{p['doi'].replace('/', '-') if p['doi'] else 'paper'}.pdf\"",
                f"```",
                f"",
            ]
    else:
        lines.append("*(none)*\n")

    lines += [
        "---",
        "",
        "## Manual Review Needed",
        "",
    ]

    if manual:
        for p in manual:
            oa = p.get("oa_pdf") or "not available"
            lines += [
                f"### [{p['title']}]({p['url']})",
                f"- **Score**: {p['score']} | **Category**: `{p['category']}` | **Source**: {p['source']}",
                f"- **DOI**: {p['doi']} | **OA PDF**: {oa}",
                f"- **Abstract**: {p['abstract'][:200]}...",
                f"",
            ]
    else:
        lines.append("*(none)*\n")

    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Monitor papers for LLM Wiki")
    parser.add_argument("--days", type=int, default=7, help="Days to look back (default: 7)")
    parser.add_argument("--min-score", type=int, default=2, help="Minimum relevance score (default: 2)")
    parser.add_argument("--no-pubmed", action="store_true", help="Skip PubMed")
    parser.add_argument("--no-biorxiv", action="store_true", help="Skip bioRxiv/medRxiv")
    args = parser.parse_args()

    print(f"Scanning papers from the last {args.days} days (min score: {args.min_score})...")

    papers = []
    if not args.no_biorxiv:
        print("  Fetching bioRxiv/medRxiv...")
        biorxiv_papers = fetch_biorxiv(args.days)
        print(f"    Found {len(biorxiv_papers)} preprints")
        papers.extend(biorxiv_papers)

    if not args.no_pubmed:
        print("  Fetching PubMed...")
        pubmed_papers = fetch_pubmed(args.days)
        print(f"    Found {len(pubmed_papers)} articles")
        papers.extend(pubmed_papers)

    print(f"  Total: {len(papers)} papers. Scoring...")
    report = generate_report(papers, args.min_score, args.days)

    # Save report
    today = datetime.now().strftime("%Y-%m-%d")
    reports_dir = WIKI_ROOT / "scripts" / "monitor_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"monitor-{today}.md"
    report_path.write_text(report, encoding="utf-8")

    print(f"\nReport saved: {report_path}")
    print(report[:500] + "..." if len(report) > 500 else report)


if __name__ == "__main__":
    main()
