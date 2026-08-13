"""TP 01 — Premiers pas : la fiche d'un contribuable.

Complétez les passages marqués « À COMPLÉTER », puis exécutez :
    uv run python tp_premiers_pas.py
"""

# --- 1. Variables ----------------------------------------------------------
# Un contribuable est décrit par quelques informations élémentaires.

nif = "100004512"
raison_sociale = "  ets fatumata djaló  "   # saisie brute, mal formatée
chiffre_affaires = 45_000_000                  # en FCFA
taux_tva = 0.18

# --- 2. Nettoyage de la raison sociale -------------------------------------
# À COMPLÉTER : retirez les espaces superflus avec .strip()
# puis mettez chaque mot en majuscule initiale avec .title()
raison_propre = ...

# --- 3. Calcul de la TVA ----------------------------------------------------
# À COMPLÉTER : calculez la TVA collectée (chiffre d'affaires × taux)
tva = ...

# --- 4. Affichage formaté ---------------------------------------------------
# À COMPLÉTER : affichez avec une f-string, au format :
#   Contribuable 100004512 — Ets Fatumata Djaló
#   CA : 45 000 000 FCFA | TVA : 8 100 000 FCFA
# Astuce : le format {valeur:,} insère des séparateurs de milliers
# et .replace(",", " ") les transforme en espaces.
print(...)
print(...)

# --- 5. Pour aller plus loin ------------------------------------------------
# Demandez le CA à l'utilisateur avec input(), convertissez-le en int,
# et refaites le calcul.
