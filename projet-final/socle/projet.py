"""Projet final — Squelette commun à tous les sujets.

Complétez UNIQUEMENT les blocs marqués « À VOUS DE JOUER ».
La structure (lecture → validation → traitement → rapport) est imposée.

    uv run python projet.py --aide-sujet
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent.parent.parent / "00-data" / "sortie"


def charger() -> dict[str, pd.DataFrame]:
    """Charge les fichiers nécessaires à votre sujet."""
    try:
        return {
            "contribuables": pd.read_csv(DATA / "contribuables.csv", dtype={"nif": str}),
            "declarations": pd.read_csv(DATA / "declarations.csv", dtype={"nif": str}),
            "paiements": pd.read_csv(DATA / "paiements.csv", dtype={"nif": str}),
            "regions": pd.read_csv(DATA / "regions.csv"),
        }
    except FileNotFoundError as exc:
        sys.exit(f"Fichier manquant : {exc.filename}\n"
                 f"→ cd 00-data && python generate_data.py --auto")


def valider(tables: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Écartez l'invalide EN LE COMPTANT (rien en silence).

    ================= À VOUS DE JOUER =================
    Selon votre sujet : CA <= 0, dates inexploitables,
    doublons de NIF, TVA manquante…
    ===================================================
    """
    return tables


def traiter(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Le cœur de votre sujet.

    ================= À VOUS DE JOUER =================
    Jointures, calculs, agrégations : produisez LE
    DataFrame qui répond à votre question.
    ===================================================
    """
    raise NotImplementedError("traiter() : à écrire selon votre sujet")


def restituer(resultat: pd.DataFrame, sortie: Path) -> None:
    """Affiche l'essentiel et exporte le rapport.

    ================= À VOUS DE JOUER =================
    print() des chiffres clés + export CSV (ou Excel
    multi-feuilles pour le sujet 5).
    ===================================================
    """
    raise NotImplementedError("restituer() : à écrire selon votre sujet")


def main() -> None:
    parser = argparse.ArgumentParser(description="Projet final.")
    parser.add_argument("--sortie", default="rapport.csv", help="Fichier de sortie")
    # À VOUS DE JOUER : ajoutez les options propres à votre sujet
    # (ex. --region, --periode, --seuil)
    args = parser.parse_args()

    print("1. Chargement…")
    tables = charger()
    print("2. Validation…")
    tables = valider(tables)
    print("3. Traitement…")
    resultat = traiter(tables)
    print("4. Restitution…")
    restituer(resultat, Path(args.sortie))


if __name__ == "__main__":
    main()
