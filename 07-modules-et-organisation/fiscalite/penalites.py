"""Calcul des pénalités de retard (repris du module 03).

À COMPLÉTER : recopiez (ou améliorez !) vos fonctions du module 03.
"""


def mois_entames(jours_retard: int) -> int:
    """Mois entamés au-delà du premier mois de retard."""
    ...  # À COMPLÉTER


def taux_penalite(jours_retard: int, plafond: float = 0.50) -> float:
    """Taux de pénalité applicable, plafonné."""
    ...  # À COMPLÉTER


def penalite(tva_due: int, jours_retard: int) -> int:
    """Montant de la pénalité, arrondi au GNF."""
    ...  # À COMPLÉTER
