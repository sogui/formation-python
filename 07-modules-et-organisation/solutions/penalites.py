"""Solution de fiscalite/penalites.py."""


def mois_entames(jours_retard: int) -> int:
    if jours_retard <= 30:
        return 0
    return (jours_retard - 31) // 30 + 1


def taux_penalite(jours_retard: int, plafond: float = 0.50) -> float:
    if jours_retard <= 0:
        return 0.0
    return min(0.10 + 0.02 * mois_entames(jours_retard), plafond)


def penalite(tva_due: int, jours_retard: int) -> int:
    return round(tva_due * taux_penalite(jours_retard))
