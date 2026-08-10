"""TP 07 — Utiliser son propre paquet.

Exécuter DEPUIS ce dossier :
    uv run python tp_utiliser_paquet.py
"""

from fiscalite import normaliser, penalite

print(normaliser("14/03/2025"))            # → 2025-03-14
print(penalite(8_100_000, 45))             # → 972000 une fois penalites.py complété

# À COMPLÉTER : importez aussi taux_penalite et affichez le taux pour
# 10, 45 et 400 jours de retard, en pourcentage.
