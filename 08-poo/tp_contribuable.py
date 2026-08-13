"""TP 08 — POO : modéliser un contribuable et ses déclarations."""

from dataclasses import dataclass, field


@dataclass
class Declaration:
    periode: str            # "2025-03"
    chiffre_affaires: int
    tva_collectee: int
    tva_deductible: int

    @property
    def tva_nette(self) -> int:
        """TVA à payer : collectée moins déductible, jamais négative."""
        # À COMPLÉTER (une ligne, avec max())
        ...


@dataclass
class Contribuable:
    nif: str
    raison_sociale: str
    regime: str
    declarations: list[Declaration] = field(default_factory=list)

    def ajouter(self, d: Declaration) -> None:
        """Ajoute une déclaration."""
        # À COMPLÉTER
        ...

    @property
    def ca_total(self) -> int:
        """Somme des chiffres d'affaires déclarés."""
        # À COMPLÉTER (sum + expression génératrice)
        ...

    def tva_due_totale(self) -> int:
        """Somme des TVA nettes de toutes les déclarations."""
        # À COMPLÉTER
        ...


# --- Mise à l'épreuve --------------------------------------------------------
c = Contribuable("100000001", "Ets Djaló", "Réel normal")
c.ajouter(Declaration("2025-01", 40_000_000, 7_200_000, 3_000_000))
c.ajouter(Declaration("2025-02", 55_000_000, 9_900_000, 12_000_000))  # crédit !

assert c.ca_total == 95_000_000
assert c.declarations[1].tva_nette == 0        # jamais négative
assert c.tva_due_totale() == 4_200_000
print(c)
print(f"CA total : {c.ca_total:,} | TVA due : {c.tva_due_totale():,}")

# --- Pour aller plus loin ----------------------------------------------------
# Ajoutez une méthode declarations_manquantes(annee) qui renvoie la liste
# des périodes "AAAA-MM" de l'année sans déclaration déposée.
