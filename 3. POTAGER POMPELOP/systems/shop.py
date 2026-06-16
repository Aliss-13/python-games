from data.data import boutique
from systems.inventory import ajouter_item
RECOLTES = boutique["recoltes"]
ENGRAIS = boutique["engrais"]


SHOP_OK = "ok"
SHOP_NOT_ENOUGH_MONEY = "not_enough_money"
SHOP_INVALID_ITEM = "invalid_item"


def acheter_recolte(state, choix):

    if choix < 0 or choix >= len(RECOLTES):
        return {"status": SHOP_INVALID_ITEM, "events": []}

    item = RECOLTES[choix]

    if not state.joueur.payer(item["prix"]):
        return {"status": SHOP_NOT_ENOUGH_MONEY, "events": []}

    state.joueur.ajouter_recolte(item["nom"])

    return {
        "status": SHOP_OK,
        "events": [
            {
                "type": "item_bought",
                "item": item["nom"],
                "price": item["prix"]
            }
        ]
    }


def acheter_engrais(state, choix):
     
    if choix < 0 or choix >= len(ENGRAIS):
        return {"status": SHOP_INVALID_ITEM, "events": []}
    
    item = ENGRAIS[choix]

    if not state.joueur.payer(item["prix"]):
        return {"status": SHOP_NOT_ENOUGH_MONEY, "events": []}

    ajouter_item(state.joueur.inventaire, item["nom"])
    return {
        "status": SHOP_OK,
        "events": [
            {
                "type": "item_bought",
                "item": item["nom"],
                "price": item["prix"]
            }
        ]
    }


def agrandir_potager(state):

    prix = state.joueur.potager_max * 10

    if not state.joueur.payer(prix):
        return {"status": SHOP_NOT_ENOUGH_MONEY, "events": []}

    state.joueur.potager_max += 3
    return {
        "status": SHOP_OK,
        "events": [
            {
                "type": "potager_upgraded",
                "new_size": state.joueur.potager_max,
                "cost": prix
            }
        ]
    }