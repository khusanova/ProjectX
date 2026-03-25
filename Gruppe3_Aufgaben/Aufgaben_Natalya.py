"""
Aufgaben_Natalya.py
Created: 25.03.26 12:40
Author: natalya
Project: ProjectX

"""


# Gruppe: Natalya
def aufgabe_043_dict_without_keys(data: dict[str, int], keys: list[str]) -> dict[str, int]:
	"""Gib ein neues Dict ohne die angegebenen Schlüssel zurück."""
	return {k: v for k, v in data.items() if k not in keys}  # als Dict Comprehension


# Gruppe: Natalya
def aufgabe_046_set_union(a: set[int], b: set[int]) -> set[int]:
	"""Vereinigung zweier Sets zurückgeben."""
	return a | b  # oder a.union(b)


# Gruppe: Natalya
def aufgabe_049_remove_duplicates_preserve_order(werte: list[str]) -> list[str]:
	"""Entferne doppelte Einträge aus einer Stringliste, Reihenfolge behalten."""
	return list(dict.fromkeys(werte))


"""
# oder schrittweise:
    seen = set()
    result = []
    for item in werte:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
"""


# Gruppe: Natalya
def aufgabe_052_factorial(n: int) -> int:
	"""Berechne n! iterativ oder rekursiv."""
	# Iterative Lösung, da auch große Zahlen geeignet
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


# Gruppe: Natalya
def aufgabe_055_primzahlen_bis(limit: int) -> list[int]:
	"""Gib alle Primzahlen bis inklusive limit zurück."""
	# 1. Prüfe den Sonderfall: Für Zahlen kleiner als 2 gibt es keine Primzahlen
	if limit < 2:
		return []

	# 2. Erstelle eine Liste, die für jede Zahl speichert, ob sie eine Primzahl ist
	# Am Anfang denken wir, dass alle Zahlen Primzahlen sind (True)
	# Wir brauchen Platz für Zahlen von 0 bis limit, deshalb limit + 1
	ist_prim = [True] * (limit + 1)

	# 3. 0 und 1 sind keine Primzahlen
	ist_prim[0] = False
	ist_prim[1] = False

	# 4. Das Sieb: Wir prüfen jede Zahl von 2 bis zur Wurzel aus limit
	# Beispiel: Bei limit=100 reicht es, bis 10 zu prüfen
	# Denn wenn eine Zahl zusammengesetzt ist, hat sie einen Teiler <= Wurzel(limit)
	grenze = int(limit ** 0.5) + 1

	for zahl in range(2, grenze):
		# Wenn die aktuelle Zahl als Primzahl markiert ist
		if ist_prim[zahl]:
			# Dann streichen wir alle Vielfachen dieser Zahl
			# Wir beginnen bei zahl * zahl, weil kleinere Vielfache schon gestrichen wurden
			vielfaches = zahl * zahl

			while vielfaches <= limit:
				ist_prim[vielfaches] = False  # Diese Zahl ist keine Primzahl
				vielfaches = vielfaches + zahl  # Gehe zum nächsten Vielfachen

	# 5. Sammle alle Primzahlen in einer Liste
	primzahlen = []
	for zahl in range(2, limit + 1):
		if ist_prim[zahl]:
			primzahlen.append(zahl)

	return primzahlen


# Gruppe: Natalya
def aufgabe_058_durchschnitt_gewichtet(werte: list[float], gewichte: list[float]) -> float:
	"""Berechne den gewichteten Mittelwert, gleiche Länge vorausgesetzt."""
	# 1. Prüfe, ob die Listen leer sind

	if not werte or not gewichte:
		return 0.0

		# 2. Berechne die gewichtete Summe (werte * gewichte)
	gewichtete_summe = 0.0
	summe_gewichte = 0.0

	for i in range(len(werte)):
		gewichtete_summe = gewichtete_summe + werte[i] * gewichte[i]
		summe_gewichte = summe_gewichte + gewichte[i]

	# 3. Vermeide Division durch Null
	if summe_gewichte == 0:
		return 0.0

	# 4. Berechne den gewichteten Durchschnitt
	durchschnitt = gewichtete_summe / summe_gewichte

	return durchschnitt
