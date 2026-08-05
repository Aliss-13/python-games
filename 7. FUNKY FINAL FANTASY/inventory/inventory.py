from inventory.data import ITEMS
from inventory.item_generator import generate_item
from inventory.apply_item_effect import apply_item_effect
from inventory.class_shop import FOREST_SHOPS
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


def get_item(inventory, choix):

    if not isinstance(choix, int):
        return None
    
    if choix < 0 or choix >= len(inventory):
        return None

    item = inventory[choix]

    if not isinstance(item, dict):
        return None

    return item

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

    if character.character_class not in item["class"]:
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

def sell_item(game, choix):

    if choix < 0 or choix >= len(game.inventory):
        return


    item = game.inventory[choix]

    value = ITEMS[item["id"]].get("cost", 0)


    if value == 0:
        print("Cet objet ne peut pas être vendu.")
        return


    quantity = item.get("quantity", 1)

    gain = value * quantity

    game.gold += gain

    remove_item(game.inventory, choix)

    print(
        f"💰 Vous vendez {item['name']} "
        f"pour {gain} pièces."
    )

# ----------------------------------------- Boutique --------------------------------------------------------

def shop_menu(game, merchant):
    while True:
        print(f"\n🏪 {merchant.name}")
        print(f"Or : {game.gold}\n")

        for i, item_id in enumerate(merchant.inventory):
            item = ITEMS[item_id]
            print(f"[{i}] {item['name']} - {item['cost']} or")

        print("[v] Vendre des objets")
        print("[0] Retour")

        choix = input("> ")

        item = generate_item(item_id, game.current_zone.progress)

        if game.gold >= ITEMS[item_id]["cost"]:
            game.gold -= ITEMS[item_id]["cost"]
            add_item(game.inventory, item)
            print(f"Vous achetez {item['name']}.")
        else:
            print("Pas assez d'or.")


def unlock_shop(game, shop_id):

    if shop_id not in game.discovered_shops:

        game.discovered_shops.append(shop_id)

        print(f"🏪 Nouvelle boutique découverte : {FOREST_SHOPS[shop_id].name}")