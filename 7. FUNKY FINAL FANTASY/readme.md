# FUNKY FINAL FANTASY
Fiche de projet — version pré-release

## 🎮 Concept

Funky Final Fantasy est un RPG textuel en Python, centré sur l'exploration de zones, les combats, les quêtes, les ennemis, le butin et la progression du joueur.

Le jeu fonctionne entièrement en interface texte avec affichage des événements, combats, inventaire, équipement, progression et dialogues.


## 🏗️ Architecture actuelle

Le projet a été largement refactorisé autour d'un objet central : **GameState**

Il constitue désormais l'état global du jeu et centralise notamment :

- l'équipe du joueur ;
- les ennemis et leur progression ;
- l'inventaire ;
- la zone actuelle ;
- les quêtes actives ;
- les quêtes terminées ;
- les ennemis uniques vaincus ;
- les PNJ ayant débloqué de nouveaux dialogues.

Cette architecture permet d'éviter de faire circuler une multitude de valeurs entre les fonctions.

Principe retenu

Le jeu passe par game plutôt que par une succession de valeurs indépendantes.


## ⚔️ Système de combat

Le système de combat utilise un **CombatContext** pour regrouper les informations nécessaires au déroulement d'un combat.

La **génération des équipes ennemies** prend en compte :

- la zone ;
- la difficulté ;
- la catégorie de l'événement ;
- la rareté ;
- les ennemis disponibles ;
- les ennemis uniques déjà vaincus.
- Types particuliers

### Boss / sous-boss

- apparaissent seuls ;
- ne réapparaissent pas lorsqu'ils sont uniques et déjà vaincus.

### Ennemis rares

- apparaissent lors des événements dédiés ;
- sont générés individuellement ;
-ne forment pas accidentellement des équipes de plusieurs rares.

### Ennemis uniques

- ne peuvent apparaître qu'une seule fois ;
- sont enregistrés dans defeated_unique_enemies.


## 👹 Progression des ennemis

Le jeu distingue notamment :

**Ennemis classiques** : leurs éliminations sont comptabilisées dans les progressions classiques de quêtes.

**Ennemis uniques** : leur victoire est enregistrée dans **game.defeated_unique_enemies**

Cela permet :
- d'empêcher leur réapparition ;
- de valider leurs quêtes spécifiques ;
- de faire progresser les quêtes kill_each.


## 📜 Système de quêtes

Les quêtes sont regroupées dans une **classe Quest**.

**Types actuellement pris en charge** :

- collect_items
- kill_each
- kill_group
- discover_each

**Progression dynamique** : la progression peut être recalculée à partir du GameState.

Pour kill_each :
- les ennemis uniques utilisent defeated_unique_enemies ;
- les ennemis classiques utilisent objectives_progress.

Cela permet à une même quête de gérer correctement les deux types d'ennemis.


## 🔔 Système d'événements

Les actions du joueur produisent des événements de jeu. Exemple : GameEvent("kill", enemy.id)

Ces événements peuvent ensuite :
- faire progresser les quêtes ;
- déclencher leur validation ;
- débloquer des dialogues ;
- modifier la progression de zone.

Le système permet ainsi de découpler les actions du joueur des conséquences qu'elles peuvent provoquer.


## 💬 PNJ et dialogues

Certains événements importants peuvent débloquer de nouveaux dialogues.

Les ennemis uniques vaincus peuvent déclencher des déblocages de dialogues via un système de correspondance entre ennemi et PNJ.

Les PNJ concernés sont enregistrés dans **game.npcs_with_new_dialogue**.


## 🎁 Butin et objets

Le jeu utilise une **génération d'objets** permettant de créer de véritables instances d'objets.

Les objets peuvent notamment posséder :
- un identifiant ;
- un niveau d'objet ;
- une rareté ;
- une quantité ;
- des bonus.

La génération est utilisée pour :
- le butin des ennemis ;
- les récompenses de quêtes ;
- les objets évolutifs.

Une attention particulière a été portée au niveau des objets générés afin d'éviter les récompenses disproportionnées par rapport au niveau du joueur.


## 💾 Sauvegarde

Le système de sauvegarde repose sur **SaveManager**.

La sauvegarde contient notamment :
- l'équipe ;
- les ennemis vaincus ;
- l'inventaire ;
- la zone actuelle ;
- les quêtes actives ;
- les quêtes terminées ;
- les progressions associées ;
- les ennemis uniques vaincus.

Le format de sauvegarde prévoit également des mécanismes de migration pour les anciennes données.


## 🌲 Progression des zones

Les zones disposent d'une progression propre.

Une zone peut être considérée comme terminée lorsque :
- sa progression atteint le maximum prévu ;
- les conditions finales, notamment le boss, sont remplies.

La vérification est centralisée dans **is_zone_complete(game)**

Le message de fin de zone est déclenché après la résolution complète du combat final, plutôt que depuis la validation d'une quête.


```python
══════════════════════════════════════
       🌲 FORÊT OBSCURE CONQUISE 🌲
══════════════════════════════════════

Vous avez traversé la Forêt obscure.

✨ Zone terminée !

Les créatures qui la hantaient ont été vaincues,
ses secrets ont été révélés,
et les habitants peuvent enfin respirer un peu.

              — FIN DE LA ZONE —
```

## 🧪 Phase de test pré-release

Plusieurs problèmes importants ont été identifiés et corrigés :

- apparition multiple d'ennemis uniques ;
- équipes composées accidentellement de plusieurs ennemis rares ;
- mauvaise progression des quêtes kill_each ;
- progression différente entre ennemis uniques et ennemis classiques ;
- déblocage de dialogues après victoire contre un ennemi unique ;
- récompenses de quête trop puissantes ;
- problèmes de migration de sauvegarde ;
- affichage incorrect de certains objets ;
- déclenchement prématuré de la fin de zone.

## 🚀 État actuel
Statut : 🟢 PRÉ-RELEASE

Le parcours principal a été testé de bout en bout.

Les systèmes principaux fonctionnent ensemble :

Exploration
    ↓
Événement
    ↓
Combat
    ↓
Ennemis vaincus
    ↓
Événements de jeu
    ↓
Quêtes / dialogues / progression
    ↓
Loot
    ↓
Progression de zone
    ↓
Boss
    ↓
Fin de zone



## 🏆 Bilan

Le projet a évolué d'un ensemble de systèmes séparés vers une architecture beaucoup plus cohérente autour de GameState, des événements et des quêtes.

Le gros chantier de refactorisation est désormais derrière nous.

Version actuelle

Funky Final Fantasy — prête pour sa première release. 


# Architecture


Funky Final Fantasy est un RPG développé en Python et jouable dans le terminal. Le projet met l’accent sur une architecture modulaire (combat, quêtes, événements, inventaire, sauvegarde, progression de zone) afin de séparer clairement les responsabilités de chaque composant du jeu.


## Fonctionnalités


- Combat au tour par tour
- Gestion d’une équipe de personnages
- Gestion d’une équipe ennemie
- Système d’équipement
- Génération aléatoire d’objets
- Quêtes et événements
- Progression de zone
- Sauvegarde et chargement de partie


## Choix techniques


- Architecture orientée objet
- Séparation des responsabilités par modules
- Sérialisation des données en JSON
- Génération procédurale d’objets

Le projet a été progressivement refactorisé afin d’améliorer sa maintenabilité, notamment par l’introduction d’un objet **GameState** centralisant l’état de la partie.


## Architecture du projet


- **main.py** : point d’entrée du jeu

- **protagonists/** : personnages jouables et ennemis (statistiques, équipement, compétences, montée de niveau, progression)

- **skills/** : compétences des personnages et des ennemis (dégâts, soins, ciblage, déclenchement d’effets)

- **effects/** : effets appliqués par les compétences (dégâts/soins périodiques, bonus/malus, provocation, immobilisation, attaques différées)

- **npcs/** : personnages non joueurs (dialogues, interactions, déclenchement de quêtes)

- **zones/** : progression des zones, sous-boss, boss et exploration

- **inventory/** : objets, génération, équipement, utilisation, tables de butin

- **quests/** : gestion des quêtes et intégration avec les événements du jeu

- **events/** : événements de zone (découverte, combat, récolte de ressources, interactions)

- **combat/** : moteur de combat (ordre des tours, résolution des actions, morts, suivi des ennemis vaincus)

- **class_savemanager.py** : système de sauvegarde et de chargement

- **display.py** : affichage des combats, de l’inventaire, des quêtes et de la progression


## Lancer le jeu

Prérequis : **Python 3**

Lancement : depuis le dossier du projet, exécuter python **main.py**.

Une **version exécutable** peut également être disponible dans les Releases du dépôt.


## Auteur : Lisa S.