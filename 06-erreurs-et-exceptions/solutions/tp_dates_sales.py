"""TP 06 — Solution."""

import csv
from datetime import datetime
from pathlib import Path

DATA = Path(__file__).parents[2] / "00-data" / "sortie"

FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d"]


def normaliser(date_brute: str) -> str | None:
    for fmt in FORMATS:
        try:
            return datetime.strptime(date_brute.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


assert normaliser("2025-03-14") == "2025-03-14"
assert normaliser("14/03/2025") == "2025-03-14"
assert normaliser("14-3-2025") == "2025-03-14"
assert normaliser("20250314") == "2025-03-14"
assert normaliser("n'importe quoi") is None

ok, echecs = 0, 0
with open(DATA / "declarations.csv", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        if normaliser(ligne["date_depot"]) is not None:
            ok += 1
        else:
            echecs += 1
print(f"Dates normalisées : {ok} | échecs : {echecs}")


def lire_montant(texte: str) -> int:
    if texte.strip() == "":
        raise ValueError("montant vide")
    montant = int(texte)          # peut lever ValueError (non numérique)
    if montant < 0:
        raise ValueError(f"montant négatif : {montant}")
    return montant


invalides = 0
with open(DATA / "declarations.csv", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        try:
            lire_montant(ligne["chiffre_affaires"])
        except ValueError:
            invalides += 1
print(f"Chiffres d'affaires invalides : {invalides}")
