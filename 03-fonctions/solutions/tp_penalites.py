"""TP 03 — Solution."""

def mois_entames(jours_retard: int) -> int:
    if jours_retard <= 30:
        return 0
    return (jours_retard - 31) // 30 + 1


assert mois_entames(30) == 0
assert mois_entames(31) == 1
assert mois_entames(61) == 2


def taux_penalite(jours_retard: int, plafond: float = 0.50) -> float:
    if jours_retard <= 0:
        return 0.0
    taux = 0.10 + 0.02 * mois_entames(jours_retard)
    return min(taux, plafond)


assert taux_penalite(0) == 0.0
assert taux_penalite(15) == 0.10
assert abs(taux_penalite(65) - 0.14) < 1e-9
assert taux_penalite(2000) == 0.50


def penalite(tva_due: int, jours_retard: int) -> int:
    return round(tva_due * taux_penalite(jours_retard))


print(f"Pénalité (TVA 8 100 000, 45 j de retard) : {penalite(8_100_000, 45):,} GNF")
