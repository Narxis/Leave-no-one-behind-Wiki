# Rôles des joueurs

> **Proposition, à valider par le MJ.** Les rôles sont dans le jeu, avec des effets par défaut. Tout se change sans toucher au code dans `src/config/roles.json` du jeu : nom, stat, nombre de dés en plus, texte de l'effet, icône, et `"unique"` (un seul joueur par rôle ou non).

Chaque joueur peut recevoir un rôle dans l'équipage. Un rôle est un **bonus**, pas une exclusivité : tout le monde peut toujours piloter, soigner ou se battre, mais celui qui a le rôle le fait mieux. Chaque stat garde donc son intérêt pour tous.

## Les rôles

| Rôle | Stat | Effet |
| --- | --- | --- |
| **Capitaine** | aucune | Une fois par planète, peut faire relancer un jet raté (le sien ou celui d'un équipier). Le MJ relance avec le menu MJ (« Jet pour un joueur ») et garde le nouveau résultat. |
| **Pilote** | Pilotage | +1 dé sur ses jets de Pilotage |
| **Armurier** | Combat | +1 dé sur ses jets de Combat |
| **Ingénieur** | Ingénierie | +1 dé sur ses jets d'Ingénierie |
| **Éclaireur** | Reconnaissance | +1 dé sur ses jets de Reconnaissance |
| **Infirmier** | Survie | +1 dé sur ses jets de Survie, y compris pour soigner (voir [Points de vie](points-de-vie.md)) |

## Le dé en plus

C'est la même idée que les bonus de race à la [création du personnage](creation-personnage.md) : on lance **un dé de plus et on garde le meilleur**.

Un jet normal en partie lance un dé de 1 à 100 ; le résultat vaut `dé × stat / 100 + (moral − 50) / 4`, réussi à partir de 50. Avec son rôle, le joueur lance deux dés de 1 à 100 et garde le plus haut. Le jeu le fait tout seul, pour les jets lancés depuis l'app des joueurs comme pour ceux du menu MJ ; le menu MJ et l'app affichent les deux dés et celui gardé.

Le bonus compte aussi pour les jets de module (avec le vaisseau), puisque c'est un jet de la même stat.

## Attribution

- Le MJ choisit le rôle de chaque joueur sur la page **Fiche Personnages**, avant de commencer la partie.
- **Un seul joueur par rôle** : donner un rôle déjà pris le retire à l'autre joueur.
- Un joueur peut n'avoir aucun rôle (plus de 6 joueurs, ou par choix).
- Le logo du rôle s'affiche devant le nom du joueur sur l'écran de jeu (cartes et planètes) ; le nom du rôle apparaît dans l'app des joueurs, sur sa fiche et dans la liste de l'équipage.
