# SVB People Intelligence Dashboard
> Organizations are complex. We made ours clear.

---

## Who I Am

- **Name:** Amber Hearn
- **Role:** UI Designer, Digital Strategy & Operations, Global Marketing, SVB
- **Coding experience:** None. Explain all code changes in plain language after making them.
- **Working style:** Design decisions are made in Claude Chat first, confirmed before any code is written. Build one component at a time. Always confirm before moving on.

---

## What We're Building

A single-page web app that visualizes SVB's organizational structure as a 2D force-directed network. 270 employee headshot nodes float organically on a canvas and cluster fluidly when filters are applied.

**Tech stack:** HTML + CSS + JavaScript + D3.js (force simulation)
**Hosting:** GitHub (code + version history) → Netlify (live URL, auto-deploys on push)

---

## Project Files

```
svb-dashboard/
├── index.html              ← the entire app lives here
├── CLAUDE.md               ← this file
├── svb-employees-final.csv ← employee data — ALWAYS load from here, never hardcode
└── headshots/              ← circular employee photos, matched by headshotFilename column
```

**Critical rule:** Data lives in the CSV. Code lives in index.html. Never mix them.

---

## Data Structure

`svb-employees-final.csv` has 270 rows and 11 columns:

| Field | Type | Source | Notes |
|---|---|---|---|
| `id` | Text | Generated | Format XXX## — e.g. MKT01, CBK03 |
| `name` | Text | SVB Data | First + Last — e.g. JP Giannini, Sarah Chen |
| `title` | Text | SVB Data | e.g. Senior Vice President, Managing Director |
| `seniority` | Text | Generated | EVP & President / SVP / VP / Director / Manager / IC |
| `department` | Text | SVB Data | e.g. Commercial Banking, Investment Banking |
| `team` | Text | Generated | e.g. Startup Banking, Private Client Advisory |
| `location` | Text | SVB Data | City only — e.g. San Francisco, New York, Boston |
| `tenure` | Number | Generated | Years at SVB |
| `reportsTo` | Text | Generated | References another employee's id. Top level is blank. |
| `headshotFilename` | Image | Library | e.g. jp-giannini.jpg |
| `profileUrl` | Text | SVB Data | e.g. svb.com/profile/jp-giannini/ |

---

## Org Structure

- **270 employees** across 6 seniority tiers
- **Top level** reports to Phil Cox or Daniel Beck (not in dataset)
- **Seniority order (top → bottom):** EVP & President → SVP → VP → Director → Manager → IC

---

## Departments & Teams

| Department | Teams |
|---|---|
| Commercial Banking | Technology & Life Sciences · Startup Banking · Growth & Mid-Market · Relationship Management · Credit & Lending |
| Private Banking & Wealth Management | Private Client Advisory · Investment Advisory · Trust & Estate Planning · Portfolio Management · Client Services |
| Investment Banking | Mergers & Acquisitions · Capital Markets · Corporate Advisory · Industry Coverage · Deal Execution |
| Asset Management & Investment Services | Fund Management · Portfolio Strategy · Risk & Compliance · Investor Relations · Operations |
| Global Fund Banking | Venture Capital Banking · Private Equity Banking · Fund Treasury Services · Capital Call Lines · Limited Partner Services |

---

## Dashboard Layout

```
┌─────────────────────────────────────────────────────┐
│  Left Filter Panel  │  Main Canvas (force-directed) │
│                     │                               │
│  [ Search bar ]     │   ○ ○ ○  ○  ○ ○               │
│                     │  ○  ○ ○    ○  ○               │
│  Department         │    ○  ○ ○  ○                  │
│  Team               │  ○ ○    ○  ○  ○               │
│  Seniority          │                               │
│  Location           │                               │
│  Tenure             │                               │
│                     │                               │
├─────────────────────┴───────────────────────────────┤
│  Bottom Stats Bar — live counts, active filters     │
└─────────────────────────────────────────────────────┘
```

---

## Core Interaction — Focus + Context

When a filter is selected:
- Matching nodes **cluster together** and light up (full opacity)
- Non-matching nodes **dim to ~20% opacity** and drift apart
- Connections between highlighted nodes remain visible
- Transition is **fluid and animated**, not a cut

Specific interactions:
- **Filter by Seniority** — all employees at that tier light up
- **Filter by Department** — all members cluster together
- **Filter by Location** — geographic groupings light up
- **Search by name** — matching node lights up instantly
- **Click a node** — opens employee detail panel (name, title, department, team, profile link)
- **Clear filter** — all nodes return to free-floating state

---

## Visual Direction

- **Background:** White. Light. Never dark.
- **Colors:** Navy `#003A61` and green `#2A7A58` as accents only — not large fills
- **Feel:** Clean, alive, considered. Glass & transparency with intention. Depth without darkness.
- **Avoid:** Flat white sterility · Generic Dribbble dashboard aesthetic
- **Fonts:** TBD — clean, professional, modern
- **Headshots:** Circular, displayed on each node

---

## Build Order

| Phase | Days | Milestone |
|---|---|---|
| Setup | 1–2 | GitHub repo, CSV wired up, Netlify live URL working |
| Shell | 3–5 | Filter panel, canvas area, stats bar — placeholder circles |
| Logic | 6–9 | Force-directed physics, clustering, filter interactions, detail panel |
| Polish | 10–12 | Real headshots, final visual design, typography |
| Wrap-up | 13–14 | Documentation, QA, presentation prep |

---

## Definition of Done

- [ ] Interactive dashboard with filtering, clustering, and node interactions fully working
- [ ] Live URL accessible from any computer via Netlify
- [ ] All code and data backed up on GitHub with version history
- [ ] Documentation written — decisions, process, next steps

---

## Claude Code Rules

1. **Explain** every code change in plain language after making it
2. **Ask** before making any structural changes
3. **Never** hardcode employee data — always load from `svb-employees-final.csv`
4. **Keep** data file separate from app code at all times
5. **Build** one component at a time — confirm with Amber before moving on
6. **Prefer** simple, readable code over clever solutions
7. **Re-read** this file at the start of every session
