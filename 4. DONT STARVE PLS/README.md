# 🌲 DON'T STARVE PLS

```« Tu vas mourir ici mon petit pote… »```

DON'T STARVE PLS est un jeu de survie développé en Python et jouable dans le terminal.

Le principe est simple : survivre assez longtemps pour pouvoir repartir.

Pour y parvenir, il faudra explorer le monde, récolter des ressources, fabriquer des outils et des équipements, construire ton campement, gérer ta faim, ton endurance et ta santé mentale… et surtout anticiper l'hiver.

Parce que manifestement, rester tranquillement chez soi en attendant les beaux jours était trop facile.


## 🎮 Principe du jeu

Tu incarnes un survivant perdu dans un monde hostile.

Chaque action a un coût et tes ressources sont limitées. Il faut donc constamment faire des choix :

- récolter du bois, de la pierre, de l'herbe ou de la nourriture ;
- gérer ta satiété et ton endurance ;
- explorer de nouvelles zones ;
- améliorer ton équipement ;
- construire des structures utiles ;
- transformer les ressources récoltées ;
- te préparer à l'arrivée de l'hiver ;
- préserver ta santé mentale ;
- retrouver les pièces d'un mystérieux navire.


Ton objectif ultime :

⚓ Construire le Hollandais Volant

Une fois toutes les pièces récupérées et les ressources nécessaires réunies…

👻 Le Hollandais Volant se matérialise dans la brume…

🚢 Tu quittes ce monde.

🏆 VICTOIRE

Parce que survivre éternellement dans une forêt hostile n'était visiblement pas le projet.


## ❤️ Survivre

Trois jauges déterminent ton état :

```python
🍽️ Satiété
⚡ Endurance
🧠 Santé mentale
```

Si l'une d'elles tombe à zéro, c'est terminé.

Les actions de survie ont donc un coût : récolter des ressources consomme de l'endurance et de la satiété, tandis que la nuit et l'hiver apportent leurs propres pénalités.

Il faudra apprendre à gérer tes ressources plutôt que de cliquer frénétiquement sur « récolter » jusqu'à ce que ton personnage rende l'âme.


## 🌦️ Un monde qui évolue

Le jeu fonctionne avec un **cycle jour / nuit** et **quatre saisons**.

La nuit, des monstres rôdent, rendant les récoltes périlleuses.

L'hiver est particulièrement dangereux :

- les conditions climatiques fatiguent davantage le personnage ;
- des tempêtes de neige peuvent se produire ;
- la gestion de la nourriture devient plus importante ;
- certains bonus d'équipement permettent de mieux résister au froid ;
- il faut anticiper son arrivée pour ne pas se retrouver complètement démuni.

❄️ « L'hiver arrive dans… »

Tonton Ned avait pourtant prévenu.


## 🗺️ Exploration

Le monde est composé de plusieurs **zones** :

```python
🕳️ Grotte
🏔️ Montagne
🌲 Forêt
🌾 Plaine
🏜️ Désert
🌴 Jungle
🌊 Rivière
```

L'exploration et les déplacements consomment des ressources et des actions. 

Les zones sont connectées entre elles. Elles contiennent des ressources ainsi que des éléments nécessaires à la progression.

L'exploration permet également de rechercher les différentes pièces du Hollandais Volant.


## 🌿 Récolte et ressources

Les **ressources** sont obtenues grâce à des **récoltes** soumises à des probabilités.

La quantité récoltée dépend notamment :

- du type de ressource ;
- de la zone explorée ;
- de la saison ;
- du hasard ;
- des outils possédés.

Certaines récoltes peuvent également produire du **butin rare**.

Par exemple :

✨ Pépite d'or trouvée !

Parce qu'il fallait bien une raison supplémentaire de retourner casser des cailloux.


## 🛠️ Fabrication et progression

Les ressources récoltées peuvent être utilisées pour fabriquer différents équipements.

```python
🔨 Structures
🔥 Feu de camp
🛖 Abri
🧵 Machine à coudre
🌐 Cage de Faraday
🚿 Douche portative
🪕 Banjo
🐮 Élevage
🥛 Laiterie
🧀 Fromagerie
```

Les **structures** permettent d'améliorer les conditions de survie et certaines produisent même des ressources automatiquement.

```python
🪓 Outils
🪓 Hache
⛏️ Pioche
🗡️ Couteau de chasse
🔪 Machette
```

Les **outils** améliorent les quantités récoltées.

```python
🧥 Vêtements
🎩 Chapeau
🧥 Manteau
🧤 Gants
🥾 Bottes
```

Les **vêtements** permettent notamment de réduire certains effets du froid ou le coût des actions.


## 🧺 Transformation des ressources

Les ressources peuvent également être transformées afin de débloquer de nouvelles possibilités :

```python
🌿 → 🪢 Corde
🪢 → 🟩 Tissu
🥩 → 🍖 Nourriture cuite
🥛 → 🧀 Fromage
```

Certaines transformations nécessitent d'avoir construit les structures correspondantes.


## 🍖 Gestion de la nourriture

Plusieurs aliments peuvent être consommés avec des effets différents :

```python
🥩 nourriture crue
🍖 nourriture cuite
🥛 lait
🧀 fromage
```

Chaque aliment peut modifier :

- la satiété ;
- l'endurance ;
- la santé mentale.

La nourriture devient donc un véritable outil de gestion des ressources, et pas simplement une jauge à remplir.


## 🧠 Santé mentale

La survie ne concerne pas uniquement le corps.

La nuit, les conditions difficiles et certaines situations affectent également la santé mentale.

À l'inverse, certaines constructions permettent de la restaurer.

🪕 +5 santé mentale
« Ça me rappelle un film… »

On ne juge pas les méthodes thérapeutiques de ce survivant.


## 🎯 Objectifs

Le jeu propose trois grands objectifs :

❄️ **Survivre à l'hiver**

```python
    Prépare-toi avant son arrivée.

    « La nourriture et les plantes vont disparaître…
    Puis la chaleur…
    Puis la confiance en tes décisions… »
```

🗺️ **Explorer le monde** : découvre toutes les zones de la carte et leurs environs.


⚓ **Construire le Hollandais Volant** 

Retrouve les pièces nécessaires, rassemble les ressources et construis le navire permettant de quitter ce monde.
```🎵🤘 Ohé ohé capitaine abandonné ! 🤘🎶 Hum. Pardon.```


## 💾 Sauvegarde

La partie peut être sauvegardée et restaurée grâce à un fichier JSON.

La sauvegarde conserve notamment :

- les statistiques du joueur ;
- l'inventaire ;
- la nourriture ;
- les vêtements ;
- les outils ;
- les structures construites ;
- les pièces du Hollandais Volant ;
- l'état du monde et sa progression.

Le système fonctionne également avec la version exécutable du jeu.



# 🧩 Architecture

Le projet est organisé en plusieurs modules afin de séparer les différentes responsabilités :

```python
DON'T STARVE PLS/
│
├── main.py
├── player.py
├── world.py
├── menu.py
├── display.py
├── buildings.py
├── food.py
└── save.py
```

Quelques responsabilités principales :

- **player.py** → statistiques, récolte, survie, sommeil et actions du joueur
- **world.py** → monde, zones, saisons, cycles et exploration
- **buildings.py** → structures, outils, vêtements et fabrication
- **food.py** → nourriture et effets
- **display.py** → affichage des jauges, carte, objectifs et informations
- **menu.py** → navigation et interactions avec le joueur
- **save.py** → sauvegarde et chargement JSON
- **main.py** → lancement du jeu et boucle principale


## 🛠️ Technologies

- Python 3
- programmation orientée objet
- dictionnaires et structures de données
- génération aléatoire avec random
- sauvegarde / chargement avec JSON
- architecture modulaire
- interface en ligne de commande
- gestion d'un état de jeu persistant


## 🚀 Installation

Prérequis : **Python 3**
Lancement : depuis le dossier du projet, exécuter python **main.py**.
Une **version exécutable** peut également être disponible dans les Releases du dépôt.


## 🎮 Quelques caractéristiques du jeu

```python
🌲 exploration
🪵 récolte de ressources
🍖 gestion de la nourriture
❤️ gestion de trois jauges de survie
🌦️ cycle des saisons et alternance jour/nuit
🛠️ fabrication
🏕️ construction
🧥 équipement
🎲 récoltes aléatoires
✨ butin rare
🗺️ carte à explorer
⚓ quête du Hollandais Volant
💾 sauvegarde JSON
🧠 santé mentale
🧀 fromage
```

Parce qu'un jeu de survie sans fromage serait tout simplement une erreur de conception.


## 📚 Ce que ce projet m'a permis de pratiquer

Ce projet m'a permis de travailler notamment sur :

- la programmation orientée objet ;
- la modularité d'un projet Python ;
- la gestion d'un état de jeu ;
- la création de systèmes de survie ;
- la gestion de ressources ;
- les probabilités et la génération aléatoire ;
- les interactions entre systèmes ;
- la sauvegarde et le chargement de données ;
- la conception d'une boucle de gameplay complète.

DON'T STARVE PLS est avant tout un projet d'expérimentation et d'apprentissage, construit autour de l'envie de créer un jeu de survie complet, avec ses propres mécaniques, son humour et son petit lot de décisions discutables.