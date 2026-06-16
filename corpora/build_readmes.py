#!/usr/bin/env python3
"""Generate minimal README.md files for corpora 1, 2, 4 from their manifests.

Same format as the hand-written corpus-3 README: a title, one line, then the
documents as a bullet list grouped by category, each title linking to the
original. Re-run whenever a manifest changes:

    python3 corpora/build_readmes.py

Corpus 3 is hand-maintained (it carries curated notes) and is left untouched.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Per-corpus config: which column groups the bullets, and the group order +
# display names. Counts are appended to each group heading.
CONFIG = {
    "1-cs": {
        "title": "Corpus 1 — Research",
        "intro": "The key papers on the AI value/alignment question, by "
                 "discipline. Each links to its record.",
        "group": "stratum",
        "order": ["Computer Science", "Political Science", "Psychology",
                  "Economics", "Philosophy"],
        "names": {},
    },
    "2-company": {
        "title": "Corpus 2 — Companies",
        "intro": "Documents from the five major AI developers — the reference corpus. "
                 "Each links to the original.",
        "group": "company",
        "order": ["anthropic", "openai", "deepmind", "meta", "microsoft"],
        "names": {"anthropic": "Anthropic", "openai": "OpenAI",
                  "deepmind": "DeepMind", "meta": "Meta", "microsoft": "Microsoft"},
    },
    "4-media": {
        "title": "Corpus 4 — Public discourse",
        "intro": "A curated set of major outlets. Students collect AI-alignment "
                 "articles from each. Every entry links to the outlet's AI coverage.",
        "group": "stratum",
        "order": ["Global press", "German press"],
        "names": {},
    },
}


def clean(text):
    return (text or "").replace("[", "(").replace("]", ")").strip()


def build(folder, cfg):
    with open(os.path.join(HERE, folder, "manifest.csv"), encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))

    order = list(cfg["order"])
    for r in rows:  # append any group not in the predefined order
        g = r[cfg["group"]]
        if g not in order:
            order.append(g)

    lines = [f"# {cfg['title']}", "", cfg["intro"], ""]
    for g in order:
        items = [r for r in rows if r[cfg["group"]] == g]
        if not items:
            continue
        heading = cfg["names"].get(g, g)
        lines.append(f"### {heading} ({len(items)})")
        if cfg.get("head_topics"):
            counts = {}
            for r in items:
                t = (r.get("topic") or "").strip()
                if t:
                    counts[t] = counts.get(t, 0) + 1
            top = [t for t, _ in sorted(counts.items(),
                                        key=lambda kv: kv[1], reverse=True)[:3]]
            if top:
                lines.append(f"*Head topics: {' · '.join(top)}*")
        for r in items:
            title = clean(r["title"])
            year = f" ({r['year']})" if r.get("year") else ""
            gated = "" if r.get("accessible", "true") != "false" else " — *gated*"
            url = (r.get("url") or "").strip()
            bullet = f"- [{title}]({url}){year}{gated}" if url else f"- {title}{year}{gated}"
            lines.append(bullet)
        lines.append("")
    out = os.path.join(HERE, folder, "README.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines).rstrip() + "\n")
    print(f"  {folder:12s} {len(rows):4d} docs -> README.md")


def main():
    for folder, cfg in CONFIG.items():
        build(folder, cfg)


if __name__ == "__main__":
    main()
