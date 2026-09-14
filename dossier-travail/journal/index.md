# Journal de bord

Une entrée par séance de travail. Le journal fait partie des critères
d'évaluation du séminaire.

## Comment ajouter une entrée

Dans Obsidian : créer la note dans `journal/` au format
`AAAA-MM-JJ-titre-court.md`, puis `Cmd+P` (Windows : `Ctrl+P`) →
*Insérer un modèle* → `journal — modèle`.

La liste ci-dessous se remplit toute seule : le `glob` attrape tout fichier
commençant par `20`, et `reversed` affiche la plus récente en premier. Cette
page n'a pas besoin d'être modifiée.

Chaque entrée porte une propriété en en-tête : `temps` (en minutes). Elle
permet de totaliser le temps passé sur les séances.

```{toctree}
:maxdepth: 1
:reversed:
:glob:

20*
```
