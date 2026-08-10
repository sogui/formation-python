# Aide-mémoire Python de la formation

## Réflexes de survie

```python
type(x)          # quel est ce type ?
len(x)           # combien d'éléments ?
dir(x)           # que sait faire cet objet ?
help(x.methode)  # comment s'en servir ?
print(f"{x=}")   # afficher nom ET valeur
```

## Pièges vus en formation

**L'indentation EST la syntaxe.** Quatre espaces, jamais de tabulation mélangée.

**`==` compare, `=` affecte.** `if x = 3:` est une erreur de syntaxe — tant mieux.

**Copier une liste :** `b = a` ne copie pas, `b = a.copy()` oui.

**Diviser :** `/` donne toujours un `float` ; `//` donne la division entière.

**Un CSV s'ouvre toujours** avec `encoding="utf-8"` et `newline=""` en écriture.

**`dict[cle]`** plante si la clé manque ; **`dict.get(cle, defaut)`** jamais.

**Argument par défaut mutable :** jamais `def f(x=[])` — utilisez `None`
ou `field(default_factory=list)` dans une dataclass.

**pandas :** filtrer c'est `df[df["col"] > 0]` ; et `dtype={"nif": str}` au
chargement, sinon les NIF perdent leurs zéros de tête.

## Vocabulaire français ↔ anglais

| Français | Anglais (dans le code/les docs) |
| -------- | ------------------------------- |
| chaîne de caractères | string, `str` |
| dictionnaire | dictionary, `dict` |
| ensemble | set |
| boucle | loop |
| exception | exception |
| trame de données | DataFrame |
