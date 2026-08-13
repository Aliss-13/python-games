# Funky Final Fantasy


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


## Lancer le jeu : python main.py


## Auteur : Lisa S.