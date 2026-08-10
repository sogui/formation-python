# Projet final — Consignes

Chaque groupe (2 à 3 personnes) construit une **chaîne de traitement complète**
en Python sur un sujet tiré au sort, à partir des jeux de données du dépôt.

```
CSV/JSON bruts ──► lecture ──► validation ──► traitement ──► agrégats ──► rapport
```

Le squelette est fourni dans `socle/` : vous n'écrivez que ce qui relève de
votre sujet, aux endroits marqués **« À VOUS DE JOUER »**.

---

## Les cinq sujets

| # | Sujet | Question centrale |
| - | ----- | ----------------- |
| 1 | **Défaillants** | Quels contribuables du réel n'ont déposé aucune déclaration sur une période donnée ? Par région, par secteur. |
| 2 | **Crédits de TVA** | Où la TVA déductible dépasse-t-elle durablement la collectée ? Classement des situations de crédit répété. |
| 3 | **Recouvrement** | Rapprochez déclarations et paiements par NIF : taux de couverture, restes à payer par région. |
| 4 | **Qualité des données** | Mesurez et corrigez : doublons, dates, libellés secteur, NIF orphelins. Produisez le fichier « propre » et le rapport d'anomalies. |
| 5 | **Tableau de bord régional** | Pour une région donnée : contribuables actifs, CA, TVA, top secteurs, évolution mensuelle — export Excel multi-feuilles. |

## Jalons

| Moment | Attendu |
| ------ | ------- |
| J4 fin de matinée | Sujet tiré, dépôt du groupe créé, socle exécuté tel quel |
| J4 fin de journée | Lecture + validation opérationnelles sur les vraies données |
| J5 mi-journée | Chaîne complète exécutable en une commande |
| J5 après-midi | Soutenance : 10 min de démonstration + 5 min de questions |

## Socle attendu (tous sujets)

- exécution en **une commande** : `uv run python projet.py [options]`
- aucune donnée versionnée ; le programme échoue **proprement** si les
  fichiers manquent (message clair, pas de traceback brut)
- les lignes écartées sont **comptées et affichées**, jamais perdues en silence
- un `README.md` de groupe : quoi, comment lancer, qui a fait quoi

## Grille d'évaluation (20 points)

| Critère | Points |
| ------- | ------ |
| La chaîne s'exécute de bout en bout sans erreur | 6 |
| Justesse du traitement (le résultat répond à la question) | 5 |
| Robustesse (données sales gérées, messages clairs) | 3 |
| Lisibilité (fonctions courtes, noms parlants, docstrings) | 3 |
| Soutenance (clarté, démonstration, réponses) | 3 |

**Bonus** (+1) : un graphique matplotlib pertinent dans le rapport.

## Ce qui est interdit

- versionner les fichiers de données ou les rapports produits
- le copier-coller massif non compris (vous serez interrogés dessus)
