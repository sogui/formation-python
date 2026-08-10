# 00 — Jeux de données

Tous les jeux de données de la formation sont **engendrés localement** par les
scripts de ce dossier. Aucun téléchargement, aucune donnée réelle.

```bash
python generate_data.py --auto        # dimensionné selon la RAM du poste
python generate_json.py --dossiers 2000
```

Les fichiers sont produits dans `sortie/`, qui n'est **jamais versionné**.

## Fichiers produits

| Fichier | Contenu | Défauts volontaires |
| ------- | ------- | ------------------- |
| `regions.csv` | Référentiel régions/préfectures | Aucun (référence propre) |
| `contribuables.csv` | Annuaire des contribuables (NIF) | Doublons, libellés incohérents, téléphones manquants |
| `declarations.csv` | Déclarations TVA mensuelles | Dates multi-formats, CA aberrants, TVA manquante |
| `paiements.csv` | Paiements | NIF orphelins, dates multi-formats |
| `dossiers_fiscaux.json` | Dossiers imbriqués | Structure à plusieurs niveaux |

Les défauts sont **voulus** : les modules 06 (exceptions) et 09 (pandas)
apprennent précisément à les détecter et les corriger.

> ⚠️ Régénérez toujours avec `--jeu tous` : les déclarations et paiements
> référencent les NIF du fichier contribuables.
