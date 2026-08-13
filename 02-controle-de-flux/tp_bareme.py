"""TP 02 — Contrôle de flux : régimes d'imposition.

Règle métier (simplifiée) :
    CA < 100 000 000 FCFA            → « Forfait »
    100 000 000 ≤ CA < 500 000 000  → « Réel simplifié »
    CA ≥ 500 000 000                → « Réel normal »
"""

# --- 1. Le barème -----------------------------------------------------------
def regime(ca: int) -> str:
    """Renvoie le régime d'imposition selon le chiffre d'affaires."""
    # À COMPLÉTER : if / elif / else selon la règle ci-dessus
    ...


# Vérifications rapides (doivent afficher True trois fois)
print(regime(50_000_000) == "Forfait")
print(regime(200_000_000) == "Réel simplifié")
print(regime(800_000_000) == "Réel normal")

# --- 2. Une liste de chiffres d'affaires ------------------------------------
chiffres_affaires = [45_000_000, 620_000_000, 150_000_000, 0,
                     98_000_000, 510_000_000, 320_000_000, -5_000_000]

# À COMPLÉTER : avec une boucle for, comptez combien de CA sont invalides
# (négatifs ou nuls) — variable nb_invalides
nb_invalides = 0
...
print(f"CA invalides : {nb_invalides}")

# --- 3. Compréhension -------------------------------------------------------
# À COMPLÉTER : construisez la liste des régimes des seuls CA valides (> 0)
# en UNE ligne, avec une compréhension de liste.
regimes = ...
print(regimes)

# --- 4. Pour aller plus loin ------------------------------------------------
# Avec une boucle while, doublez un CA de départ de 10 000 000 jusqu'à ce
# qu'il dépasse le seuil du réel normal, en comptant le nombre d'années.
