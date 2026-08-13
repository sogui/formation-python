"""TP 04 — Solution."""

annuaire = [
    {"nif": "100000001", "nom": "Ets Djaló", "region": "Bissau", "regime": "Forfait"},
    {"nif": "100000002", "nom": "Embaló & Irmãos", "region": "Bafatá", "regime": "Réel normal"},
    {"nif": "100000003", "nom": "Ets Camará", "region": "Bissau", "regime": "Réel simplifié"},
    {"nif": "100000004", "nom": "Ets Sané", "region": "Gabú", "regime": "Forfait"},
    {"nif": "100000002", "nom": "Embaló & Irmãos", "region": "Bafatá", "regime": "Réel normal"},
]

par_region = {}
for c in annuaire:
    par_region[c["region"]] = par_region.get(c["region"], 0) + 1
print(par_region)

vus = set()
uniques = []
for c in annuaire:
    if c["nif"] not in vus:
        vus.add(c["nif"])
        uniques.append(c)
print(f"{len(annuaire)} entrées → {len(uniques)} uniques")

nifs_declarants = {"100000001", "100000003", "100000009"}
nifs_annuaire = {c["nif"] for c in uniques}
orphelins = nifs_declarants - nifs_annuaire
print(f"Déclarants inconnus de l'annuaire : {orphelins}")

tries = sorted(uniques, key=lambda c: c["nom"])
for c in tries:
    print(c["nif"], "-", c["nom"])
