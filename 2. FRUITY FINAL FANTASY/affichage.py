import data
import ui

def afficher_item(item):

    if isinstance(item, str):
        item_id = item

    elif isinstance(item, dict):
        item_id = item.get("item")

    else:
        print("Item invalide :", item)
        return

    # 🔒 protection CRUCIALE
    if not item_id:
        print("Item sans ID :", item)
        return

    if item_id not in data.objets:
        print("Item inconnu :", item_id)
        return

    data_item = data.objets[item_id]

    rarete = data_item.get("rarete", "commun").lower()
    couleur = data.couleurs.get(rarete, "")
    reset = "\033[0m"
    print(f"{couleur}{item_id} ({rarete}){reset}")

def afficher_inventaire(inventaire):

    ui.header("Inventaire")
    if not inventaire:
        print("Vide.")
        return
    for i, item in enumerate(inventaire):
        print(f"{i} - ", end="")
        afficher_item(item)

def afficher_equipement(personnage):
    print(f"\nÉquipement de {personnage['nom']} :")
    for slot, item_id in personnage["equipement"].items():
        if item_id is None:
            continue
        item = data.objets[item_id]
        couleur = data.couleurs.get(item["rarete"], "\033[0m")
        reset = data.couleurs["reset"]
        print(f" {slot} → {couleur}{item_id}{reset}")

def afficher_ennemi(ennemi):
    rarete = ennemi.get("rarete", "commun")
    couleur = data.couleurs.get(rarete, "")
    reset = data.couleurs["reset"]

    ui.header("ENNEMI")
    print(f"{couleur}{ennemi['nom']} ({rarete}){reset}")
    print(f"PV : {ennemi['vie']}")
    print(f"Puissance : {ennemi['puissance']}")

def afficher_loot(loot):
    ui.separator()
    print("Butin obtenu :")

    for i, item in enumerate(loot):
        print(f"{i} - ", end="")
        afficher_item(item)
        