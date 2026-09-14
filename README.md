# Modèle de dépôt — TM IA 2026-2027

Un dossier de départ pour le travail de maturité : **un seul endroit** qui sert
à la fois de dépôt git, de coffre Obsidian et de source de documentation.

Tout est vide. C'est fait pour : tu le remplis avec ton travail à toi.

---

## Pourquoi un seul dossier pour trois outils

C'est l'idée centrale, et elle vaut la peine d'être comprise avant de
commencer.

| Le dossier est… | Ce que ça t'apporte |
|---|---|
| un dépôt **git** | tu ne perds rien, et tu obtiens un historique daté de ta progression |
| un coffre **Obsidian** | tu écris confortablement, tu lies tes notes, tu cherches |
| une source **Sphinx** | tes notes se compilent en site ou en PDF pour le rapport |

Aucun copier-coller entre outils : les notes prises en septembre deviennent
mécaniquement la matière du rapport de décembre. Les trois outils lisent les
mêmes fichiers Markdown.

---

## Installation

### 1. Récupérer le dossier

Sur GitHub, bouton **« Use this template »** → *Create a new repository*. Tu
obtiens ta propre copie, sans lien avec l'original. Puis :

```bash
git clone <l-url-de-ton-depot>
```

### 2. Installer les outils de documentation

`uv` remplace `python -m venv` + `pip`, en beaucoup plus rapide. S'il n'est pas
installé — **macOS et Linux** :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows** (PowerShell) :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Puis, dans le dossier du dépôt, la même commande partout :

```bash
uv venv && uv pip install -r requirements.txt
```

### 3. Ouvrir le coffre dans Obsidian

Obsidian → *Ouvrir un coffre* → *Ouvrir un dossier comme coffre* → choisir ce
dossier. La configuration est déjà là : les modèles sont branchés, les pièces
jointes vont au bon endroit.

---

## Usage quotidien

> **Windows :** dans toutes les commandes ci-dessous, remplace `.venv/bin/`
> par `.venv\Scripts\`. C'est la seule différence.

**Écrire** : dans Obsidian, en Markdown, normalement.

**Prévisualiser** le rendu, avec rechargement automatique à chaque
enregistrement :

```bash
.venv/bin/sphinx-autobuild . _build/html
```

Puis ouvrir <http://localhost:8000>.

**Compiler** une version figée :

```bash
.venv/bin/sphinx-build -b html . _build/html
```

À la première compilation, Sphinx affiche quatre avertissements
`toctree glob pattern didn't match any documents` : c'est normal, tes dossiers
`journal/`, `pv-entretiens/`, `concepts/` et `veille/` sont encore vides et la
table des matières ne trouve rien à lister. Chacun disparaît dès la première
note du dossier.

**Sauvegarder**, à la fin de chaque séance :

```bash
git add -A && git commit -m "décris ta séance" && git push
```

Un commit par séance produit un historique daté de la progression.

---

## Ce qu'il y a dans chaque dossier

| Dossier | À quoi il sert |
|---|---|
| `dossier-travail/` | le dossier de travail exigé par le séminaire (voir plus bas) |
| `dossier-travail/cahier-des-charges/` | la description du projet et le cahier des charges |
| `dossier-travail/journal/` | une entrée par séance de travail : réflexions et idées |
| `dossier-travail/pv-entretiens/` | un compte rendu par entretien avec l'enseignant |
| `dossier-travail/gestion-projet/` | planning, jalons et temps investi |
| `dossier-travail/concepts/` | une fiche par notion comprise, écrite avec tes mots |
| `dossier-travail/veille/` | l'actualité IA suivie et ses références |
| `dossier-travail/ressources/` | documents de référence, notes de séance |
| `dossier-travail/modèles/` | les gabarits de journal, de fiche et de PV |
| `dossier-travail/pièces-jointes/` | où Obsidian range les images collées |
| `code/experiences/` | tes scripts et essais |
| `_static/` | les images utilisées dans la documentation compilée |

Les fichiers `index.md` de `journal/`, `pv-entretiens/`, `concepts/` et
`veille/` construisent automatiquement la table des matières : tu n'as jamais
à les modifier quand tu ajoutes une note.

---

## Les trois modèles

Dans `dossier-travail/modèles/` : entrée de journal, fiche concept, PV
d'entretien. Dans Obsidian : créer une note vide au bon endroit, puis `Cmd+P`
(Windows : `Ctrl+P`) → *Insérer un modèle*.

Les fichiers de `modèles/` sont les gabarits : ils se dupliquent, ils ne se
modifient pas. Leurs rubriques sont un point de départ — à adapter à sa
manière de travailler.

---

## Ce que demande le séminaire

Trois exigences qui expliquent la structure de ce dossier :

- **Un dossier de travail** nommé `dossier-travail/`, à la racine du dépôt,
  synchronisé avec le coffre Obsidian et commité régulièrement. Il doit
  contenir six éléments : la description du projet et le cahier des charges,
  les réflexions et idées (notes journalières), les PV des entretiens avec
  l'enseignant, la gestion du projet, les notes de lecture et références, et
  le suivi des interactions avec l'IA. Le détail est dans le manuel du
  séminaire, section *Obsidian → 4. Dossier de travail*.
- **L'usage des LLMs est encouragé**, et l'évaluation porte sur sa
  *pertinence* ainsi que sur la *compréhension du code produit*. D'où la
  rubrique « usage de l'IA » dans le gabarit de journal.
- **MyST** est l'outil de rédaction attendu pour la partie écrite. D'où la
  configuration Sphinx fournie.
