# Artisanat

Repris de la page Notion « Craft rules » (avril 2023).

- On ne peut fabriquer que **dans le vaisseau** et **pendant un moment calme**. Le jeu refuse l'artisanat pendant un combat.
- Améliorer l'armurerie augmente les chances de réussite.
- La commande `/forge` du bot Discord n'existe pas encore. Pour l'instant, c'est le MJ qui lance la fabrication.

## Recettes

Une recette se saisit dans l'**éditeur d'objets**, sur l'objet fabriqué :

- les ingrédients, choisis dans le catalogue, avec leur quantité (huit au plus) ;
- le nombre d'exemplaires fabriqués.

Exemple : un **filet paralysant** se fabrique avec 2 cordes et 1 tazer cosmique.

D'autres idées de recettes (pièges, grenades, armes, boucliers, flèches…) sont listées dans [Objets](../lore/objets.md#idées-pas-encore-dans-le-jeu).

## L'atelier du MJ

Le panneau **Atelier** du menu MJ sert à fabriquer :

1. Le MJ choisit l'**artisan** : un joueur, ou le vaisseau (son stock commun). Les ingrédients sont pris dans l'inventaire de l'artisan, et l'objet fabriqué y arrive.
2. Chaque recette affiche ses ingrédients et le nombre que l'artisan en possède. S'il en manque, ils sont en rouge et le bouton « Fabriquer » est grisé.
3. **Assemblage libre** : le MJ peut aussi assembler n'importe quels objets de l'artisan et décider lui-même du résultat. Ce résultat peut être un objet du catalogue ou un nouveau nom.
4. L'objet fabriqué est annoncé sur l'écran de jeu.

## Réussite

- Par défaut, le jeu lance un dé 100. La chance de réussite est de **70 %**, plus **10 % par niveau d'armurerie** (niveaux 0 à 3, réglés dans l'atelier).
- Le MJ peut décocher « Lancer le dé de réussite » : la fabrication réussit alors toujours.
- En cas d'échec, les ingrédients sont perdus.

Ces valeurs se règlent dans le fichier `src/config/craft.json` du jeu.

## À trancher

- Les objets sont-ils partagés par l'équipage ou personnels ?
- Faut-il limiter le nombre d'objets et de consommables ?
- Comment améliore-t-on l'armurerie en jeu (coût, carte, réparation) ?
