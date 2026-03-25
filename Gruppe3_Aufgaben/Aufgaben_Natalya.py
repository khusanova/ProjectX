"""
Aufgaben_Natalya.py
Created: 25.03.26 12:40
Author: natalya
Project: ProjectX

"""
from typing import Any, Optional


# Gruppe: Natalya
def aufgabe_043_dict_without_keys(data: dict[str, int], keys: list[str]) -> dict[str, int]:
    """Gib ein neues Dict ohne die angegebenen Schlüssel zurück."""
    return {k: v for k, v in data.items() if k not in keys}  # als Dict Comprehension


# Gruppe: Natalya
def aufgabe_046_set_union(a: set[int], b: set[int]) -> set[int]:
    """Vereinigung zweier Sets zurückgeben."""
    pass


# Gruppe: Natalya
def aufgabe_049_remove_duplicates_preserve_order(werte: list[str]) -> list[str]:
    """Entferne doppelte Einträge aus einer Stringliste, Reihenfolge behalten."""
    pass


# Gruppe: Natalya
def aufgabe_052_factorial(n: int) -> int:
    """Berechne n! iterativ oder rekursiv."""
    pass


# Gruppe: Natalya
def aufgabe_055_primzahlen_bis(limit: int) -> list[int]:
    """Gib alle Primzahlen bis inklusive limit zurück."""
    pass


# Gruppe: Natalya
def aufgabe_058_durchschnitt_gewichtet(werte: list[float], gewichte: list[float]) -> float:
    """Berechne den gewichteten Mittelwert, gleiche Länge vorausgesetzt."""
    pass
