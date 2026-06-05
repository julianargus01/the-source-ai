#!/usr/bin/env python3
"""
Fetch GitHub trending repos and regenerate data/trending.js.
Pure stdlib — no pip deps needed.
Run: python3 tools/fetch_trending.py
"""
import json
import re
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


class TrendingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.repos = []
        self._in_article = False
        self._article_data = {}
        self._capture = None
        self._depth = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and "Box-row" in attrs.get("class", ""):
            self._in_article = True
            self._article_data = {"fullName": "", "url": "", "description": "",
                                   "language": "", "stars": "", "momentum": ""}
            self._depth = 0
        if not self._in_article:
            return
        self._depth += 1

        href = attrs.get("href", "")
        if tag == "a" and href and href.count("/") == 2 and self._article_data["fullName"] == "":
            # First repo link: /owner/repo
            clean = href.strip("/")
            if clean and "." not in clean.split("/")[0]:
                self._article_data["fullName"] = clean
                self._article_data["url"] = "https://github.com" + href

        cls = attrs.get("class", "")
        if tag == "span" and "programmingLanguage" in attrs.get("itemprop", ""):
            self._capture = "language"
        elif tag == "a" and href and href.endswith("/stargazers"):
            self._capture = "stars"
        elif tag == "span" and "float-sm-right" in cls:
            self._capture = "momentum"
        elif tag == "p" and not self._article_data["description"]:
            self._capture = "description"

    def handle_data(self, data):
        if not self._in_article or not self._capture:
            return
        text = data.strip()
        if text:
            key = self._capture
            self._article_data[key] = (self._article_data.get(key, "") + " " + text).strip()

    def handle_endtag(self, tag):
        if not self._in_article:
            return
        if tag in ("span", "a", "p"):
            self._capture = None
        if tag == "article":
            self._in_article = False
            r = self._article_data
            if r["fullName"] and "/" in r["fullName"]:
                self.repos.append({k: v.strip() for k, v in r.items()})
            self._capture = None


def fetch(period: str) -> list:
    url = f"https://github.com/trending?since={period}"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    parser = TrendingParser()
    parser.feed(html)
    return parser.repos[:15]


def main():
    print("Fetching daily trending...")
    daily = fetch("daily")
    print(f"  {len(daily)} repos")

    print("Fetching weekly trending...")
    weekly = fetch("weekly")
    print(f"  {len(weekly)} repos")

    data = {"daily": daily, "weekly": weekly}

    # Save JSON
    json_path = ROOT / "data" / "trending.json"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Written: {json_path}")

    # Regenerate JS
    js_path = ROOT / "data" / "trending.js"
    js_path.write_text(
        f"// The Source — GitHub trending data\n"
        f"// Fetched: {date.today()}\n"
        f"window.TRENDING_DATA = {json.dumps(data, ensure_ascii=False, separators=(',', ':'))};\n"
    )
    print(f"Written: {js_path}")

    if daily:
        print(f"Sample: {daily[0]['fullName']} — {daily[0]['description'][:60]}")


if __name__ == "__main__":
    main()
