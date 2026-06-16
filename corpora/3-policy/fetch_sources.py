#!/usr/bin/env python3
"""Snapshot the corpus-3 documents named in manifest.csv.

For each accessible row this downloads the source, saves the raw file under
`sources/raw/<id>.{pdf,html}`, extracts plain text, and writes a readable
Markdown snapshot to `sources/text/<id>.md` with a provenance header. This is
how the corpus gets *content*, not just links — and it is reproducible: re-run
to refresh, diff against the previous snapshot.

    python3 fetch_sources.py            # snapshot all accessible rows
    python3 fetch_sources.py --only eu-ai-act-2024

Needs: pdftotext (poppler) for PDFs, beautifulsoup4 for HTML.

NOTE. Several rows point at *landing pages*, not the document itself (e.g. the
NIST RMF hub). Those extract as navigation text — flagged by a low char count in
the run summary. Swapping the landing URL for the direct PDF is exactly the kind
of per-source cleanup a student group does while building the corpus.
"""
import argparse
import csv
import datetime
import os
import re
import subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "sources", "raw")
TEXT = os.path.join(HERE, "sources", "text")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read(), r.headers.get_content_type()


def html_to_text(raw):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer", "aside",
                     "form", "noscript", "svg"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body or soup
    text = main.get_text("\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def pdf_to_text(path):
    out = subprocess.run(["pdftotext", "-q", path, "-"],
                         capture_output=True, text=True, timeout=120)
    return out.stdout.strip()


def write_md(row, text, kind, today):
    md = os.path.join(TEXT, f"{row['id']}.md")
    header = (f"# {row['title']}\n\n"
              f"- **Source:** {row['source']}\n"
              f"- **Type:** {row['type']} ({row['stratum']})\n"
              f"- **Year:** {row['year']}\n"
              f"- **Original:** {row['url']}\n"
              f"- **Snapshot:** {kind}, fetched {today}\n"
              f"- **Inclusion reason:** {row['inclusion_reason']}\n\n"
              f"---\n\n")
    with open(md, "w", encoding="utf-8") as f:
        f.write(header + text + "\n")
    return len(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="snapshot a single id")
    args = ap.parse_args()
    os.makedirs(RAW, exist_ok=True)
    os.makedirs(TEXT, exist_ok=True)
    today = datetime.date.today().isoformat()

    with open(os.path.join(HERE, "manifest.csv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    for row in rows:
        rid = row["id"]
        if args.only and rid != args.only:
            continue
        if row.get("accessible") == "false":
            print(f"  SKIP   {rid:32s} gated (metadata only)")
            continue
        try:
            raw, ctype = fetch(row["url"])
            is_pdf = "pdf" in ctype or raw[:5] == b"%PDF-"
            ext = "pdf" if is_pdf else "html"
            rawpath = os.path.join(RAW, f"{rid}.{ext}")
            with open(rawpath, "wb") as f:
                f.write(raw)
            if is_pdf:
                text, kind = pdf_to_text(rawpath), "PDF → pdftotext"
            else:
                text, kind = html_to_text(raw), "HTML → main-text extract"
            n = write_md(row, text, kind, today)
            flag = "  (landing page? low text)" if n < 1500 else ""
            print(f"  OK     {rid:32s} {ext:4s} {n:7d} chars{flag}")
        except Exception as e:  # noqa: BLE001
            msg = str(e).split("\n")[0][:60]
            print(f"  FAIL   {rid:32s} {msg}")


if __name__ == "__main__":
    main()
