"""Normalisation des dates multi-formats (repris du module 06)."""

from datetime import datetime

FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%Y%m%d"]


def normaliser(date_brute: str) -> str | None:
    """Renvoie la date au format ISO, ou None si aucun format ne convient."""
    for fmt in FORMATS:
        try:
            return datetime.strptime(date_brute.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None
