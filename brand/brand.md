---
title: Brand Kit — The Source
date: 2026-06-05
author: claude-code
project: the-source
status: active
tags: [brand, design, reference]
---

# Brand Kit — The Source

> **Dual-layer brand spec.** Layer A (this file) is the brand-as-context an agent reads to produce on-brand work. Layer B is `brand.tokens.json`.

---

## 0. Metadata
- **name:** The Source · **version:** v1 · **updated:** 2026-06-05 · **project:** the-source
- **essence:** A terminal-native resource hub for AI builders. Deep black canvas, a shifted neon green that reads "system online" — not stock Matrix — with metallic silver as a whisper accent. Monospace headings feel like a command prompt. The data is the design.

---

## 1. Voice & strategy

- **voice:**
  - *raw* — no marketing fluff, no padding
  - *precise* — exact numbers, exact sources, no vagueness
  - *underground* — for people who already know what they're looking at
  - *alive* — data is fresh, the system is running right now
- **audience:** AI developers, Claude Code users, automation builders — specifically the Skool AI Automation Society community and anyone building with MCPs and open-source repos
- **what it is NOT:** neon-lime AI startup vibes / corporate dashboard gray / friendly-chirpy / over-explained

---

## 2. Before-you-render — REQUIRED

1. **Medium:** `web` only.
2. **Load only what applies:** universal tokens + web group. No email-safe constraints, no slide aspect rules.
3. **Render only what's asked** — a hero section is a hero section, not a whole page.
4. **Effects are opt-in:**
   - `matrix-rain` — animated falling character background. Hero moment only. Skip on reduced-motion.
   - `glow` — green drop-shadow/box-shadow on primary elements. One per section.
   - `scanline` — subtle 1px horizontal line texture overlay. Optional on hero.
   - `cursor-blink` — terminal cursor on interactive labels or CTAs.
   - Never apply animation to text blocks or data tables.
5. **Respect the color budget** (§3). The canvas must stay dark. Adding brightness to backgrounds violates the brand.

---

## 3. Usage ratios (color budget)

| Element | Budget |
|---|---|
| canvas / whitespace | >= 80% |
| ink / text | 5–10% |
| primary accent (green) | <= 3%, one moment per view |
| secondary accent (silver) | <= 2%, whisper only |
| imagery / effects | 0–10%, most renders zero |

---

## 4. Per-medium native layout notes

- **web:**
  - Viewports: mobile-first, breakpoints at 640px / 1024px / 1280px
  - Max content width: 1140px centered
  - Sections: hero / stats-bar / mcp-catalog / trending-repos / about / footer
  - Components allowed: terminal card, data table, pill tag, ghost button, glow CTA button, stat counter, animated rain background
  - Avoid: light cards on light backgrounds, any white-dominant panels

---

## 5. Principles (hard rules)

- **Dark dominates.** Canvas is near-black at all times. No light panels, no white sections.
- **Green is earned.** Primary accent appears once per view — active state, CTA, or hero label. Never fill a whole component.
- **Silver is a whisper.** Secondary accent for secondary text, borders, or muted tags only. Never louder than green.
- **Monospace headings feel like a prompt.** H1–H3 use JetBrains Mono. Body copy uses Inter. Never swap them.
- **No gradients except green glow.** The only gradient allowed is a radial glow behind the primary CTA or hero stat. No rainbow, no mesh.
- **Data forward.** Numbers and counts are the hero. Typography serves the data, not the other way around.
- **Sentence case throughout.** No ALL CAPS headlines (terminal culture, not shouting).
- **Animated background is hero-only.** Matrix rain stays in the hero. Do not repeat it in later sections.

---

## 6. Assets

- **logo:** Text wordmark — "The Source" in JetBrains Mono 600, primary green. No icon yet. Clearspace: 1× cap-height on all sides. Never recolor, stretch, or add effects beyond the standard green glow.
- **imagery / photography:** Not used. This is a data product — numbers and code, no stock photos.
- **iconography:** Line style, 1.5px stroke, 0px corner radius (sharp, terminal feel). Allowed sets: Lucide, Heroicons (outline). Never filled/rounded icon sets.

---

## 7. Tokens — Layer B
See `brand.tokens.json` (machine-readable DTCG source of truth for all values).

### Quick reference (for agents)
| Token | Value | Use |
|---|---|---|
| canvas | `#050805` | Page background |
| surface.soft | `#0D110D` | Section backgrounds |
| surface.strong | `#131A13` | Cards, panels |
| primary | `#39D353` | Green accent — one moment per view |
| secondary | `#A8B8C8` | Metallic silver — whisper only |
| text.ink | `#E8F5E8` | Headings, display |
| text.body | `#C4D4C4` | Body copy |
| text.muted | `#7A9A7A` | Secondary labels, metadata |
| fontFamily.mono | JetBrains Mono | H1–H3, code, labels |
| fontFamily.sans | Inter | Body, captions, UI text |
