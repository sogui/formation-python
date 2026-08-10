# 05 — Fichiers et formats

**Objectifs** : lire et écrire des fichiers texte, CSV et JSON ; manipuler
les chemins avec `pathlib`.

## Prérequis

Les jeux de données doivent exister :

```bash
cd ../00-data && python generate_data.py --auto && python generate_json.py --dossiers 2000 && cd -
```

## Déroulé

1. `open()`, encodage UTF-8, gestionnaire de contexte `with`
2. `pathlib.Path` : chemins portables Windows/Linux
3. CSV : `csv.DictReader` / `csv.DictWriter`
4. JSON : `json.load` / `json.dump`, structures imbriquées

## TP

`tp_lecture.py` : lire l'annuaire des contribuables et les dossiers JSON,
produire un premier extrait filtré.
