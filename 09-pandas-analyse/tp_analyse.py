"""TP 09 — pandas : rapport TVA par région, de bout en bout."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent.parent / "00-data" / "sortie"

# --- 1. Chargement ----------------------------------------------------------
contribuables = pd.read_csv(DATA / "contribuables.csv", dtype={"nif": str})
declarations = pd.read_csv(DATA / "declarations.csv", dtype={"nif": str})
regions = pd.read_csv(DATA / "regions.csv")

print(contribuables.info())

# --- 2. Nettoyage des contribuables -----------------------------------------
# À COMPLÉTER :
#   a) supprimez les doublons de NIF (drop_duplicates, subset="nif")
#   b) normalisez le secteur : .str.strip().str.upper()
contribuables = ...
contribuables["secteur"] = ...
print(f"Contribuables uniques : {len(contribuables)}")
print(contribuables["secteur"].value_counts().head(12))

# --- 3. Nettoyage des déclarations ------------------------------------------
# À COMPLÉTER :
#   a) tva_collectee contient des vides → remplacez par 0 (fillna)
#   b) écartez les chiffres d'affaires <= 0 (masque booléen)
declarations["tva_collectee"] = ...
declarations = ...
print(f"Déclarations valides : {len(declarations)}")

# --- 4. TVA nette ------------------------------------------------------------
# À COMPLÉTER : colonne tva_nette = (collectée − déductible), plancher à 0
# (astuce : .clip(lower=0))
declarations["tva_nette"] = ...

# --- 5. Jointures ------------------------------------------------------------
# À COMPLÉTER : joignez déclarations ← contribuables (sur nif, how="left"),
# puis ← référentiel régions dédoublonné sur code_region :
#     regions[["code_region", "region"]].drop_duplicates()
ensemble = ...

# Combien de déclarations n'ont pas trouvé leur contribuable ?
orphelines = ensemble["raison_sociale"].isna().sum()
print(f"Déclarations orphelines : {orphelines}")

# --- 6. Le rapport -----------------------------------------------------------
# À COMPLÉTER : TVA nette totale par région, triée décroissante (groupby)
rapport = ...
print(rapport)

# À COMPLÉTER : exportez en CSV (rapport_tva_regions.csv) puis en Excel.
...
print("Rapport exporté.")
