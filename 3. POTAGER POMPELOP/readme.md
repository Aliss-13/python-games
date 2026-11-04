# 🥕 POTAGER POMPÉLOP v1.0

### 🌱 Présentation

**Potager Pompélop** est un jeu de gestion de potager développé en Python, jouable directement dans le terminal.

Le joueur cultive des légumes, surveille leur croissance et organise ses récoltes pour satisfaire les commandes de ses clients.

Chaque commande honorée permet de gagner de l'argent et de l'expérience, afin de débloquer de nouvelles cultures, acheter des améliorations et développer progressivement son exploitation.

**Objectif :** transformer un modeste carré de terre en un potager prospère ! 🌻

## 🎮 Fonctionnalités

- 🌱 **Culture de légumes** : acheter des graines, les planter et attendre leur croissance avant de les récolter.
- 📦 **Gestion des commandes** : satisfaire les demandes des clients en utilisant les légumes récoltés.
- 💰 **Économie du potager** : gagner des pièces et de l'expérience grâce aux commandes.
- 🏆 **Progression** : monter en niveau et débloquer de nouvelles variétés de graines.
- 🛒 **Boutique** : acheter des graines, des engrais et des améliorations pour développer son exploitation.
- ⏳ **Gestion du temps** : faire progresser les cultures au fil des tours de jeu.
- 💾 **Sauvegarde JSON** : enregistrer les données de sa partie.

### 🛠️ Compétences techniques

- **Python** : développement d'un jeu de gestion en terminal.
- **Programmation modulaire** : organisation du code en plusieurs fichiers selon leurs responsabilités.
- **Gestion d'état** : suivi des ressources, des cultures et de la progression du joueur.
- **Manipulation de structures de données** : utilisation de listes et de dictionnaires.
- **Persistance des données** : sérialisation des informations de jeu au format JSON.

### 🚀 Perspectives d'évolution

Potager Pompélop est un premier prototype de jeu de gestion agricole en Python.

Une refonte plus ambitieuse est envisagée à long terme, avec l'objectif d'enrichir les mécaniques de simulation, de développer l'univers du jeu et de mettre en pratique de nouvelles compétences techniques.

Cette version 1.0 constitue la base de ce futur projet.


## 🏗️ Architecture du projet

Le projet repose sur une **architecture modulaire**, permettant de séparer les données, les objets du jeu, la logique métier et l'interface utilisateur.

```text
POTAGER POMPELOP/
│
├── main.py          # Point d'entrée du jeu
│
├── core/            # Moteur du jeu et gestion de l'état
├── data/            # Données et catalogue des graines
├── models/          # Classes représentant les entités
├── systems/         # Mécaniques de jeu
├── ui/              # Interface en terminal
└── utils/           # Utilitaires et sauvegarde
```

Cette organisation facilite la lecture du code, sa maintenance et l'évolution des fonctionnalités.

Elle permet également de distinguer les règles de gestion du jeu de leur affichage dans le terminal.


## 🚀 Installation et lancement

### Prérequis

- Python 3 installé sur votre ordinateur.
- Un terminal (PowerShell, Invite de commandes, etc.).

Aucune bibliothèque externe n'est nécessaire.

### Installation

**1. Cloner le dépôt GitHub**

```bash
git clone URL_DU_DEPOT
```

**2. Accéder au dossier du projet**

```bash
cd NOM_DU_DEPOT
```

**3. Lancer le jeu**

```bash
python main.py
```

### 🎮 Comment jouer ?

Le jeu se déroule entièrement dans le terminal.

Suivez les menus pour acheter des graines, cultiver vos légumes, gérer votre inventaire et honorer les commandes.

La progression de votre exploitation est enregistrée au format JSON et rechargée au démarrage du jeu.