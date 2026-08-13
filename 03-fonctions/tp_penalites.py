"""TP 03 — Fonctions : pénalités de retard de déclaration.

Règle métier (simplifiée) :
  - dépôt à l'heure : pénalité nulle
  - retard ≤ 30 jours : 10 % de la TVA due
  - retard > 30 jours : 10 % + 2 % par mois entamé au-delà du 1er mois,
    plafonné à 50 % au total.
"""

# --- 1. Mois de retard ------------------------------------------------------
def mois_entames(jours_retard: int) -> int:
    """Nombre de mois entamés au-delà du premier mois de retard.

    Exemples : 31 jours → 1 ; 61 jours → 2 ; 30 jours → 0.
    """
    # À COMPLÉTER (astuce : division entière // et attention au bord 30)
    ...


assert mois_entames(30) == 0
assert mois_entames(31) == 1
assert mois_entames(61) == 2

# --- 2. Taux de pénalité ----------------------------------------------------
def taux_penalite(jours_retard: int, plafond: float = 0.50) -> float:
    """Taux de pénalité applicable, plafonné (50 % par défaut)."""
    # À COMPLÉTER : appliquez la règle métier, en réutilisant mois_entames()
    # et la fonction min() pour le plafond.
    ...


assert taux_penalite(0) == 0.0
assert taux_penalite(15) == 0.10
assert abs(taux_penalite(65) - 0.14) < 1e-9
assert taux_penalite(2000) == 0.50

# --- 3. Montant final -------------------------------------------------------
def penalite(tva_due: int, jours_retard: int) -> int:
    """Montant de la pénalité, arrondi au FCFA."""
    # À COMPLÉTER : une seule ligne suffit.
    ...


print(f"Pénalité (TVA 8 100 000, 45 j de retard) : {penalite(8_100_000, 45):,} FCFA")

# --- 4. Pour aller plus loin ------------------------------------------------
# Ajoutez un paramètre nommé `taux_base=0.10` à taux_penalite() et vérifiez
# que les assert passent toujours.
