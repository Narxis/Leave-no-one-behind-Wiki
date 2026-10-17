# Score

Ce calcul est celui du jeu (`src/controllers/default.js` et `src/models/ship.js`).

## L'atterrissage abîme le vaisseau

Au moment de se poser, plus le module d'atterrissage est abîmé, plus le reste souffre :

- scanners, détection, moteurs, oxygène, énergie et gravité perdent chacun `(100 − atterrissage) / 4` ;
- les cryopods perdent `10 × (100 − atterrissage) / 4` humains.

## Les trois scores

**Score vaisseau**

```
S1 = 30×scanners + 30×détection + 40×(oxygène + énergie + gravité)
   + 80×construction + 120×(BDD scientifique + BDD historique)
```

**Score planète**

```
S2 = 85×oxygène + 60×gravité + 95×eau + 80×ressources
   + 55×climat + 30×(faune + flore) + 65×civilisation
```

**Bonus cartes** (neg, neu, pos = cartes jouées de chaque type, les lieux comptent comme neutres)

```
S3 = min(6000×neg + 3500×neu + 3500×min(planètes, 10) × min(planètes visitées − 1, 9), 500000)
   − 4500×pos
```

**Score final**

```
Score = humains × S1 × S2 / 500000 + S3
```

En clair : garder le vaisseau en bon état, choisir une bonne planète et traverser beaucoup d'épreuves. Les cartes positives coûtent des points.

## Écart avec l'ancien calcul

Le facteur 3500 du terme des planètes, prévu par la page Notion « Scoring », manquait dans le code ; il a été rétabli dans le jeu (PR #289 du dépôt du jeu). La page Notion prévoyait aussi des pertes d'humains liées à la faune, la flore et la civilisation de la planète, qui ne sont pas dans le jeu. Voir les [archives](../archives-notion/).
