"""TP 09 — Solution."""

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parents[2] / "00-data" / "sortie"

contribuables = pd.read_csv(DATA / "contribuables.csv", dtype={"nif": str})
declarations = pd.read_csv(DATA / "declarations.csv", dtype={"nif": str})
regions = pd.read_csv(DATA / "regions.csv")

contribuables = contribuables.drop_duplicates(subset="nif")
contribuables["secteur"] = contribuables["secteur"].str.strip().str.upper()
print(f"Contribuables uniques : {len(contribuables)}")
print(contribuables["secteur"].value_counts().head(12))

declarations["tva_collectee"] = declarations["tva_collectee"].fillna(0)
declarations = declarations[declarations["chiffre_affaires"] > 0]
print(f"Déclarations valides : {len(declarations)}")

declarations["tva_nette"] = (
    declarations["tva_collectee"] - declarations["tva_deductible"]
).clip(lower=0)

ensemble = declarations.merge(contribuables, on="nif", how="left")
ensemble = ensemble.merge(
    regions[["code_region", "region"]].drop_duplicates(),
    on="code_region", how="left",
)

orphelines = ensemble["raison_sociale"].isna().sum()
print(f"Déclarations orphelines : {orphelines}")

rapport = (
    ensemble.groupby("region")["tva_nette"]
    .sum()
    .sort_values(ascending=False)
)
print(rapport)

rapport.to_csv(Path(__file__).parent / "rapport_tva_regions.csv")
rapport.to_frame().to_excel(Path(__file__).parent / "rapport_tva_regions.xlsx")
print("Rapport exporté.")
