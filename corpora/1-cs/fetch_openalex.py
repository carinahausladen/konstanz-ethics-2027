#!/usr/bin/env python3
"""Seed builder for Corpus 1 — Research, by DISCIPLINE.

A CURATED list of the most important papers on the AI value/alignment question
in each discipline, fetched by OpenAlex ID so the metadata (title, year,
citations, link, topic) stays live and reproducible.

Why curated, not a keyword sweep: a discipline-filtered keyword search can't
surface the canonical work — the field-defining papers (Gabriel's "AI, Values,
and Alignment", Awad's "Moral Machine experiment", Hadfield-Menell's "Incomplete
Contracting and AI Alignment") are tagged "Multidisciplinary" in OpenAlex and
get filtered out, while the discipline buckets fill with lightly-cited
tangential papers. So the list is hand-picked (recognizable, well-cited) and
only the metadata is automated. Earlier keyword-sweep logic is in git history.

To extend: add an OpenAlex work ID to a discipline below and re-run.

    python3 fetch_openalex.py            # writes manifest.csv
"""
import csv
import json
import time
import urllib.request

API = "https://api.openalex.org/works/"
MAILTO = "hauslaca@gmail.com"

# discipline -> curated OpenAlex work IDs (the most important papers).
CURATED = {
    "Computer Science": [
        "W2626804490",  # Deep RL from human preferences (Christiano et al.)
        "W4388274718",  # AI Alignment: A Comprehensive Survey (Ji et al.)
        "W4404200702",  # Beyond Preferences in AI Alignment
        "W4224980442",  # Shared Interest: Measuring Human-AI Alignment
        "W4285392457",  # In situ bidirectional human-robot value alignment
    ],
    "Political Science": [
        "W2990856437",  # What is the State of AI Governance Globally?
        "W4214919116",  # The politics of AI regulation and governance
        "W3005462201",  # Should AI Governance be Centralised?
        "W4297840560",  # Law Informs Code: aligning AI via legal informatics
        "W4398208103",  # AI, the common good, and the democratic deficit
    ],
    "Psychology": [
        "W2896252141",  # The Moral Machine experiment (Awad et al., Nature)
        "W2886363025",  # People are averse to machines making moral decisions
        "W4391592270",  # Understanding Artificial Agency
        "W3217342481",  # Could artificial intelligence have consciousness?
    ],
    "Economics": [
        "W2963086506",  # Incomplete Contracting and AI Alignment (Hadfield-Menell & Hadfield)
        "W2776311290",  # AI and Its Implications for Income Distribution & Unemployment (Korinek & Stiglitz)
        "W4205434771",  # The Moral Preferences of Investors: Experimental Evidence
        "W2890116734",  # The Economics of Artificial Intelligence: An Agenda
    ],
    "Philosophy": [
        "W3002093512",  # Artificial Intelligence, Values, and Alignment (Gabriel)
        "W2954266614",  # A Unified Framework of Five Principles for AI in Society (Floridi & Cowls)
        "W2506282302",  # The Ethics of Artificial Intelligence (Bostrom & Yudkowsky)
        "W3022125597",  # Ethics of Artificial Intelligence and Robotics (Müller, SEP)
    ],
}


def fetch(work_id):
    url = (f"{API}{work_id}?select=id,doi,title,publication_year,"
           f"primary_location,primary_topic,cited_by_count&mailto={MAILTO}")
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def main():
    rows = []
    for discipline, ids in CURATED.items():
        got = []
        for wid in ids:
            try:
                got.append(fetch(wid))
            except Exception as e:  # noqa: BLE001
                print(f"  ! {discipline}/{wid}: {e}")
            time.sleep(0.2)
        got.sort(key=lambda w: w.get("cited_by_count", 0), reverse=True)
        for w in got:
            loc = w.get("primary_location") or {}
            src = (loc.get("source") or {}).get("display_name", "") or ""
            rows.append({
                "id": (w.get("doi") or w["id"]).replace("https://doi.org/", ""),
                "corpus": "1-cs",
                "stratum": discipline,
                "type": "paper",
                "source": src,
                "title": (w.get("title") or "").replace("\n", " ").strip(),
                "year": w.get("publication_year") or "",
                "url": w["id"],
                "accessible": "true",
                "inclusion_reason": f"discipline:{discipline}; cited_by={w.get('cited_by_count', 0)}",
                "notes": "",
                "topic": (w.get("primary_topic") or {}).get("display_name", ""),
            })
        print(f"  {discipline:18s} {len(got):2d} papers")

    cols = ["id", "corpus", "stratum", "type", "source", "title", "year",
            "url", "accessible", "inclusion_reason", "notes", "topic"]
    with open("manifest.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=cols)
        wr.writeheader()
        wr.writerows(rows)
    print(f"\nWrote {len(rows)} curated papers across {len(CURATED)} disciplines -> manifest.csv")


if __name__ == "__main__":
    main()
