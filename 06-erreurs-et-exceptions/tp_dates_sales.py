"""TP 06 — Exceptions : normaliser des dates multi-formats.

Le champ date_depot de declarations.csv mélange quatre formats :
    2025-03-14   14/03/2025   14-3-2025   20250314
Objectif : tout ramener au format ISO (AAAA-MM-JJ), sans jamais planter.
"""

import csv
from datetime import datetime
from pathlib import Path

DATA = Path(__file__).parent.parent / "00-data" / "sortie"

FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d"]


# --- 1. Le normalisateur ----------------------------------------------------
def normaliser(date_brute: str) -> str | None:
    """Renvoie la date au format ISO, ou None si aucun format ne convient.

    Essayez chaque format avec datetime.strptime dans un try/except
    ValueError ; au premier succès, renvoyez date.strftime("%Y-%m-%d").
    """
    # À COMPLÉTER
    ...


assert normaliser("2025-03-14") == "2025-03-14"
assert normaliser("14/03/2025") == "2025-03-14"
assert normaliser("14-3-2025") == "2025-03-14"
assert normaliser("20250314") == "2025-03-14"
assert normaliser("n'importe quoi") is None

# --- 2. Application au fichier réel -----------------------------------------
# À COMPLÉTER : parcourez declarations.csv, comptez les dates normalisées
# avec succès et les échecs. Affichez le bilan.
ok, echecs = 0, 0
...
print(f"Dates normalisées : {ok} | échecs : {echecs}")

# --- 3. Montants suspects ---------------------------------------------------
def lire_montant(texte: str) -> int:
    """Convertit un montant en int.

    Lève ValueError avec un message clair si le champ est vide ou négatif.
    """
    # À COMPLÉTER : int(texte) peut lui-même lever ValueError ; à vous de
    # décider quoi laisser passer et quoi enrichir avec raise.
    ...


# À COMPLÉTER : comptez les chiffres d'affaires invalides du fichier en
# appelant lire_montant dans un try/except.
