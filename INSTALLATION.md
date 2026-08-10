# Installation de l'environnement

Comptez vingt à trente minutes. Tout est gratuit et fonctionne sous Windows,
macOS et Linux.

---

## 1. Visual Studio Code

Téléchargez et installez VS Code : https://code.visualstudio.com/

Extensions à installer (icône « Extensions » dans la barre latérale) :

- **Python** (Microsoft)
- **Pylance** (Microsoft)
- **Jupyter** (Microsoft)

## 2. Git

- Windows : https://git-scm.com/download/win — installez **Git Bash** avec.
- macOS : `xcode-select --install`
- Linux : `sudo apt install git`

Vérifiez :

```bash
git --version
```

## 3. uv — gestionnaire de Python

`uv` installe Python lui-même et les bibliothèques, aux versions exactes du
projet. Personne n'a besoin d'installer Python à la main.

- Windows (PowerShell) :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- macOS / Linux :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Fermez puis rouvrez le terminal, et vérifiez :

```bash
uv --version
```

## 4. Récupérer le dépôt et synchroniser

```bash
git clone <adresse-du-depot> formation-python
cd formation-python
uv sync
```

`uv sync` lit `pyproject.toml` et `uv.lock`, télécharge Python 3.12 si besoin,
et crée l'environnement `.venv/`.

## 5. Brancher VS Code sur l'environnement

1. Ouvrez le dossier `formation-python` dans VS Code (`Fichier > Ouvrir un dossier`).
2. Ouvrez un fichier `.py`.
3. En bas à droite, cliquez sur la version de Python et choisissez
   **`.venv`** (`./.venv/bin/python` ou `.venv\Scripts\python.exe`).

## 6. Vérification finale

```bash
uv run python -c "import pandas; print('Environnement OK, pandas', pandas.__version__)"
```

Si ce message s'affiche, vous êtes prêt.

---

## Incidents fréquents

| Symptôme | Cause probable | Remède |
| -------- | -------------- | ------ |
| `uv : commande introuvable` | Terminal non rouvert après installation | Fermer/rouvrir le terminal |
| VS Code ne trouve pas pandas | Mauvais interpréteur sélectionné | Refaire l'étape 5 |
| Erreur de fins de ligne dans un `.sh` | Script lancé depuis PowerShell | Utiliser Git Bash |
| `Permission denied` sous Windows | Antivirus ou dossier synchronisé (OneDrive) | Cloner dans `C:\dev\` |
