# Cartes et deck

## Les types de cartes

| Type | Rôle | Dans le jeu |
| --- | --- | --- |
| Départ | La séquence de lancement depuis la Terre | 1 |
| Positive | Réparations, moral, objets, alliés | 6 |
| Négative | Dégâts, intrus, perte de moral | 19 |
| Neutre | Rencontres dont l'issue dépend des choix | 11 |
| Lieu | Une étape à plusieurs embranchements (voir [Lieux](../lore/lieux.md)) | 3 lieux |
| Planète | Une planète où l'on peut se poser | dans `jsonFiles/plaCardList.json` |

Chiffres relevés dans `src/config/baseCards.json` en octobre 2026. Les brouillons PDF des [archives](../archives-notion/) parlaient de 39 négatives et 25 positives prévues.

Beaucoup de cartes ont un choix réservé à une race présente dans l'équipage (Nek-Air pour la douane, Fnek pour les odeurs, Omphor pour le pot de cornichons, Sylv pour la bombe, Ygrl pour les Shrymps Hackers, Aku pour la direction-horaire), et une version alternative en cas de Blackout.

## Composer le deck

Réglages dans `src/config/baseConf.json` :

- `planetCount` : nombre de planètes (3 par défaut, prévu pour 3 joueurs et 1 h 30 à 2 h de jeu) ;
- **mode Fair** : avant chaque planète, une étape de `placeByStep` lieu, `positiveByStep` positives, `negativeByStep` négatives et `neutralByStep` neutres, mélangées (1, 2, 2 et 2 par défaut) ;
- **mode Chaos** : `cardByStepsChaos` cartes tirées au hasard avant chaque planète (6 par défaut), jamais plus de 3 négatives d'affilée.

Les planètes sont classées par qualité : le premier tiers des étapes pioche dans les planètes les moins bonnes, le dernier tiers dans les meilleures.

L'ancien algorithme du Notion (parties de 50, 80 ou 120 cartes avec 5 planètes) est dans les [archives](../archives-notion/deck.md).

## Les planètes

Une planète a huit caractéristiques, chacune avec un coût en points de détection et une valeur :

`oxy` oxygène · `grv` gravité · `wtr` eau · `fau` faune · `flo` flore · `civ` civilisation · `cli` climat · `res` ressources

## Écrire une carte

Les cartes vivent dans `src/config/baseCards.json` du dépôt du jeu, avec un modèle dans `src/config/readme.md`. Une carte a une description, des choix, ce qui est révélé aux joueurs (`reveal`) et au MJ seul (`mjreveal`), et peut utiliser des variables comme `[le_module_0]`, `[un_race_1]` ou `[de_stats_0]`.

### Écrire une carte lieu

D'après `src/config/readme.md` :

1. Imaginer le lieu.
2. Le décrire : décor et personnages présents.
3. Trouver les actions que les joueurs auront naturellement envie de faire (parler, visiter, inspecter) et en faire 3 choix.
4. Inventer une histoire pour chacun.
5. Faire progresser les joueurs étape par étape.
6. Donner une récompense liée à l'histoire.

Les cartes lieu se construisent dans l'éditeur visuel du jeu (`/buildCard`).
