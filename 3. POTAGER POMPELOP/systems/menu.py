from core.game import tour_suivant
import ui.farming_ui as farming_ui
import ui.commands_ui as commands_ui
from ui.shop_ui import afficher_boutique_ui
from systems.inventory import afficher_inventaire
from utils.save import safe_load_json, sauvegarder


def afficher_9(state):
    
    while True:
        print("\n1 Sauvegarder | 2 Charger | 3 Retour")
        choix = input("> ")
            
        if choix == "1":
            sauvegarder(state)
        elif choix == "2":
            safe_load_json()
        elif choix == "3":
            return


def menu(state):
    actions = {
        "1": [farming_ui.planter_multiple_ui],
        "2": [lambda s: tour_suivant(s)],
        "3": [farming_ui.afficher_potager_ui],
        "4": [farming_ui.afficher_garde_manger_ui, farming_ui.afficher_bourse_ui, afficher_inventaire, farming_ui.utiliser_objet_ui],
        "5": [farming_ui.recolter_tout_ui],
        "6": [farming_ui.recolter_ui],
        "7": [farming_ui.afficher_garde_manger_ui, commands_ui.liste_commandes, commands_ui.valider_commande_ui],
        "8": [afficher_boutique_ui],
        "9": [afficher_9],
    }
     
    while True:
        print("\n1 Planter | 2 Temps | 3 Voir potager | 4 Garde-manger 🧺 - Bourse 💰 - Inventaire 🚜 | 5 Récolter tout ")
        print("| 6 Récolter | 7 Remplir commandes | 8 Boutique | 9 Sauvegarder - Charger | 10 Quitter")
        choix = input("> ")

        if choix == "10":
            break

        action = actions.get(choix)

        if action:
            for f in action:
                f(state)
        else:
            print("Choix invalide")