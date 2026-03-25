# Python-Übungsset (100 Funktionen)

Dieses Repository enthält 100 Basis-Übungsfunktionen in `aufgaben.py`. Jede
Funktion hat einen deutschen Docstring, `pass` als Platzhalter und soll von den
Studierenden implementiert werden. Fokus: Strings, Listen, Dicts/Sets,
Schleifen, einfache Mathematik und saubere Funktionalität.

## Gruppenaufteilung (5 Gruppen)
- **Gruppe 1** (Alexander, Erik, Jan B): Funktionen 1–20 (`aufgabe_001` bis `aufgabe_020`)
- **Gruppe 2** (Jennifer, Eric, Vincent): Funktionen 21–40 (`aufgabe_021` bis `aufgabe_040`)
- **Gruppe 3** (Muhammad, Yanu, Natalya): Funktionen 41–60 (`aufgabe_041` bis `aufgabe_060`)
- **Gruppe 4** (Felix, Andreas, Johannes): Funktionen 61–80 (`aufgabe_061` bis `aufgabe_080`)
- **Gruppe 5** (Jan R., York-Phillipp, Michael): Funktionen 81–100 (`aufgabe_081` bis `aufgabe_100`)

Hinweis: Die Nummer ist im Funktionsnamen enthalten. Bitte bearbeitet nur den
euch zugewiesenen Bereich, damit Merge-Konflikte minimiert werden. Eure Namen
stehen auch direkt als Kommentar über jeder Aufgabe in `aufgaben.py`.

## Vorgehensweise für Studierende
1. Repository klonen: `git clone <repo-url>`
2. In das Repo wechseln: `cd Project-x`
3. Eigenen Branch anlegen (Beispiel für Gruppe 1, Person Arne):
   - `git checkout -b gruppe-1/arne`
4. Nur eure Funktionen in `aufgaben.py` implementieren (Docstring lesen).
5. Lokale Checks (Beispiele):
   - Optional: einfache Selbsttests schreiben/ausführen
   - Falls Tests bereitgestellt werden: `python -m pytest`
6. Änderungen prüfen: `git status`
7. Änderungen vormerken und committen:
   - `git add aufgaben.py`
   - `git commit -m "Implementiere Aufgaben 001-010"`
8. Branch pushen: `git push origin gruppe-1/arne`
9. Pull Request (PR) im Git-Host erstellen. Reviewer: Dozent oder Teamlead.
10. Feedback einarbeiten, PR aktualisieren (`git add` + `git commit --amend` oder
    neuer Commit, dann `git push --force-with-lease` bei amend).

## Qualitätsleitplanken
- Halte dich an PEP 8 (Lesbarkeit vor Cleverness).
- Sinnvolle Variablennamen, kurze Funktionen, keine unnötigen globalen Zustände.
- Docstrings nicht löschen; ergänze Beispiele, falls hilfreich.
- Prüfe Randfälle (leere Listen, None, negative Zahlen, Sonderzeichen).
- Schreibe kleine, wiederverwendbare Hilfsfunktionen nur, wenn nötig.

## Konflikte vermeiden
- Arbeite ausschließlich im zugewiesenen Funktionsbereich.
- Ziehe vor neuem Work `git pull origin main` (oder `git fetch` + `git rebase`).
- Bei Konflikten: ruhig bleiben, Konflikt markieren, lokal testen, erst dann
  committen.

## Abgabeformat
- Ein PR pro Person/Branch.
- Commit-Messages: kurz und beschreibend (z.B. `Implementiere Aufgaben 035-040`).
- Keine Änderungen an fremden Bereichen oder an der Gruppenaufteilung.

Viel Erfolg und fragt bei Unklarheiten früh nach!
