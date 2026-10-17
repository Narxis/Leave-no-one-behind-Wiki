# Interface

[https://github.com/Narxis/Leave-no-one-behind](https://github.com/Narxis/Leave-no-one-behind)

![Page 1.png](Interface%20b9f316acf540466cb77c85a84bec0ac0/Page_1.png)

![Page 3.png](Interface%20b9f316acf540466cb77c85a84bec0ac0/Page_3.png)

![https://media.discordapp.net/attachments/616675777974632483/1039917932878250015/image.png?width=1246&height=701](https://media.discordapp.net/attachments/616675777974632483/1039917932878250015/image.png?width=1246&height=701)

![Page 4.png](Interface%20b9f316acf540466cb77c85a84bec0ac0/Page_4.png)

![Drop-down menu.png](Interface%20b9f316acf540466cb77c85a84bec0ac0/Drop-down_menu.png)

![Carte evenement.png](https://cdn.discordapp.com/attachments/616675777974632483/1035804541469335592/unknown.png)

(  🔴 = éléments animés
   🔵= FlexBox)

### Dans un “menu déroulant 1”: “vaisseau”

Pv du vaisseau (par défaut) : “1000 passagers”

stats du vaisseau: “radars, speed ?, base de donnée de connaissances humaines, système d’atterissage, sytème d’aide à la construction, etc “ (collectibles?)

“colectible pour examiner mieux les planètes” (drones\ fusée de reconnaissances (1\2 joueurs descendent sur la planète en reconnaissance)

au debuts toutes les stats sont à 100%

Carburant = nombre de “tours\cartes jouées”

modules = états des modules (0-100%) et une checkbox si upgrade (que le mj cochera au cours de la partie)

### Dans un “menu deroulant 1” : “fiches joueurs”

Les joueurs ont le choix d’une race parmis “?” dans “un menu déroulant”

stats des joueurs :

Combat

Pilotage

Ingénierie

Survie

Reconnaissance

Moral

(Une option de roll random des stats) : possibilité de donné aux joueurs une “compensation” si le roll de stats est “faible” (exemple capacités spéciales à sélectionner dans un “menu déroulant”)

### Dans un “menu déroulant 1” : “Carte actuelle\temps présent”

décris “la carte\l’évènement” avec du texte

Maybe afficher les stats du vaisseau sur cette page aussi (genre dans un rectangle en haut ou jsp cf: @Narxis)

Les joueurs font une action (libre) et le Mj choisit “l’outcome”

Outcome :

Perte de stats du vaisseau (hp ou autre)

Gain de stats\ collectible (sauf hp, gain possible de carburant)

### Dans un “menu déroulant 1” : “carte précédente (maybe historique complet)”

Voir la\les actions passées 

Voir les modifs de stats effectuées  

Un menu avec toutes les cartes (possibilité de les disable)

[](https://i.imgur.com/6NNZW9K.png)

Faire un “wrap effect” en transition de carte :
La page entière se fait aspirer au centre et laisse apparaitre un effet où des étoiles défilent vers l’utilisateur jusqu’à laisser apparaitre la nouvelle carte/page

[https://codepen.io/Seasle/pen/VVeEdK](https://codepen.io/Seasle/pen/VVeEdK)

Une animation de transition entre image du vaisseau et première carte (au début de la partie).

 Texte animé genre matrix genre console de l’autopilote du vaisseau 

“Mise à jour de l’autopilote en v7.27 rev B……”

“Vérification de l’état des cryopods[…]”

“1000 humains détectés, démarrages des cryopods.”

“Calcul de l’itinéraire en cours[…]

“Quantité carburant ~ 250mg”

“5 planètes trouvées sur l’itinéraire”

“Initialisation de la phase de lancement”

“Partir un jour sans retour ?” [Y/ ~~N~~ Y] 

“5”

“4”

“7”

“2”

“1”

“Zero”

un “menu” qui affiche les status 

Faire une animations des cartes planètes : les stats sont flottantes et les petits traits apparaissent quand on hover la stat.

Trucs qui s’affiche quand on est sur une carte évènement : 

La carte (avec % des 6 modules et timer + choix et bouton suivant ) 

Une text box pour chaque personnage pour rentrer les jets de dès “player tab”

Les consommables/ status 

Une nav bar pour naviguer (genre en haut à gauche)

Historique genre en haut 

Menu qui sort du mur (genre droite) pour les stats des modules qui sont pas déjà affichées

Menu pour voir les fiches persos