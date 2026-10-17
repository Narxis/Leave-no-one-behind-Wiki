# Leave-no-one-behind-Wiki

## Français

Vous trouverez ici toutes les informations sur le lore de [Leave-no-one-behind](https://github.com/Narxis/Leave-no-one-behind).

### Le lore

- [L'univers](lore/univers.md) : le synopsis, la guerre terrienne, l'OLI
- [Le PLUGS](lore/vaisseau-plugs.md) : le vaisseau et ses modules
- [Les systèmes stellaires](lore/systemes-stellaires.md)
- [Les races](lore/races/README.md) : [Fneks](lore/races/fnek.md), [Omphors](lore/races/omphor.md), [Sylvs](lore/races/sylv.md), [Ygrls](lore/races/ygrl.md), [Shrymps](lore/races/shrymp.md), [Akus](lore/races/aku.md), [Yorcs](lore/races/yorc.md), [Neks](lore/races/nek.md)
- [Organisations](lore/organisations.md)
- [Personnages](lore/personnages.md)
- [Objets](lore/objets.md)
- [Lieux](lore/lieux/README.md) : dont 6 scénarios complets
- [Ennemis](lore/ennemis.md)

### Les règles

- [Déroulement d'une partie](regles/deroulement.md)
- [Création de personnage](regles/creation-personnage.md)
- [Rôles des joueurs](regles/roles.md) : capitaine, pilote, infirmier…
- [Règle de combat](regles/combat.md)
- [Points de vie](regles/points-de-vie.md) : PV des joueurs, soins, K.O.
- [Statuts](regles/statuts.md)
- [Cartes et deck](regles/cartes-et-deck.md)
- [Score](regles/score.md)
- [Artisanat](regles/artisanat.md)
- [Monnaie et marchands](regles/monnaie.md)
- [Guide du maître du jeu](regles/guide-mj.md) (à écrire)

Les tableaux « Dans le jeu » (stats des races, objets, statuts) sont recopiés depuis les fichiers du jeu, qui font foi pour les chiffres. Ils se trouvent entre les marqueurs `<!-- jeu:debut … -->` et `<!-- jeu:fin -->` : ne les modifiez pas à la main, le reste de la page est libre. Ils sont mis à jour par l'action « Tableaux du wiki » du dépôt du jeu, ou à la main depuis le dossier du jeu : `npm run wiki-tableaux -- ../Leave-no-one-behind-Wiki` (ajouter `--customs` pour inclure les races customs de l'éditeur).

### Le reste

- [Glossaire](glossaire.md) : acronymes et jeux de mots
- [Archives Notion](archives-notion/) : l'export d'origine, gardé tel quel pour référence

Quand le wiki et le jeu se contredisent, c'est le MJ qui décide, sauf mention contraire.

### Le site pour les joueurs

L'univers et les règles sont publiés sur **https://narxis.github.io/Leave-no-one-behind-Wiki/** (menu, recherche, lisible sur téléphone). Les pages des races, des objets, des lieux, des ennemis, le guide du MJ et les archives Notion n'y sont pas : elles restent ici pour le MJ, et les joueurs les découvrent dans le Codex du jeu.

- **À faire une seule fois** : sur GitHub, *Settings → Pages → Build and deployment → Source : GitHub Actions*. Ensuite, chaque modification de `lore/`, `regles/` ou `glossaire.md` poussée sur `main` met le site à jour (action « Site du wiki », `.github/workflows/site.yml`). On peut aussi la lancer à la main depuis l'onglet *Actions*.
- **Ajouter ou retirer une page du site** : la liste `nav` de `mkdocs.yml`. Seules les pages de cette liste sont publiées ; un lien vers une page non publiée s'affiche comme du texte simple (`publication/hooks.py`).
- **Voir le site sur son PC** : `pip install -r publication/requirements.txt`, puis `mkdocs serve` et ouvrir http://127.0.0.1:8000.

## English

You will find here all the information about the lore of Leave-no-one-behind. The wiki is written in French.
