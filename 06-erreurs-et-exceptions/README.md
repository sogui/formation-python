# 06 — Erreurs et exceptions

**Objectifs** : écrire du code qui résiste aux données sales — car les
fichiers administratifs le sont toujours.

## Déroulé

1. Lire un traceback sans paniquer
2. `try` / `except` / `else` / `finally`
3. Attraper des exceptions précises (`ValueError`, `KeyError`, ...)
4. Lever ses propres exceptions (`raise`)
5. Application : normaliser les dates multi-formats des jeux de données

## TP

`tp_dates_sales.py` : le fichier `declarations.csv` contient quatre formats
de date différents. Écrivez un normalisateur robuste.
