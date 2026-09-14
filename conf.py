# Configuration Sphinx — Travail de maturité
# Documentation : https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# À PERSONNALISER : les quatre lignes ci-dessous, et rien d'autre au départ.

project = "TM — titre de ton travail"
author = "Prénom Nom"
copyright = "2026-2027, Prénom Nom"
release = "0.1"

language = "fr"

# MyST permet à Sphinx de lire des fichiers Markdown (.md).
# Sans lui, Sphinx n'accepte que le reStructuredText (.rst) — alors qu'Obsidian
# n'écrit que du Markdown. C'est cette extension qui rend le même dossier
# utilisable par les deux outils.
extensions = [
    "myst_parser",
]

myst_enable_extensions = [
    "colon_fence",      # blocs ::: pour les admonitions (note, avertissement)
    "deflist",          # listes de définitions
    "linkify",          # transforme les URL brutes en liens cliquables
    "tasklist",         # cases à cocher - [ ] / - [x]
]

# Attention : Obsidian écrit les liens internes sous la forme [[note]].
# Sphinx ne les comprend pas. Dans les fichiers destinés à être compilés,
# utiliser des liens Markdown normaux : [texte](chemin/fichier.md)

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

master_doc = "index"

# Fichiers et dossiers que Sphinx ignore à la compilation.
exclude_patterns = [
    "_build",
    ".obsidian",
    "dossier-travail/modèles",
    "dossier-travail/pièces-jointes",
    "README.md",
    "Thumbs.db",
    ".DS_Store",
    "venv",
    ".venv",
]

html_theme = "furo"
html_static_path = ["_static"]
html_title = "TM — titre de ton travail"

# Numérote automatiquement figures et tableaux, et permet d'y renvoyer depuis
# le texte. Utile pour le rapport final.
numfig = True
