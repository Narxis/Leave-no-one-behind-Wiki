# Création de personnage

## Nom et race

Chaque joueur choisit une [race](../lore/races/README.md) et un nom : une des onze races de base, ou une race custom que le MJ autorise dans le lobby. Le MJ peut ensuite appeler les joueurs par leur nom de personnage pour renforcer l'immersion. Le jeu crée les personnages un par un ; l'ordre n'a pas d'importance.

Lire la page de sa race est recommandé : elle a une influence dans certaines cartes, et elle aide à jouer le personnage. Par exemple, une Nek-Eau et un Nek-Feu dans le même équipage peuvent se disputer pendant les phases de choix. On peut aussi faire des parties à thème où tout le monde joue la même race.

## Les statistiques

Six statistiques : **Combat**, **Pilotage**, **Ingénierie**, **Survie**, **Reconnaissance** et **Moral**.

Pour chacune, le joueur lance des dés à 50 faces selon le modificateur de sa race, puis ajoute 50 :

| Modificateur | Dés lancés | Résultat |
| --- | --- | --- |
| 0 | 1 d50 | le dé + 50 |
| +1 | 2 d50 | le meilleur + 50 |
| −1 | 2 d50 | le pire + 50 |
| +2 | 3 d50 | le meilleur + 50 |
| −2 | 3 d50 | le pire + 50 |

## Modificateurs par race

Ces valeurs sont celles du jeu (`src/config/raceStats.json`, mises à jour le 21/02/2023). Le Moral est à 0 pour toutes les races.

| Race | Combat | Pilotage | Ingénierie | Survie | Reconnaissance |
| --- | --- | --- | --- | --- | --- |
| Fnek | +2 | +2 | +2 | −1 | −2 |
| Omphor | −2 | +2 | +2 | +2 | −1 |
| Sylv | −1 | 0 | +2 | +1 | +1 |
| Ygrl | 0 | +2 | −2 | +1 | +2 |
| Shrymp | −1 | +2 | +2 | −1 | +1 |
| Aku | +2 | −2 | +1 | 0 | +2 |
| Yorc | +2 | 0 | 0 | +2 | −1 |
| Nek-Eau | 0 | +2 | +1 | −2 | +2 |
| Nek-Feu | +1 | +2 | −2 | +2 | 0 |
| Nek-Terre | −1 | +1 | 0 | +1 | +2 |
| Nek-Air | −1 | +2 | +2 | −2 | +2 |

Chaque race totalise +3. L'ancien tableau du Notion (total +1) n'est plus à jour ; il reste dans les [archives](../archives-notion/).

## Objets de départ

Chaque race commence avec ses objets : voir [Objets](../lore/objets.md).
