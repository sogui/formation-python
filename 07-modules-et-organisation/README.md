# 07 — Modules et organisation d'un projet

**Objectifs** : sortir du fichier unique — organiser son code en modules et
paquets, comprendre ce que fait `uv`.

## Déroulé

1. `import` : bibliothèque standard, vos propres fichiers
2. `if __name__ == "__main__"` : script vs module
3. Un paquet : le dossier `fiscalite/` fourni ici
4. `pyproject.toml`, `uv sync`, `uv add` : d'où viennent les bibliothèques
5. Bonnes pratiques : un module = une responsabilité

## TP

Le paquet `fiscalite/` regroupe les fonctions écrites aux modules 03 et 06.
Complétez `fiscalite/penalites.py`, puis utilisez le paquet depuis
`tp_utiliser_paquet.py`.
