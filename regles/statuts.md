# Statuts

Les statuts sont des effets temporaires appliqués par les cartes.

## Dans le jeu

Définis dans `src/config/statuses.json` :

<!-- jeu:debut statuts -->

_Généré depuis `src/config/statuses.json` du jeu : ne pas modifier à la main._

| Statut | Texte du jeu |
| --- | --- |
| **Blackout** | Le vaisseau ne peut plus rien détecter, il est impossible pour les joueurs d’agir. |
| **Anticipation** | Les joueurs vont pouvoir éviter le prochain danger sans subir de pertes. |
| **Affaibli** | Une ou plusieurs statistiques des joueurs sont diminuées |
| **Recherché** | Vous êtes recherchés par les autorités |

<!-- jeu:fin -->

## En détail

| Statut | Effet |
| --- | --- |
| **Blackout** | Le vaisseau ne détecte plus rien : les cartes s'affichent dans leur version « blackout », et les joueurs ne peuvent plus agir normalement. Déclenché quand on éteint les radars (pulsar, supernova, amas stellaire) ou par un court-circuit. |
| **Anticipation** | Les joueurs évitent le prochain danger sans subir de pertes. Donné par un message d'avertissement. |
| **Affaibli** | Une ou plusieurs statistiques des joueurs sont diminuées. |
| **Recherché** | L'équipage est recherché par les autorités. |

## Retirés ou jamais ajoutés

- **Entraîné** (une stat augmente jusqu'à la prochaine planète) : retiré du jeu le 20/02/2023, mais son icône existe encore. La carte « tutoriel » augmente désormais la stat directement.
- **Proximité planétaire** : cité dans une idée de carte positive (entrée dans un système solaire proche de la Terre), sans effet défini.

## Ancienne définition du Blackout

Les notes Notion décrivaient le Blackout comme « pire issue possible sur les x prochaines cartes (2 ou 3) ». C'est une autre règle que celle du jeu, à garder seulement si vous voulez la remettre.
