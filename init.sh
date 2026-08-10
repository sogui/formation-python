#!/usr/bin/env bash
# Initialisation complète du poste : environnement + jeux de données.
# À lancer depuis Git Bash (Windows) ou un terminal (macOS/Linux).
set -e

echo "== Synchronisation de l'environnement =="
uv sync

echo "== Génération des jeux de données =="
cd 00-data
uv run python generate_data.py --auto
uv run python generate_json.py --dossiers 2000
cd ..

echo "== Terminé. Bonne formation ! =="
