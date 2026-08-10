"""TP 05 — Solution."""

import csv
import json
from pathlib import Path

DATA = Path(__file__).parents[2] / "00-data" / "sortie"

regions = {}
with open(DATA / "regions.csv", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        regions[ligne["code_region"]] = ligne["region"]
print(f"{len(regions)} codes région chargés : {regions}")

compte = {}
with open(DATA / "contribuables.csv", encoding="utf-8") as f:
    for ligne in csv.DictReader(f):
        code = ligne["code_region"]
        compte[code] = compte.get(code, 0) + 1
for code, n in sorted(compte.items(), key=lambda kv: -kv[1]):
    print(f"{regions.get(code, code):12s} : {n}")

with open(DATA / "contribuables.csv", encoding="utf-8") as f_in, \
     open(Path(__file__).parent / "extrait_conakry.csv", "w",
          newline="", encoding="utf-8") as f_out:
    lecteur = csv.DictReader(f_in)
    scribe = csv.DictWriter(f_out, fieldnames=lecteur.fieldnames)
    scribe.writeheader()
    for ligne in lecteur:
        if ligne["code_region"] == "CKY":
            scribe.writerow(ligne)
print("extrait_conakry.csv écrit.")

with open(DATA / "dossiers_fiscaux.json", encoding="utf-8") as f:
    dossiers = json.load(f)
avec_etab_actif = sum(
    1 for d in dossiers
    if any(e["actif"] for e in d["etablissements"])
)
print(f"Dossiers avec établissement secondaire actif : {avec_etab_actif}")
