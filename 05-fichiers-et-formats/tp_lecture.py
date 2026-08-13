"""TP 05 — Fichiers et formats : lire les vrais jeux de données."""

import csv
import json
from pathlib import Path

DATA = Path(__file__).parent.parent / "00-data" / "sortie"

# --- 1. Lire le référentiel des régions -------------------------------------
# À COMPLÉTER : avec open(...) et csv.DictReader, construisez le dictionnaire
# {code_region: nom_de_region} à partir de regions.csv.
# N'oubliez pas encoding="utf-8" et le bloc with.
regions = {}
...
print(f"{len(regions)} codes région chargés : {regions}")

# --- 2. Compter les contribuables par région --------------------------------
# À COMPLÉTER : lisez contribuables.csv et comptez les lignes par
# code_region, puis affichez le NOM de la région (via le dict `regions`).
compte = {}
...
for code, n in sorted(compte.items(), key=lambda kv: -kv[1]):
    print(f"{regions.get(code, code):12s} : {n}")

# --- 3. Écrire un extrait ---------------------------------------------------
# À COMPLÉTER : écrivez dans extrait_bissau.csv (dans CE dossier) les seuls
# contribuables du secteur autonome de Bissau, région BIS (Bissau), avec csv.DictWriter (mêmes colonnes).
...
print("extrait_bissau.csv écrit.")

# --- 4. JSON imbriqué -------------------------------------------------------
# À COMPLÉTER : chargez dossiers_fiscaux.json et comptez combien de dossiers
# ont AU MOINS un établissement secondaire actif.
...
