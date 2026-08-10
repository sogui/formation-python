# Formation Python

Support de la formation « Python, Fondamentaux et Analyse de Données ».

Ce dépôt contient l'ensemble du matériel : supports, exercices, jeux de données,
environnement technique et consignes de projet.

---

## Démarrer

### 1. Installer les outils

Suivez **[INSTALLATION.md](INSTALLATION.md)** : Visual Studio Code, ses
extensions, et `uv` pour la gestion de Python. Comptez vingt à trente minutes.

### 2. Récupérer le dépôt

```bash
git clone <adresse-du-depot> formation-python
cd formation-python
uv sync
```

`uv sync` installe la version de Python attendue et toutes les bibliothèques,
aux versions exactes. Tout le monde obtient ainsi le même environnement.

### 3. Engendrer les jeux de données

```bash
cd 00-data
python generate_data.py --auto
```

L'option `--auto` dimensionne les fichiers selon la mémoire de votre poste.

> ⚠️ Utilisez toujours `--jeu tous` si vous régénérez : produire `contribuables`
> seul rendrait incohérentes les déclarations et les paiements qui s'y réfèrent.

### 4. Chaque matin

Faire si besoin :

```bash
git pull
```

Gérer les conflits si besoin sur git.

---

## Organisation du dépôt

Les modules sont numérotés dans l'ordre où ils sont abordés, mais nommés par **thème**.

| Module                      | Contenu                                              |
| --------------------------- | ---------------------------------------------------- |
| `00-data/`                  | Générateurs des jeux de données                      |
| `01-premiers-pas/`          | Interpréteur, variables, types, chaînes              |
| `02-controle-de-flux/`      | Conditions, boucles, compréhensions                  |
| `03-fonctions/`             | Définition, arguments, portée, documentation         |
| `04-structures-de-donnees/` | Listes, dictionnaires, ensembles, tuples             |
| `05-fichiers-et-formats/`   | Lecture/écriture, CSV, JSON, chemins                 |
| `06-erreurs-et-exceptions/` | try/except, validation, données sales                |
| `07-modules-et-organisation/` | Modules, paquets, `uv`, structure d'un projet      |
| `08-poo/`                   | Classes, objets, méthodes, dataclasses               |
| `09-pandas-analyse/`        | DataFrames, nettoyage, agrégations, jointures        |
| `10-integration/`           | La chaîne complète, de bout en bout                  |
| `projet-final/`             | Consignes, grille d'évaluation, socle technique      |
| `slides/`                   | Supports projetés, publiés au fil de l'eau           |

### Correspondance avec les journées

| Jour                                          | Modules              |
| --------------------------------------------- | -------------------- |
| **J1** — Fondamentaux du langage              | `01`, `02`           |
| **J2** — Fonctions et structures de données   | `03`, `04`           |
| **J3** — Fichiers, formats et robustesse      | `05`, `06`, `07`     |
| **J4** — Objets et analyse de données         | `08`, `09`           |
| **J5** — Intégration et projets               | `10`, `projet-final` |

Chaque module contient un `README.md` ainsi que des exercices à compléter.

---

## Les jeux de données

Tous sont **engendrés localement** : aucun téléchargement, aucune dépendance
extérieure. Ils reproduisent des données d'une administration fiscale —
contribuables identifiés par NIF, déclarations, paiements, régions et
préfectures de Guinée — avec les imperfections des fichiers administratifs :
libellés incohérents, valeurs aberrantes, formats de date multiples, doublons.

| Générateur                  | Produit                                               |
| --------------------------- | ----------------------------------------------------- |
| `generate_data.py`          | Contribuables, déclarations TVA, paiements, référentiels |
| `generate_json.py`          | Dossiers fiscaux en JSON imbriqué, avec historiques   |

```bash
python generate_data.py --auto                 # dimensionné selon la RAM
python generate_data.py --jeu tous --lignes 50000
python generate_json.py --dossiers 5000        # pour le module 05
```

Les fichiers produits ne sont **jamais** versionnés : ils se régénèrent en
quelques secondes.

---

## Le projet

Chaque groupe construit une petite application complète en Python sur un
sujet tiré au sort.

```
générateur ──► lecture & validation ──► traitement ──► agrégats ──► rapport
```

Tout est décrit dans **[projet-final/consignes.md](projet-final/consignes.md)** :
les cinq sujets, les jalons, le socle attendu, la grille d'évaluation.

Le squelette technique est fourni dans `projet-final/socle/` — vous n'écrivez
que ce qui relève de votre sujet, aux endroits marqués « À VOUS DE JOUER ».

---

## Environnement technique

| Composant | Version |
| --------- | ------- |
| Python    | 3.12    |
| pandas    | 2.x     |
| uv        | dernière stable |

Aucun service externe, aucune base de données : tout tourne sur le poste.

---

## Conventions

Les scripts `.sh` s'exécutent depuis **Git Bash** sous Windows, jamais depuis
PowerShell. Le fichier `.gitattributes` force les fins de ligne LF sur les
scripts — sans quoi Bash échoue avec un message obscur.

Ne versionnez jamais les jeux de données engendrés (le `.gitignore` s'en charge).

Les exercices sont conçus pour être exécutés dans l'ordre. Ceux des premiers
modules comportent des passages à compléter, marqués `À COMPLÉTER` ; les
solutions sont publiées au fil de l'eau dans le dossier `solutions/` de chaque
module.

---

*Formation conçue pour la montée en compétences des agents — contexte
d'administration fiscale (données pédagogiques fictives).*
