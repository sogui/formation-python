# 10 — Intégration : la chaîne complète

**Objectifs** : assembler tout ce qui précède en un programme unique,
organisé, robuste, lancé en ligne de commande.

```
CSV bruts ──► lecture ──► validation ──► nettoyage ──► agrégats ──► rapport
```

## Ce module ne contient pas de trous

Le script `pipeline.py` est **entièrement fourni et commenté** : lisez-le,
exécutez-le, modifiez-le. Il constitue le modèle du projet final.

```bash
uv run python pipeline.py --region CKY
uv run python pipeline.py --toutes
```

## Ce qu'il illustre

- `argparse` pour les options en ligne de commande
- le paquet `fiscalite` du module 07 (dates, pénalités)
- pandas pour l'analyse (module 09)
- la séparation lecture / validation / traitement / restitution
- un `main()` court qui raconte l'histoire du programme
