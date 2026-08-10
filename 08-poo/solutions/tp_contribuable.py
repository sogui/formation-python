"""TP 08 — Solution."""

from dataclasses import dataclass, field


@dataclass
class Declaration:
    periode: str
    chiffre_affaires: int
    tva_collectee: int
    tva_deductible: int

    @property
    def tva_nette(self) -> int:
        return max(self.tva_collectee - self.tva_deductible, 0)


@dataclass
class Contribuable:
    nif: str
    raison_sociale: str
    regime: str
    declarations: list[Declaration] = field(default_factory=list)

    def ajouter(self, d: Declaration) -> None:
        self.declarations.append(d)

    @property
    def ca_total(self) -> int:
        return sum(d.chiffre_affaires for d in self.declarations)

    def tva_due_totale(self) -> int:
        return sum(d.tva_nette for d in self.declarations)

    def declarations_manquantes(self, annee: int) -> list[str]:
        deposees = {d.periode for d in self.declarations}
        return [f"{annee}-{m:02d}" for m in range(1, 13)
                if f"{annee}-{m:02d}" not in deposees]


c = Contribuable("100000001", "Ets Diallo", "Réel normal")
c.ajouter(Declaration("2025-01", 40_000_000, 7_200_000, 3_000_000))
c.ajouter(Declaration("2025-02", 55_000_000, 9_900_000, 12_000_000))

assert c.ca_total == 95_000_000
assert c.declarations[1].tva_nette == 0
assert c.tva_due_totale() == 4_200_000
print(c)
print(f"CA total : {c.ca_total:,} | TVA due : {c.tva_due_totale():,}")
print("Manquantes 2025 :", c.declarations_manquantes(2025)[:3], "...")
