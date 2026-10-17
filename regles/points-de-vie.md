# Points de vie (PV) des joueurs

Les PV existent dans le jeu depuis la PR #293 du jeu (combat). Cette page décrit ce que fait le jeu aujourd'hui, puis propose ce qui manque encore (départ, soins, K.O., mort).

## Ce que fait le jeu aujourd'hui

### PV = moral × 10

Les PV ne sont pas une stat à part : **1 point de moral = 10 PV**. Le moral en base fait foi ; le jeu garde seulement en mémoire les PV perdus sous la dizaine, pour que 3 dégâts ne coûtent pas un point de moral entier.

| | Valeur | Où dans le code |
| --- | --- | --- |
| Moral de départ | 100 (toutes les races) | `src/controllers/statRolls.js`, `src/controllers/db.js` |
| PV de départ | 100 × 10 = **1000 PV** | `HP_PER_MORAL` dans `src/controllers/combat.js` |
| PV maximum | **1000 PV** (moral 100) | `MAX_HP` dans `src/controllers/combat.js` |
| PV minimum | 0 (moral 0), affiché « K.O. » | |

Conséquence importante : **perdre des PV fait baisser le moral**, et le moral compte dans tous les jets (bonus de `(moral − 50) / 4`, ou `/ 2` pour les jets de module). Un joueur blessé réussit donc moins bien tout ce qu'il tente. À l'inverse, une carte qui « remonte le moral » rend aussi des PV.

Les compagnons (PNJ alliés) suivent la même règle. Les ennemis, eux, ont leurs propres PV (10 par défaut, réglés dans l'éditeur `/bestiaire`).

### Ce qui fait baisser les PV

- **Attaque ennemie réussie** : le MJ désigne l'attaquant et la cible ; si l'attaque touche, les dégâts sont retirés tout de suite selon le palier de l'ennemi : faible **1 à 4**, moyen **5 à 8**, fort **9 à 12** PV. Le MJ peut imposer l'issue (touché / raté) et les dégâts.
- **Statuts** posés par le MJ, qui agissent à chaque « Tour suivant » : Saignement (**1 à 4** PV par tour), Poison (**3** PV par tour), ou un statut inventé avec ses propres dégâts. Étourdi ne blesse pas (il empêche d'attaquer).
- **Cartes** qui font perdre du moral (le MJ applique la perte sur la stat Moral : −1 moral = −10 PV).
- **Le MJ**, à la main, à tout moment (menu MJ, liste de l'équipe : boutons ± 10 PV, Maj ± 100, Ctrl ± 50, ou saisie directe).

### Ce qui fait remonter les PV

- **Seulement le MJ**, à la main (même réglage que ci-dessus), ou en remontant la stat Moral.
- Aucun soin automatique : ni objet, ni repos, ni action de soin dans le jeu.
- Détail technique : les PV perdus sous la dizaine sont gardés en mémoire ; si le serveur redémarre, ils sont oubliés (le joueur remonte à la dizaine pleine).

### À 0 PV

L'onglet du joueur affiche « K.O. » et ses statuts s'arrêtent. Le jeu **n'empêche rien d'autre** : le MJ peut encore le viser, le joueur peut encore lancer des dés (avec un moral de 0, donc un gros malus). Il n'y a pas de mort.

## Proposition, à valider par le MJ

> **Proposition, à valider par le MJ.** Rien de ce qui suit n'est dans le jeu : ce sont des valeurs par défaut, faites pour l'échelle actuelle (1000 PV, coups de 1 à 12). Tout se règle à la main depuis le menu MJ, sans changer le code.

### PV de départ

Garder ce que fait le jeu : **1000 PV** (moral 100) pour tout le monde, quelle que soit la race. C'est aussi le maximum : un soin ne fait jamais dépasser 1000.

### K.O. (évanoui)

Un joueur est **K.O.** :

- quand il tombe à **0 PV** ;
- ou quand il a perdu **110 PV ou plus pendant le même combat** (c'est la règle de combat d'origine, « 11 points de moral perdus = évanoui », traduite en PV).

Un joueur K.O. ne joue plus et ne peut plus être visé jusqu'à la fin du combat. Le MJ le suit dans le journal du combat (les pertes de PV y sont notées).

### Mort

**Pas de mort définitive** : on ne laisse personne derrière.

- Si **tous les joueurs** sont K.O., le combat est perdu (règle de [combat](combat.md)) : ils se réveillent dans le vaisseau et l'équipage **perd 200 humains**.
- Un joueur K.O. se réveille à la fin du combat avec ses PV actuels ; s'il était à 0, il remonte à **100 PV** (moral 10).

### Soins

| Soin | Quand | Effet |
| --- | --- | --- |
| **Soigner un allié** | En combat, à la place de son action | Jet de **Survie** réussi : l'allié regagne **1d8 PV**. Tout le monde peut le tenter ; un infirmier peut y gagner un bonus (règle des rôles, en proposition). Pas sur soi-même. |
| **Premiers soins** | Une fois après chaque combat | Chaque joueur blessé peut être soigné une fois : jet de **Survie** du soigneur réussi → **+20 PV**. |
| **Objet de soin** | À tout moment (en combat : son action) | Objet consommable « trousse de soins » à ajouter dans l'éditeur d'objets : **+30 PV**. Les objets qui « remontent le moral » d'une race (Shrips pour les Omphors, pelote de laine pour les Neks, voir [Objets](../lore/objets.md)) donnent **+50 PV** (5 moral) à cette race. |
| **Repos sur une planète** | À chaque planète, que l'équipage atterrisse ou reparte | Tous les joueurs regagnent **100 PV** (10 moral). |
| **Cartes** | Selon la carte | Une carte qui remonte le moral rend les PV correspondants (+1 moral = +10 PV). |

Le MJ applique chaque soin avec le réglage des PV du menu MJ.
