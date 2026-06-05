#!/usr/bin/env python3
"""
Generate data/mcps.js and data/trending.js for The Source website.
Run from ~/wat-builds/day5-website/: python3 tools/generate_data.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# ── MCP catalog ───────────────────────────────────────────────────────────────

mcps_raw = json.loads((Path.home() / "wat-builds/day2-scraper/.tmp/mcp-catalog.json").read_text())

def clean(s):
    if not s:
        return ""
    s = str(s).strip()
    # Remove emoji characters for clean rendering
    s = re.sub(r'[^\x00-\x7F -⁯ -ÿĀ-ɏ]+', '', s)
    return s.strip(" -|_")

mcps = []
for m in mcps_raw:
    name = clean(m.get("name", ""))
    cat = clean(m.get("category", ""))
    desc = clean(m.get("description", ""))
    url = m.get("url", "")
    src = m.get("source", "")
    if not name or not url:
        continue
    mcps.append({
        "n": name[:80],
        "d": desc[:200],
        "c": cat[:40],
        "u": url,
        "s": "glama" if src == "glama.ai" else "ams",  # compact source
    })

# Get sorted unique categories
from collections import Counter
cat_counts = Counter(m["c"] for m in mcps if m["c"])
categories = [c for c, _ in cat_counts.most_common(40) if c]

js_mcps = f"""// The Source — MCP catalog data
// {len(mcps)} servers from awesome-mcp-servers + glama.ai
// Generated: {__import__('datetime').date.today()}
window.MCP_DATA = {json.dumps(mcps, ensure_ascii=False, separators=(',', ':'))};
window.MCP_CATEGORIES = {json.dumps(categories, ensure_ascii=False)};
"""
(DATA_DIR / "mcps.js").write_text(js_mcps, encoding="utf-8")
print(f"mcps.js: {len(mcps)} entries, {len(categories)} categories, {(DATA_DIR / 'mcps.js').stat().st_size // 1024}KB")

# ── Trending repos ────────────────────────────────────────────────────────────

trending_raw = json.loads((ROOT / "data/trending.json").read_text())

js_trending = f"""// The Source — GitHub trending data
// Fetched: {__import__('datetime').date.today()}
window.TRENDING_DATA = {json.dumps(trending_raw, ensure_ascii=False, separators=(',', ':'))};
"""
(DATA_DIR / "trending.js").write_text(js_trending, encoding="utf-8")
daily_n = len(trending_raw.get("daily", []))
weekly_n = len(trending_raw.get("weekly", []))
print(f"trending.js: {daily_n} daily, {weekly_n} weekly")
print("Done.")
