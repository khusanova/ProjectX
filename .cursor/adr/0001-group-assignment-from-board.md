# ADR 0001: Group assignment updated from board (yellow sheet)

## Status
Accepted (2025-02-25)

## Context
The project uses a fixed set of 100 Python exercises in `aufgaben.py` with group-based task assignment. The previous assignment used 8 groups. The instructor provided a new grouping on the board (left yellow sheet: numeric group IDs; right yellow sheet: numbered list of names). Each group should consist of 3 or more individuals.

## Decision
- **Source of truth:** The left yellow sheet defines groups by member IDs; the right sheet maps IDs to names. A sixth group (Sinan, Viktor, Martin) was added per request.
- **Adopted groups (6 groups, ~17 functions each):**
  1. **Gruppe 1:** Arne, Alina, Philipp — Funktionen 1–17
  2. **Gruppe 2:** Frank, Levent, Joahnnes — Funktionen 18–34
  3. **Gruppe 3:** Bjoern, Hakan, Markus — Funktionen 35–50
  4. **Gruppe 4:** Nick, Ladysh, Angelique — Funktionen 51–67
  5. **Gruppe 5:** Torben, Nikit, Yannic, Malte — Funktionen 68–84
  6. **Gruppe 6:** Sinan, Viktor, Martin — Funktionen 85–100
- **Artifacts updated:** `README.md` (Gruppenaufteilung, branch examples), `aufgaben.py` (every `# Gruppe: …` comment above each function).

## Consequences
- Single source of truth for groups is the board/yellow sheet plus the added Gruppe 6; code and README reflect it.
- All 100 functions have a unique group comment; merge conflicts are minimized by strict ranges.
- Viktor is now assigned in Gruppe 6 (Sinan, Viktor, Martin).
