"""Générateur des jeux de données de la formation.

Produit des fichiers CSV reproduisant les données d'une administration
fiscale : contribuables (NIF), déclarations TVA, paiements, référentiel
des régions et préfectures de Guinée.

Les données sont FICTIVES mais réalistes, avec les imperfections des
fichiers administratifs : libellés incohérents, formats de date multiples,
doublons, valeurs manquantes ou aberrantes. C'est voulu : les modules 06
et 09 apprennent justement à les traiter.

Usage :
    python generate_data.py --auto                  # taille selon la RAM
    python generate_data.py --jeu tous --lignes 50000
    python generate_data.py --jeu contribuables --lignes 10000

⚠️ Régénérez toujours avec --jeu tous : les déclarations et paiements
   référencent les NIF des contribuables.
"""

from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path

# Graine fixe : tout le monde obtient les mêmes données.
random.seed(2026)

SORTIE = Path(__file__).parent / "sortie"

# ---------------------------------------------------------------------------
# Référentiels (fictifs mais géographiquement réalistes)
# ---------------------------------------------------------------------------

REGIONS = {
    "BIS": ("Bissau", ["Bissau"]),
    "BAF": ("Bafatá", ["Bafatá", "Bambadinca", "Contuboel", "Galomaro", "Xitole"]),
    "BIO": ("Biombo", ["Quinhámel", "Prábis", "Safim"]),
    "BOL": ("Bolama-Bijagós", ["Bolama", "Bubaque", "Caravela"]),
    "CAC": ("Cacheu", ["Cacheu", "Bula", "Canchungo", "Caió", "São Domingos"]),
    "GAB": ("Gabú", ["Gabú", "Boé", "Pirada", "Pitche", "Sonaco"]),
    "OIO": ("Oio", ["Farim", "Bissorã", "Mansabá", "Mansôa", "Nhacra"]),
    "QUI": ("Quinara", ["Buba", "Empada", "Fulacunda", "Tite"]),
    "TOM": ("Tombali", ["Catió", "Bedanda", "Cacine", "Quebo"]),
}

PRENOMS = [
    "Mamadú", "Fatumata", "Braima", "Aissatu", "Umaro", "Mariama",
    "Domingos", "Quinta", "Seco", "Aminata", "Carlos", "Iança",
    "Bacar", "Djenabu", "Abdulai", "Salimatu", "Fodé", "Binta", "João", "N'Fanda",
]

NOMS = [
    "Djaló", "Baldé", "Embaló", "Mané", "Sané", "Vieira", "Gomes", "Sanhá",
    "Có", "Camará", "Cassamá", "Indjai", "Seidi", "Turé", "Nanque",
    "Correia", "Pereira", "da Costa", "Sambú", "Dabó",
]

SECTEURS = [
    "Commerce général", "BTP", "Transport", "Restauration", "Import-export",
    "Télécommunications", "Agriculture", "Services", "Industrie", "Mines",
]

# Variantes volontairement incohérentes d'un même secteur (à normaliser en TP)
VARIANTES_SECTEUR = {
    "Commerce général": ["Commerce général", "COMMERCE GENERAL", "commerce gal", "Commerce Général "],
    "BTP": ["BTP", "Btp", "Bâtiment et TP", "BATIMENT"],
    "Transport": ["Transport", "TRANSPORT ", "transports"],
}

REGIMES = ["Réel normal", "Réel simplifié", "Forfait"]


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def nif(i: int) -> str:
    """Un NIF fictif à 9 chiffres, stable pour un même index."""
    return f"{100000000 + i}"


def date_sale(annee: int) -> str:
    """Une date dans un format volontairement variable (fichiers réels...)."""
    j, m = random.randint(1, 28), random.randint(1, 12)
    fmt = random.random()
    if fmt < 0.60:
        return f"{annee}-{m:02d}-{j:02d}"          # ISO
    if fmt < 0.85:
        return f"{j:02d}/{m:02d}/{annee}"          # français
    if fmt < 0.95:
        return f"{j}-{m}-{annee}"                  # sans zéros
    return f"{annee}{m:02d}{j:02d}"                # compact


def taille_auto() -> int:
    """Dimensionne le jeu selon la mémoire disponible."""
    try:
        with open("/proc/meminfo") as f:
            for ligne in f:
                if ligne.startswith("MemTotal"):
                    go = int(ligne.split()[1]) / 1024 / 1024
                    break
            else:
                go = 4
    except OSError:
        go = 4
    if go >= 16:
        return 100_000
    if go >= 8:
        return 50_000
    return 20_000


# ---------------------------------------------------------------------------
# Générateurs
# ---------------------------------------------------------------------------

def gen_referentiel() -> None:
    """regions.csv : référentiel propre (le seul fichier sans défaut !)."""
    chemin = SORTIE / "regions.csv"
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["code_region", "region", "secteur_admin"])
        for code, (nom, prefs) in REGIONS.items():
            for p in prefs:
                w.writerow([code, nom, p])
    print(f"  {chemin.name} : référentiel des secteurs")


def gen_contribuables(n: int) -> list[str]:
    """contribuables.csv : l'annuaire, avec doublons et champs sales."""
    chemin = SORTIE / "contribuables.csv"
    nifs: list[str] = []
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nif", "raison_sociale", "secteur", "regime",
                    "code_region", "date_immatriculation", "telephone"])
        for i in range(n):
            numero = nif(i)
            nifs.append(numero)
            prenom, nom = random.choice(PRENOMS), random.choice(NOMS)
            rs = f"Ets {prenom} {nom}" if random.random() < 0.7 else f"{nom} & Frères SARL"
            secteur = random.choice(SECTEURS)
            # ~15 % de libellés incohérents
            if secteur in VARIANTES_SECTEUR and random.random() < 0.5:
                secteur = random.choice(VARIANTES_SECTEUR[secteur])
            regime = random.choice(REGIMES)
            code_region = random.choice(list(REGIONS))
            date_imm = date_sale(random.randint(2010, 2025))
            # ~5 % de téléphones manquants
            tel = "" if random.random() < 0.05 else f"9{random.choice([5, 6, 7])}{random.randint(1000000, 9999999)}"
            w.writerow([numero, rs, secteur, regime, code_region, date_imm, tel])
            # ~2 % de doublons purs (double saisie)
            if random.random() < 0.02:
                w.writerow([numero, rs, secteur, regime, code_region, date_imm, tel])
    print(f"  {chemin.name} : {n} contribuables (+ doublons)")
    return nifs


def gen_declarations(nifs: list[str], n: int) -> None:
    """declarations.csv : déclarations TVA mensuelles, avec aberrations."""
    chemin = SORTIE / "declarations.csv"
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_declaration", "nif", "periode", "chiffre_affaires",
                    "tva_collectee", "tva_deductible", "date_depot"])
        for i in range(n):
            numero = random.choice(nifs)
            annee = random.randint(2023, 2025)
            mois = random.randint(1, 12)
            ca = random.randint(500_000, 500_000_000)
            tva_c = round(ca * 0.18)
            tva_d = round(tva_c * random.uniform(0.2, 0.9))
            # ~1 % de valeurs aberrantes (CA négatif ou nul)
            if random.random() < 0.01:
                ca = random.choice([0, -ca])
            # ~3 % de TVA collectée manquante
            tva_c_txt = "" if random.random() < 0.03 else str(tva_c)
            w.writerow([f"DEC-{annee}-{i:07d}", numero, f"{annee}-{mois:02d}",
                        ca, tva_c_txt, tva_d, date_sale(annee)])
    print(f"  {chemin.name} : {n} déclarations TVA")


def gen_paiements(nifs: list[str], n: int) -> None:
    """paiements.csv : paiements, dont certains orphelins (NIF inconnu)."""
    chemin = SORTIE / "paiements.csv"
    modes = ["Espèces", "Chèque", "Virement", "Mobile money"]
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_paiement", "nif", "montant", "mode", "date_paiement"])
        for i in range(n):
            # ~2 % de NIF inconnus du fichier contribuables (orphelins)
            if random.random() < 0.02:
                numero = nif(10_000_000 + i)
            else:
                numero = random.choice(nifs)
            montant = random.randint(50_000, 200_000_000)
            w.writerow([f"PAY-{i:08d}", numero, montant,
                        random.choice(modes), date_sale(random.randint(2023, 2025))])
    print(f"  {chemin.name} : {n} paiements")


# ---------------------------------------------------------------------------
# Point d'entrée
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Génère les jeux de données de la formation.")
    parser.add_argument("--jeu", default="tous",
                        choices=["tous", "contribuables", "declarations", "paiements", "referentiel"])
    parser.add_argument("--lignes", type=int, default=None,
                        help="Nombre de contribuables (les autres jeux sont proportionnels)")
    parser.add_argument("--auto", action="store_true",
                        help="Dimensionner selon la mémoire du poste")
    args = parser.parse_args()

    n = args.lignes or (taille_auto() if args.auto else 20_000)
    SORTIE.mkdir(exist_ok=True)

    print(f"Génération dans {SORTIE}/ ({n} contribuables) :")
    if args.jeu != "tous":
        print("⚠️  Génération partielle : la cohérence entre fichiers n'est pas garantie.")

    if args.jeu in ("tous", "referentiel"):
        gen_referentiel()
    nifs = gen_contribuables(n) if args.jeu in ("tous", "contribuables") else [nif(i) for i in range(n)]
    if args.jeu in ("tous", "declarations"):
        gen_declarations(nifs, n * 3)
    if args.jeu in ("tous", "paiements"):
        gen_paiements(nifs, n * 2)

    print("Terminé.")


if __name__ == "__main__":
    main()
