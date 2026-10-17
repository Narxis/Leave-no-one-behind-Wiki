# Monnaie et marchands

## Le crédit galactique

Le **crédit** (abrégé « cr ») est la monnaie des stations, des marchés et des casinos de la galaxie. L'OLI en confie un petit pécule à chaque membre d'équipage avant le départ.

Les marchands les moins regardants acceptent aussi d'être payés en **cryopods**. Pour eux, un humain en sommeil est une marchandise comme une autre. Pour l'équipage, payer ainsi revient à abandonner une partie de ceux qu'il doit sauver.

## Bourses

- Chaque joueur a sa propre **bourse**. Il commence la partie avec **20 crédits**.
- Le vaisseau a une **caisse de bord** commune, vide au départ.
- La bourse de chaque joueur s'affiche en haut de son coffre dans l'inventaire et dans sa vue joueur. La caisse de bord s'affiche en tête du stock du vaisseau.

## Gagner des crédits

Les crédits se trouvent dans les **butins**, comme les objets :

- **Butin de carte** : dans l'éditeur de cartes, on ajoute « Crédits » au butin d'un lieu, avec une quantité. Les crédits ramassés avec « Tout récupérer dans le vaisseau » vont dans la caisse de bord.
- **Butin de combat** : le MJ peut ajouter des crédits au butin d'un ennemi ou d'un combat.
- Un joueur qui glisse les crédits d'un butin vers son coffre les met dans sa bourse.

## Prix

- Chaque objet a un **prix en crédits**, fixé dans l'éditeur d'objets.
- Le cours est fixé à **5 cryopods pour 1 crédit**. Un objet à 25 crédits coûte donc 125 cryopods.
- Un marchand **rachète** un objet à **la moitié** de son prix, arrondie à l'entier inférieur. Le MJ peut changer ce prix au cas par cas.

Ordres de grandeur, repris du [marché casino](../lore/lieux/marche-casino.md) :

| Objet | Prix |
|---|---|
| Consommable | 10 crédits |
| Collection (moral) | 15 crédits |
| Outil de réparation | 20 crédits |
| Gadget électronique | 25 à 30 crédits |

## Rencontrer un marchand

Le MJ ouvre la boutique depuis le panneau **Marchand** du menu MJ :

1. Il donne un nom au marchand et compose son étal : des objets, leur prix et leur stock (vide pour un stock illimité). Le bouton « Objets à prix » remplit l'étal avec tous les objets du catalogue qui ont un prix.
2. Il ouvre la boutique. L'étal s'affiche alors sur l'écran de jeu, avec chaque prix en crédits et en cryopods.
3. **Acheter** : le MJ choisit l'acheteur (un joueur ou le vaisseau) et le moyen de paiement (crédits ou cryopods). Les cryopods sont toujours pris sur le vaisseau. L'objet arrive dans le coffre de l'acheteur.
4. **Vendre** : le MJ choisit le vendeur, puis l'objet à vendre. Le prix de rachat est modifiable.
5. Le MJ peut aussi ajouter ou retirer des crédits à une bourse (+10, −5) pour un pari, une amende ou un don.

Une bourse ne descend jamais sous zéro : un achat trop cher est refusé.

## Réglages

Le nom de la monnaie, son texte, le cours en cryopods, la part de rachat et les sommes de départ se règlent dans le fichier `src/config/currency.json` du jeu.
