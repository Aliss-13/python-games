import systems.shop as shop
from data.data import boutique
from core.event_handler import handle_events

RECOLTES = boutique["recoltes"]
ENGRAIS = boutique["engrais"]

SHOP_OK = "ok"
SHOP_NOT_ENOUGH_MONEY = "not_enough_money"
SHOP_INVALID_ITEM = "invalid_item"


def afficher_boutique_ui(state):
    while True:
        print("\n1 Récoltes | 2 Engrais | 3 Agrandir potager | 4 Quitter")

        choix = input("> ")

        if choix == "1":
            acheter_recolte_ui(state)
        elif choix == "2":
            acheter_engrais_ui(state)
        elif choix == "3":
            agrandir_potager_ui(state)
        elif choix == "4":
            break


def acheter_recolte_ui(state):
    for i, item in enumerate(RECOLTES):
        print(f"{i} - {item['nom']} ({item['prix']} pièces)")

    try:
        choix = int(input("> "))
    except ValueError:
        return

    result = shop.acheter_recolte(state, choix)
    handle_events(result["events"], state)

    item = RECOLTES[choix] if 0 <= choix < len(RECOLTES) else None

    if result == SHOP_OK:
        print(f"{item['nom']} ajouté au garde-manger.")

    elif result == SHOP_NOT_ENOUGH_MONEY:
        print("Pas assez de pièces.")

    elif result == SHOP_INVALID_ITEM:
        print("Choix invalide.")
 

def acheter_engrais_ui(state):

    for i, item in enumerate(ENGRAIS):
        print(f"{i} - {item['nom']} - {item['bonus']} temps - ({item['prix']} pièces)")

    try:
        choix = int(input("> "))
    except ValueError:
        return

    result = shop.acheter_engrais(state, choix)
    handle_events(result["events"], state)

    if result == SHOP_OK:
        item = ENGRAIS[choix]
        print(f"{item['nom']} ajouté à l'inventaire.")

    elif result == SHOP_NOT_ENOUGH_MONEY:
        print("Pas assez de pièces.")

    elif result == SHOP_INVALID_ITEM:
        print("Choix invalide.")

   
def agrandir_potager_ui(state):

    result = shop.agrandir_potager(state)
    handle_events(result["events"], state)

    if result == SHOP_OK:
        print(f"Potager agrandi ! Nouvelle capacité : {state.joueur.potager_max}")
    
    elif result == SHOP_NOT_ENOUGH_MONEY:
        print("Pas assez de pièces.")
    