"""Générateur de dossiers fiscaux en JSON imbriqué.

Chaque dossier contient l'identité du contribuable, ses établissements
secondaires et l'historique de ses changements de régime — structure
imbriquée typique d'un export applicatif, exploitée au module 05.

Usage :
    python generate_json.py --dossiers 5000
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

random.seed(2026)

SORTIE = Path(__file__).parent / "sortie"

PRENOMS = ["Mamadou", "Fatoumata", "Ibrahima", "Aissatou", "Ousmane", "Mariama",
           "Alpha", "Kadiatou", "Sékou", "Aminata"]
NOMS = ["Diallo", "Bah", "Barry", "Sow", "Camara", "Condé", "Touré", "Sylla", "Keita", "Soumah"]
VILLES = ["Conakry", "Kindia", "Kankan", "Labé", "Nzérékoré", "Boké", "Mamou", "Faranah"]
REGIMES = ["Forfait", "Réel simplifié", "Réel normal"]


def dossier(i: int) -> dict:
    nb_etabs = random.choices([0, 1, 2, 3], weights=[50, 30, 15, 5])[0]
    nb_hist = random.randint(1, 3)
    annees = sorted(random.sample(range(2015, 2026), nb_hist))
    return {
        "nif": f"{100000000 + i}",
        "identite": {
            "raison_sociale": f"Ets {random.choice(PRENOMS)} {random.choice(NOMS)}",
            "ville": random.choice(VILLES),
        },
        "etablissements": [
            {"code": f"ETAB-{i}-{k}", "ville": random.choice(VILLES),
             "actif": random.random() > 0.2}
            for k in range(nb_etabs)
        ],
        "historique_regimes": [
            {"annee": a, "regime": random.choice(REGIMES)} for a in annees
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dossiers", type=int, default=2000)
    args = parser.parse_args()

    SORTIE.mkdir(exist_ok=True)
    chemin = SORTIE / "dossiers_fiscaux.json"
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump([dossier(i) for i in range(args.dossiers)], f,
                  ensure_ascii=False, indent=2)
    print(f"{chemin} : {args.dossiers} dossiers imbriqués")


if __name__ == "__main__":
    main()
