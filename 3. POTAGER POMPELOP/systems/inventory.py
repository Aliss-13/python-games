from data.data import boutique

RECOLTES = boutique["recoltes"]
ENGRAIS = boutique["engrais"]

def ajouter_item(stock, nom, quantite=1):
    stock[nom] = stock.get(nom, 0) + quantite


def retirer_item(stock, nom, quantite=1):
    if nom not in stock:
        return False

    stock[nom] -= quantite

    if stock[nom] <= 0:
        del stock[nom]

    return True


def afficher_inventaire(state):

    print("Inventaire 🚜 :")

    for i, (nom, quantite) in enumerate(state.joueur.inventaire.items()):
        print(f"{i} - {nom}x{quantite}")
    
    # for i, item in enumerate(inventaire): pour une liste
        # print(f'{i} - {item}')
    
    
