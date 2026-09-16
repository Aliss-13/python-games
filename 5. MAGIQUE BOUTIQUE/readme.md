# 🧙‍♀️ Magique Boutique
« What sorcery is this ???? »

Magique Boutique est un jeu de gestion développé en Python, dans lequel vous incarnez une sorcière qui ouvre sa propre boutique d'objets magiques.

Vous devrez fabriquer **potions**, **sortilèges** et **grimoires**, gérer vos stocks, approvisionner les rayons, accueillir des clients plus ou moins recommandables et **développer votre jardin enchanté**.

Et accessoirement, devenir la plus grande sorcière commerçante du BHV.


## 🎮 Le principe

La boutique fonctionne comme une petite entreprise magique :

- récolter des ingrédients grâce au jardin enchanté ;
- fabriquer des objets magiques ;
- choisir entre les placer en réserve ou les mettre en rayon ;
- vendre automatiquement les objets exposés ;
- gérer l'argent et l'expérience ;
- améliorer les recettes ;
- débloquer progressivement de nouveaux ingrédients et objets ;
- répondre aux demandes de clients spéciaux ;
- accomplir des quêtes secondaires ;
- récupérer les fragments du Scarabac ;
- atteindre les objectifs nécessaires pour remporter la victoire.

La boutique continue également à évoluer avec le temps grâce à plusieurs **mécaniques basées sur le temps réel.**


## ✨ Fonctionnalités


### 🌿 Jardin enchanté

Le jardin produit automatiquement des **ingrédients** au fil du temps.

Son **niveau** détermine les ingrédients disponibles et ses améliorations permettent d'accélérer progressivement leur production.

La production est calculée à partir du temps réellement écoulé, ce qui permet au jardin de fonctionner sans avoir besoin d'une boucle permanente.


### ⚗️ Fabrication

Les objets disponibles sont définis dans une base de recettes comprenant notamment :

- potions ;
- sortilèges ;
- grimoires.

Chaque recette possède ses propres ingrédients, niveau requis, prix, expérience et coût d'amélioration.

**Les recettes peuvent être améliorées** afin d'augmenter progressivement leur valeur et l'expérience obtenue.


### 🏪 Gestion de la boutique

Après fabrication, un objet peut être :

- placé en réserve ;
- directement mis en rayon.

**Les objets exposés sont vendus automatiquement** selon un système de vente basé sur le temps.

Chaque vente génère :

- de l'argent ;
- de l'expérience ;
- une trace dans l'historique des ventes ;
- un dialogue aléatoire adapté à l'objet vendu.


### 🔔 Clients spéciaux

Certains clients apparaissent aléatoirement lorsque le niveau de la sorcière le permet.

Chaque client possède :

- ses propres dialogues ;
- plusieurs demandes possibles ;
- un niveau requis ;
- un niveau de patience ;
- des récompenses spécifiques.

Certains clients peuvent attendre lorsqu'un objet nécessaire n'est pas disponible.

Le **système de file d'attente** conserve notamment l'heure d'arrivée du client afin de calculer dynamiquement son temps d'attente.

Si le délai est dépassé, le client repart.

Et certains clients ont manifestement des problèmes beaucoup plus sérieux que l'attente d'une potion.


### 📈 Progression

**L'expérience** permet de monter de niveau.

**Les niveaux** débloquent progressivement :

- de nouvelles recettes ;
- de nouveaux ingrédients ;
- des améliorations du jardin ;
- de nouveaux clients.

La progression repose sur **plusieurs objectifs indépendants** :

- fabriquer toutes les recettes ;
- atteindre le niveau 20 ;
- compléter le Scarabac.


### 🪲 Le Scarabac

Le Scarabac est constitué de **six fragments** à récupérer au cours des récoltes.

Chaque fragment obtenu est conservé dans la sauvegarde et participe à l'un des objectifs de victoire.

Parce qu'une boutique de sorcellerie sans artefact mystérieux à reconstituer aurait probablement été beaucoup trop raisonnable.


### 🏆 Quêtes et objectifs secondaires

Le jeu possède également **plusieurs objectifs secondaires** basés sur les ventes réalisées.

Ils demandent notamment de vendre certaines catégories d'objets ou des exemplaires de chaque type de création.

Les ventes sont enregistrées et utilisées pour déterminer automatiquement la progression de ces objectifs.


### 💾 Sauvegarde

L'état du jeu est sauvegardé dans un fichier JSON.

La sauvegarde conserve notamment :

- niveau et expérience ;
- argent ;
- inventaire ;
- recettes débloquées ;
- améliorations des recettes ;
- stocks et objets en rayon ;
- historique des ventes ;
- clients en attente ;
- progression du Scarabac ;
- objectifs de victoire ;
- quêtes secondaires ;
- état de victoire.

Les clients en attente ne sont pas sérialisés directement : seules les informations nécessaires à leur reconstruction sont enregistrées.

Cela permet notamment de conserver leur arrival_time et de reprendre correctement leur temps d'attente après un chargement.


# 🛠️ Aspects techniques

Le projet a été développé en Python avec une architecture organisée en plusieurs modules spécialisés.

Quelques éléments techniques mis en œuvre :

- programmation orientée objet ;
- séparation des responsabilités entre modules ;
- gestion d'état du jeu ;
- sérialisation et désérialisation JSON ;
- sauvegarde et chargement ;
- génération et gestion de stocks ;
- systèmes de progression ;
- gestion d'événements ;
- systèmes temporels avec time ;
- files d'attente avec expiration ;
- génération aléatoire ;
- systèmes de récompenses ;
- suivi d'objectifs et de quêtes ;
- validation des entrées utilisateur ;
- gestion des erreurs et des anciennes sauvegardes.


## Architecture

Le projet sépare notamment les responsabilités entre plusieurs modules :

```python
main.py
│
├── menu.py
│
├── witch.py
│   └── état principal du joueur
│
├── garden.py
│   └── production des ingrédients
│
├── garden_ingredients.py
│   └── données des ingrédients
│
├── recipes.py
│   └── données des recettes
│
├── recipes_actions.py
│   └── fabrication, stocks et améliorations
│
├── clients.py
│   └── clients et événements
│
├── clients_choices.py
│   └── choix proposés aux clients
│
├── clients_results.py
│   └── résultats et récompenses
│
├── clients_queue.py
│   └── gestion des clients en attente
│
├── progression.py
│   └── niveaux, ventes, quêtes et victoire
│
├── save.py
│   └── sauvegarde / chargement
│
├── sale_dialogues.py
│   └── dialogues de vente
│
└── colors_and_names.py
    └── affichage et métadonnées

```

Cette séparation permet notamment de faire évoluer les différents systèmes indépendamment et de limiter les responsabilités de chaque module.


## 🧪 Un projet qui sert aussi de terrain d'expérimentation

Magique Boutique est avant tout un projet personnel de développement.

Il m'a permis de travailler progressivement sur des problématiques plus complexes qu'une simple succession de fonctionnalités :

- faire communiquer plusieurs systèmes entre eux ;
- conserver un état cohérent du jeu ;
- gérer la persistance des données ;
- réfléchir à la séparation entre données statiques et état dynamique ;
- construire des systèmes temporels ;
- refactoriser progressivement le code ;
- identifier et supprimer du code devenu inutile ;
- tester les interactions entre mécaniques plutôt que les fonctionnalités isolément.

Le projet a notamment évolué par itérations successives, avec plusieurs phases de refactorisation destinées à améliorer la lisibilité et la maintenabilité du code.


## 🚀 Installation

Prérequis : **Python 3**

Lancement : depuis le dossier du projet, exécuter python **main.py**.

Une **version exécutable** peut également être disponible dans les Releases du dépôt.


## 🧙‍♀️ Quelques créations

La boutique propose des objets dont la magie est parfois... discutable.

Parmi les créations disponibles :

- Potion de vie
- Philtre d'amour
- Polynectar
- Brazilian Butt Lift
- Gratte-cul
- Contrôle fiscal
- Les Lois de Murphy
- Optimisation des ressources humaines
- Vengeance à la harissa
- Djinns sexy et pentagrammes
- Jean-Marc Synergie
- Les petits déj d'enfer du Diable

Parce qu'il fallait bien donner une utilité commerciale à toute cette magie.


## 📌 État du projet

Projet fonctionnel et jouable.

Le développement actuel porte principalement sur la consolidation, la refactorisation et l'amélioration de l'architecture existante plutôt que sur l'ajout de fonctionnalités fondamentales.