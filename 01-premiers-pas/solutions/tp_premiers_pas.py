"""TP 01 — Solution."""

nif = "100004512"
raison_sociale = "  ets fatumata djaló  "
chiffre_affaires = 45_000_000
taux_tva = 0.18

raison_propre = raison_sociale.strip().title()
tva = int(chiffre_affaires * taux_tva)

print(f"Contribuable {nif} — {raison_propre}")
print(f"CA : {chiffre_affaires:,} FCFA | TVA : {tva:,}".replace(",", " ") + " FCFA")

ca_saisi = int(input("Nouveau CA : "))
print(f"TVA : {int(ca_saisi * taux_tva):,}".replace(",", " ") + " FCFA")
