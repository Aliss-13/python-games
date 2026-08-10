from inventory.data import ITEMS
from inventory.item_generator import generate_item
from inventory.apply_item_effect import apply_item_effect
from inventory.class_shop import FOREST_SHOPS

from display import display_item_details

# ----------------------------------------- Ajout, retrait, sélection dans l'inventaire --------------------------------------------------------

def add_item(inventory, item):

    if item["type"] in ["consumable", "base_craft"]:

        for existing in inventory:

            if existing["id"] == item["id"]:
                existing["quantity"] += item.get("quantity", 1)
                return

    inventory.append(item.copy())


def remove_item(inventory, index):
    if not isinstance(index, int):
        print("Index invalide :", index)
        return None

    return inventory.pop(index)


def remove_item_by_id(inventory, item_id, amount=1):

    for item in inventory:

        if item["id"] != item_id:
            continue

        quantity = item.get("quantity", 1)

        if quantity > amount:
            item["quantity"] -= amount
        else:
            inventory.remove(item)

        return True

    return False


def get_item(inventory, choix):

    if not isinstance(choix, int):
        return None
    
    if choix < 0 or choix >= len(inventory):
        return None

    item = inventory[choix]

    if not isinstance(item, dict):
        return None

    return item


def get_item_quantity(inventory, item_id):

    quantity = 0

    for item in inventory:

        if item["id"] == item_id:
            quantity += item.get("quantity", 1)

    return quantity
# ----------------------------------------- Consommables --------------------------------------------------------

def use_item(player_team, inventory):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventory):
        print("Choix invalide.")
        return

    item = get_item(inventory, choix)

    if item is None:
        return

    item_id = item["id"]
    
    if item["type"] in ["equipment", "base_craft"]:
        print("Cet objet n'est pas consommable.")
        return
    
    success = apply_item_effect(player_team, item)

    if success:
        remove_item(inventory, choix)
        print(f"{ITEMS[item_id]["name"]} disparaît de l'inventaire !")

# ----------------------------------------- Statistiques de base + bonus --------------------------------------------------------

def get_item_stats(item):

    data = ITEMS[item["id"]]

    level = item.get("item_level", 1)

    stats = {}

    for stat, value in data["bonus"].items():

        scaling = data.get("scaling", {}).get(stat, 0)

        stats[stat] = value + int(level * scaling)

    return stats
    
# ----------------------------------------- Equipement --------------------------------------------------------

def equip_from_inventory(character, inventory):

    try:
        choix = int(input("Choisir numéro de l'objet :"))
    except ValueError:
        print("Entrée invalide.")
        return

    if choix < 0 or choix >= len(inventory):
        print("Choix invalide.")
        return

    item = get_item(inventory, choix) # objet réel (avec item_level et bonus scalés)

    if item is None:
        return

    if item["type"] in ["consumable", "base_craft"]:
        print("Cet objet ne peut être équipé.")
        return

    if character.character_class not in item.get("character_class", []):
        print("Classe incompatible")
        return

    slot = item["slot"]

    ancien = character.equipment.get(slot)

    if ancien:
        for stat, val in ancien["bonus"].items():
            character.bonus[stat] = character.bonus.get(stat, 0) - val
        inventory.append(ancien.copy())

    character.equipment[slot] = item.copy()

    for stat, val in item["bonus"].items():
        character.bonus[stat] = character.bonus.get(stat, 0) + val

    remove_item(inventory, choix)

    print(f"{character.name} équipe {item['name']}")

# ----------------------------------------- Vente --------------------------------------------------------

def sell_item(game, item_index):

    if item_index < 0 or item_index >= len(game.inventory):
        print("Objet invalide.")
        return

    item = game.inventory[item_index]

    value = ITEMS[item["id"]].get("cost", 0)

    if value <= 0:
        print("Cet objet ne peut pas être vendu.")
        return

    quantity = item.get("quantity", 1)

    if quantity > 1:

        try:
            amount = int(input(f"Combien vendre ? (1-{quantity}) [{value} or / unité] : "))

        except ValueError:
            print("Entrée invalide.")
            return

        if amount < 1 or amount > quantity:
            print("Quantité invalide.")
            return

    else:
        amount = 1

    game.gold += value * amount

    if quantity > amount:
        item["quantity"] -= amount
    else:
        game.inventory.pop(item_index)

    print(
        f"💰 Vous vendez {item['name']} x{amount} "
        f"pour {value * amount} or."
    )

# ----------------------------------------- Boutique --------------------------------------------------------

def menu_shop(game):

    shops = [
        FOREST_SHOPS[shop_id]
        for shop_id in game.unlocked_shops
    ]

    while True:

        print("\n🏪 Boutiques disponibles")

        for i, shop in enumerate(shops, start=1):
            print(f"[{i}] {shop.name}")

        print("[0] Retour")

        choix = input("> ")

        if choix == "0":
            return

        if choix.isdigit():

            index = int(choix) - 1

            if 0 <= index < len(shops):
                open_shop(game, shops[index])


def open_shop(game, shop):
    while True:
        print(f"\n🏪 {shop.name}")
        print(f"Or : {game.gold}\n")

        for i, item_id in enumerate(shop.inventory, start=1): # pour avoir une numérotation qui commence à 1
            item = ITEMS[item_id]
            print(f"[{i}] {display_item_details(item)} - {item['cost']} or")

        print("[0] Retour")

        choice = input("> ")

        if choice == "0":
            return

        if choice.isdigit():

            index = int(choice) - 1 # pour aller avec la numérotation qui commence à 1

            if 0 <= index < len(shop.inventory):

                item_id = shop.inventory[index]

                item = generate_item(
                    item_id,
                    game.current_zone.progress
                )

                price = ITEMS[item_id]["cost"]

                if game.gold >= price:
                    game.gold -= price
                    add_item(game.inventory, item)
                    print(f"Vous achetez {item['name']}.")
                else:
                    print("Pas assez d'or.")

        else:
            print("Choix invalide.")


def unlock_shop(game, shop_id):

    if shop_id not in game.unlocked_shops:

        game.unlocked_shops.append(shop_id)

        print(f"🏪 Nouvelle boutique découverte : {FOREST_SHOPS[shop_id].name}")