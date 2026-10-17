# Le PLUGS

Le vaisseau des joueurs est un **PLUGS** (*Pretty Looking and Ultimately Glorious Ships*), fabriqué par l'[OLI](organisations.md#loli) pour sauver un maximum d'êtres humains de la guerre entre l'USA et le JAPAN. Les joueurs lui donnent un nom en début de partie.

## Description

- Il stocke plus d'humains dans ses cryopods que le modèle concurrent « Geisha », et les met dans un état qui les rend plus faciles à transporter.
- Il a un **bouclier** qui lui permet de résister à une attaque, mais **aucune arme** : au cas où les humains se réveilleraient et voudraient prendre le contrôle du vaisseau (ils seraient alors contraints de faire grève).
- Il atteint « à peu près un peu moins que la vitesse de la lumière », mais moins, et uniquement le mercredi en descente (pour les années bissextiles, se référer au manuel).
- Il peut atterrir sur n'importe quelle surface grâce à des bras mécaniques qui pénètrent dans le sol (sauf sur les matelas gonflables et la lave en fusion, sauf si la lave est à plus de 21 °C).
- L'intérieur est organisé pour un confort optimal : salle de cinéma avec une bibliothèque de plus de 150 000 films de pétanque, et une machine à glace.
- Son **autopilote** est en retard sur son temps mais capable d'anticiper des évènements passés. Il est recommandé de ne pas l'utiliser pour survivre avec plus de chance. C'est souvent lui qui mène l'équipage vers les [lieux](lieux.md).

## La séquence de lancement

Au début de la partie, l'autopilote affiche :

```
Mise à jour de l'autopilote en v7.27 [rev B] ....
Vérification de l'état des cryopods ....
1000 humains détectés, démarrage des cryopods ....
Calcul de l'itinéraire en cours ....
Quantité carburant ~ 250mg ....
[n] planètes trouvées sur l'itinéraire ....
Initialisation de la phase de lancement ....
Êtes-vous prêt à partir un jour sans retour ?   [Oui] / [~~Non~~]
```

## Les modules

L'état du vaisseau est suivi module par module (de 0 à 100 %). Ce sont les noms utilisés dans le jeu (`src/config/lang.json`) :

| Clé | Nom en jeu | Rôle |
| --- | --- | --- |
| `cryopods` | Cryopods | Les humains à bord (leur nombre compte dans le score) |
| `motors` | Moteurs | Déplacement |
| `shield` | Bouclier | Résiste à une attaque |
| `scanner` | Scanners | Analyse des planètes |
| `proximity` | Module de détection | Radars et capteurs |
| `energy` | Centrale électrique | Alimentation |
| `oxygen` | Module d'oxygène | Air respirable |
| `gravity` | Générateur de gravité artificielle | Gravité à bord |
| `landing` | Module d'atterrissage | Atterrissage sur la planète finale |
| `construction` | Module de construction | Imprimantes pour bâtir la colonie |
| `dbscience` | Base de données scientifique | Savoir à transmettre |
| `dbhistory` | Base de données historique | Mémoire de l'humanité |

Le carburant correspond au nombre de cartes qu'il reste à jouer. Voir aussi [Score](../regles/score.md).
