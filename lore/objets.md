# Objets

## Dans le jeu

Ces objets existent dans `src/config/items.json` (catalogue modifiable dans l'éditeur `/items` du jeu). Les tableaux sont recopiés depuis le jeu.

### Objets de départ, par race

<!-- jeu:debut objets-depart -->

_Généré depuis `src/config/items.json` du jeu : ne pas modifier à la main._

| Race | Objet | Type | Description |
| --- | --- | --- | --- |
| Fnek | Fronde Fnek | Arme | Malgré leurs avancées technologiques, les Fneks préfèrent utiliser une fronde pour se battre. Généralement, ces frondes sont fournies avec des boules puantes qui libèrent un puissant concentré d'odeur de Fnek. |
| Omphor | Shrips | Consommable | Les Shrips sont des chips goût crevette qui ont la forme de Shrymps, elles peuvent remonter le moral des Omphors |
| Omphor | Armure en "Kev-lard" | Armure | L'armure en Kev-lard rend son utilisateur plus résistant mais limite ses déplacements |
| Sylv | Pelote de laine | Consommable | Offrir une pelote de laine à un Nek lui remonte le moral. |
| Sylv | Tazer cosmique | Arme | Un tazer utilisant l'énergie cosmique |
| Ygrl | Fouet Ygrl | Arme | Un fouet |
| Shrymp | Shrymp Utility Kit | Outil | Le Shrymp Utility Kit (kit de campement) contient de nombreux ustensiles |
| Shrymp | Corde | Outil | Une corde dans le Shrymp Utility Kit |
| Shrymp | Lampe torche | Outil | Une lampe torche dans le Shrymp Utility Kit |
| Shrymp | Nourriture déshydratée | Consommable | De la nourriture déshydratée |
| Shrymp | Dictionnaire Ygrlien | Divers | Un dictionnaire du langage Ygrl (inutile) |
| Shrymp | Mèche d'Ygrl | Divers | Une mèche de cheveux d'Ygrl |
| Shrymp | Lance Shrymp | Arme | Une lance qui fait approximativement la taille d'un cure-dent. |
| Aku | L'Aku tosswice | Outil | Une sorte de boîte à outils contenant beaucoup d'objets |
| Aku | Outils | Outil | Outils de maintenance variés |
| Aku | Boule puante Fnek | Munition | Une boule puante pour fronde Fnek |
| Aku | Paquet de Shrips | Consommable | Les Shrips sont des chips goût crevette qui ont la forme de Shrymps, elles peuvent remonter le moral des Omphors |
| Aku | Cure-dent | Divers | Un cure-dent |
| Aku | Montre-Boussole | Outil | Une montre-boussole (qui montre soit l'heure soit la direction, en fonction de l'heure actuelle) |
| Aku | Passeport | Divers | Un passeport |
| Aku | Balle de Nek-k47 | Munition | Une balle de Nek-k47 |
| Yorc | Massue Yorc | Arme | Une massue seulement utilisable par un Yorc au cœur pur |
| Nek-Eau | Filet paralysant | Arme | Filet pouvant neutraliser temporairement une cible à distance |
| Nek-Feu | Projectile à combustion | Arme | Dagues de lancer utilisant la chaleur des Nek-Feux pour accélérer vers sa cible |
| Nek-Terre | Nek'Ronomicon | Divers | Un recueil religieux avec un double fond pour stocker des objets |
| Nek-Terre | Nek-k47 | Arme | Un revolver nektologique pouvant être stocké dans un double fond |
| Nek-Air | Em-0 Droid | Gadget | Un drone pouvant prendre des vidéos en 64k 1440fps |

<!-- jeu:fin -->

### Autres objets

<!-- jeu:debut objets-autres -->

_Généré depuis `src/config/items.json` du jeu : ne pas modifier à la main._

| Catégorie | Objet | Type | Description |
| --- | --- | --- | --- |
| Électronique | Projecteur de bouclier personnel | Armure | Le projecteur de bouclier personnel est un dispositif utilisant l'énergie cosmique permettant d'absorber un coup ou un projectile ciblant l'utilisateur. Le projecteur de bouclier personnel doit être rechargé en énergie cosmique avant de pouvoir être réutilisé. |
| Électronique | Drone | Gadget | Un drone pour révéler les stats des planètes. |
| Électronique | SPIDER bomb | Arme | Une bombe qui permet d’infliger de lourds dégâts à sa cible sans causer beaucoup de dégâts collatéraux. |

<!-- jeu:fin -->

### Objets trouvés dans les cartes

SPIDER bomb (*Spooky Powerful Intelligent Directed Explosive Reliable Bomb*), bouteille offerte au pub (marque « Jaks Dimalou's »), antivirus à usage unique, boules de Chris Tale, outils de réparation de module.

## Le Nek'Ronomicon

Deux objets portent ce nom (avec un R majuscule), et les deux sont gardés :

- le **recueil religieux à double fond** des Nek-Terres, objet de départ (`items.json`) ;
- le **livre qui sait tout** : il contient toute la connaissance du monde, répond à une question puis explose (et blesse celui qui l'a posée). On peut le gagner à la bibliothèque de l'espace (brouillons de cartes neutres).

## Idées pas encore dans le jeu

Le Notion (« Idées objets ») contient beaucoup plus d'idées. Elles utilisent parfois des statistiques que le jeu n'a pas (force, dextérité, charisme, intelligence, perception).

- **Composants** : planche, ferraille, tissu, cuir, verre, cristal cosmique, poudre à canon, essence, pièges et grenades vides… et des butins de PNJ (cheveux d'Ygrl, huile essentielle de Fnek, lettre de Dimalou, uranium, mycélium, brochure, amende…).
- **Pièges par race** : piège vide + l'appât de la race (Yorc : huile de Fnek ; Shrymp : cheveux d'Ygrl ; Aku : lettre de motivation ; Fnek : uranium ; Sylv : lettre de Dimalou ; Omphor : Shrips ; Ygrl : mycélium ; Nek-Eau : poisson ; Nek-Feu : micro ; Nek-Terre : brochure ; Nek-Air : amende).
- **Grenades** : fumigène, aveuglante, incapacitante, leurre, assourdissante, IEM.
- **Armes, boucliers, armures** : pied de biche, nunchaku, poêle, arc, arbalète, flèches spéciales, pistolet laser, targe, pavois, casque de chantier…
- **Nourriture et stimulants** : stimu-lents, stimu-rapides (café Neksafé, Aderall de l'espace), burger Fnek, tacos du centre commercial, cocaféine…
- **Drones** : Alde Trump, cam-et-rat, toutou, chat, tortue.
- **Livres-tutoriels** : « Man VS Space », « Apprendre à dire non pour les nuls », « Livre de Fnekanique quantique »…
- **Films par race** : voir chaque page de race.

Les règles d'artisanat sont dans [Artisanat](../regles/artisanat.md).
