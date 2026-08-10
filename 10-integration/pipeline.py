"""Module 10 — La chaîne complète, de bout en bout.

Lit les jeux de données, valide, nettoie, agrège, produit un rapport.
Entièrement fourni : c'est le modèle du projet final.

    uv run python pipeline.py --region CKY
    uv run python pipeline.py --toutes
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent.parent / "00-data" / "sortie"

FORMATS_DATE = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d"]


# --------------------------- 1. Lecture -------------------------------------

def charger() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Charge les trois fichiers. Échec explicite si absents."""
    try:
        contribuables = pd.read_csv(DATA / "contribuables.csv", dtype={"nif": str})
        declarations = pd.read_csv(DATA / "declarations.csv", dtype={"nif": str})
        regions = pd.read_csv(DATA / "regions.csv")
    except FileNotFoundError as exc:
        sys.exit(f"Jeu de données manquant ({exc.filename}). "
                 f"Lancez d'abord : cd 00-data && python generate_data.py --auto")
    return contribuables, declarations, regions


# --------------------------- 2. Validation ----------------------------------

def normaliser_date(brute: str) -> str | None:
    """Quatre formats possibles → ISO, sinon None (module 06)."""
    for fmt in FORMATS_DATE:
        try:
            return datetime.strptime(str(brute).strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


def valider(declarations: pd.DataFrame) -> pd.DataFrame:
    """Écarte l'invalide, trace ce qu'on écarte — jamais en silence."""
    n0 = len(declarations)

    declarations = declarations[declarations["chiffre_affaires"] > 0]
    print(f"  CA invalides écartés        : {n0 - len(declarations)}")

    declarations = declarations.copy()
    declarations["date_depot"] = declarations["date_depot"].map(normaliser_date)
    n1 = len(declarations)
    declarations = declarations.dropna(subset=["date_depot"])
    print(f"  Dates inexploitables        : {n1 - len(declarations)}")

    declarations["tva_collectee"] = declarations["tva_collectee"].fillna(0)
    return declarations


# --------------------------- 3. Traitement ----------------------------------

def construire(contribuables: pd.DataFrame, declarations: pd.DataFrame,
               regions: pd.DataFrame) -> pd.DataFrame:
    """Nettoie, calcule la TVA nette, joint tout."""
    contribuables = contribuables.drop_duplicates(subset="nif").copy()
    contribuables["secteur"] = contribuables["secteur"].str.strip().str.upper()

    declarations = declarations.copy()
    declarations["tva_nette"] = (
        declarations["tva_collectee"] - declarations["tva_deductible"]
    ).clip(lower=0)

    ensemble = declarations.merge(contribuables, on="nif", how="inner")
    ensemble = ensemble.merge(
        regions[["code_region", "region"]].drop_duplicates(),
        on="code_region", how="left",
    )
    return ensemble


# --------------------------- 4. Restitution ---------------------------------

def rapport(ensemble: pd.DataFrame, code_region: str | None) -> None:
    """Affiche et exporte le rapport, global ou pour une région."""
    if code_region:
        ensemble = ensemble[ensemble["code_region"] == code_region]
        if ensemble.empty:
            sys.exit(f"Aucune donnée pour la région {code_region}.")

    tableau = (
        ensemble.groupby(["region", "secteur"])["tva_nette"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
    )
    print("\nTVA nette par région et secteur (top 15) :")
    print(tableau.to_string())

    sortie = Path(__file__).parent / "rapport_tva.csv"
    tableau.to_csv(sortie)
    print(f"\nExporté : {sortie}")


# --------------------------- main -------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Chaîne complète TVA.")
    groupe = parser.add_mutually_exclusive_group(required=True)
    groupe.add_argument("--region", help="Code région (ex. CKY)")
    groupe.add_argument("--toutes", action="store_true", help="Toutes les régions")
    args = parser.parse_args()

    print("1. Chargement…")
    contribuables, declarations, regions = charger()
    print("2. Validation…")
    declarations = valider(declarations)
    print("3. Construction…")
    ensemble = construire(contribuables, declarations, regions)
    print("4. Rapport…")
    rapport(ensemble, None if args.toutes else args.region)


if __name__ == "__main__":
    main()
