# Statuts

Les statuts sont des effets temporaires appliqués par les cartes.

## Dans le jeu

Définis dans `src/config/statuses.json` :

| Statut | Effet |
| --- | --- |
| **Blackout** | Le vaisseau ne détecte plus rien : les cartes s'affichent dans leur version « blackout », et les joueurs ne peuvent plus agir normalement. Déclenché quand on éteint les radars (pulsar, supernova, amas stellaire) ou par un court-circuit. |
| **Anticipation** | Les joueurs évitent le prochain danger sans subir de pertes. Donné par un message d'avertissement. |
| **Affaibli** | Une ou plusieurs statistiques des joueurs sont diminuées. |
| **Recherché** | L'équipage est recherché par les autorités. |
| **Diverti** | Les pertes de moral sont divisées par deux, arrondi vers le bas (une perte de 10 devient 5, une perte de 1 est annulée). Les gains de moral et les dégâts de combat ne changent pas. Donné pour 3 cartes par le vaisseau Sylv (choix « Entrer en contact »), en plus du gain de moral. |

Un statut dure un nombre de cartes : sa durée baisse de 1 à chaque nouvelle carte. Il touche toute l'équipe, ou un seul joueur si le MJ le choisit (seuls les statuts de toute l'équipe changent la version des cartes, comme le Blackout).

## Statuts créés par le MJ

Le MJ peut créer un statut à la volée depuis son menu : un nom, une description courte (affichée au survol partout où le statut apparaît : menu MJ, écran de jeu, app des joueurs), une durée en cartes et la cible (toute l'équipe ou un joueur). Ces statuts n'ont pas d'effet automatique : le MJ applique leurs conséquences. Ils disparaissent à la partie suivante.

## Après une planète

L'option de partie « Retirer les statuts après une planète » (active par défaut) remet les statuts à zéro quand l'équipage repart d'une planète. Un statut créé par le MJ a sa propre case « Retiré après une planète » (cochée comme l'option au moment de le créer), qui l'emporte sur l'option.

## Retirés ou jamais ajoutés

- **Entraîné** (une stat augmente jusqu'à la prochaine planète) : retiré du jeu le 20/02/2023, mais son icône existe encore. La carte « tutoriel » augmente désormais la stat directement.
- **Proximité planétaire** : cité dans une idée de carte positive (entrée dans un système solaire proche de la Terre), sans effet défini.

## Ancienne définition du Blackout

Les notes Notion décrivaient le Blackout comme « pire issue possible sur les x prochaines cartes (2 ou 3) ». C'est une autre règle que celle du jeu, à garder seulement si vous voulez la remettre.
