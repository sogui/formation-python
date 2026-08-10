"""TP 02 — Solution."""

def regime(ca: int) -> str:
    if ca < 100_000_000:
        return "Forfait"
    elif ca < 500_000_000:
        return "Réel simplifié"
    else:
        return "Réel normal"


print(regime(50_000_000) == "Forfait")
print(regime(200_000_000) == "Réel simplifié")
print(regime(800_000_000) == "Réel normal")

chiffres_affaires = [45_000_000, 620_000_000, 150_000_000, 0,
                     98_000_000, 510_000_000, 320_000_000, -5_000_000]

nb_invalides = 0
for ca in chiffres_affaires:
    if ca <= 0:
        nb_invalides += 1
print(f"CA invalides : {nb_invalides}")

regimes = [regime(ca) for ca in chiffres_affaires if ca > 0]
print(regimes)

ca, annees = 10_000_000, 0
while ca < 500_000_000:
    ca *= 2
    annees += 1
print(f"Réel normal atteint en {annees} ans")
