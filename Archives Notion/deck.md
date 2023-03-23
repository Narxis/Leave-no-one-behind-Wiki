# Deck

On a :

- “pla” cartes planètes
- “pos” cartes positives
- “neg” cartes négatives
- “neu” cartes neutres
  
## Mode Fair / Mode Chaos

Fonctionnement du deck : (la première carte est la carte “Terre” et ne compte pas dans le nbr de carte “n”)

1. Sélection du nombre de carte (durée de la partie) “n” n=50/80/120
2. on coupe le nbr de carte en 4 part
3. L’algorithme sélectionne :
    1. “nbr.neu”neu parmis “neu”
    2. “nbr.neg”neg parmis “neg”
    3. “nbr.pos”pos parmis “pos”
    4. 5pla parmis “pla” avec la condition Moy(value:pla) ~1

4. L’algorithme range les cartes de la manière suivante : (non effectué en mode gamer)

5. Les pla sont ordonnée par “value” croissante et placées tout les n/5 cartes

6. L’algorithme coupe les (n/5) -1 cartes entre chaque planete en 3 parts

        1. “nbr.neu”/5 cartes neutres
        2. “nbr.neg”/5 cartes négatives
        3. “nbr.pos”/5 cartes positives

7. L’algorithme sélectionne le bon nombre de cartes dans les bonnes catégories et fixe leur position dans le deck.

8. La partie commence, on pioche la carte “Terre”

    ex: 50 (partie la plus courte)

    25neu, 15neg, 5pos, 5pla (neu>neg>pos≥pla=5) :point_up: value : Plus la “value” est haute, plus planète possède de bonnes stats [Planètes](https://www.notion.so/Plan-tes845cc45f4dec4512a8b9052febc6ac46) (value comprise entre “-1” et “2”)
