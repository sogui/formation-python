"""TP 04 — Structures de données : mini-annuaire de contribuables."""

# Un annuaire : liste de dictionnaires (structure la plus courante en Python).
annuaire = [
    {"nif": "100000001", "nom": "Ets Diallo", "region": "Conakry", "regime": "Forfait"},
    {"nif": "100000002", "nom": "Barry & Frères", "region": "Kindia", "regime": "Réel normal"},
    {"nif": "100000003", "nom": "Ets Camara", "region": "Conakry", "regime": "Réel simplifié"},
    {"nif": "100000004", "nom": "Ets Sow", "region": "Labé", "regime": "Forfait"},
    {"nif": "100000002", "nom": "Barry & Frères", "region": "Kindia", "regime": "Réel normal"},
]

# --- 1. Comptage par région -------------------------------------------------
# À COMPLÉTER : construisez un dictionnaire {region: nombre de contribuables}
# avec une boucle et dict.get(cle, 0).
par_region = {}
...
print(par_region)

# --- 2. Dédoublonnage par NIF -----------------------------------------------
# À COMPLÉTER : avec un ensemble (set) des NIF déjà vus, construisez la
# liste `uniques` sans doublons (le NIF ...002 apparaît deux fois).
vus = set()
uniques = []
...
print(f"{len(annuaire)} entrées → {len(uniques)} uniques")

# --- 3. Comparaison de deux ensembles ---------------------------------------
nifs_declarants = {"100000001", "100000003", "100000009"}
nifs_annuaire = {c["nif"] for c in uniques}

# À COMPLÉTER : quels NIF ont déclaré sans être dans l'annuaire ? (différence)
orphelins = ...
print(f"Déclarants inconnus de l'annuaire : {orphelins}")

# --- 4. Tri -----------------------------------------------------------------
# À COMPLÉTER : triez `uniques` par nom avec sorted() et l'argument key.
tries = ...
for c in tries:
    print(c["nif"], "-", c["nom"])
