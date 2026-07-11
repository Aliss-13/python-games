import time
from colors_and_names import RESET, DIM, TYPE_META
from recipes import ITEMS
from garden_ingredients import INGREDIENTS
from clients import check_waiting_clients, serve_waiting_clients
from progression import check_victory, update_victory


#============================= CRAFTING ====================================

def available_crafts(witch, garden):
    print("===== Que voulez-vous fabriquer ? =====")

    available = []

    for item, data in ITEMS.items():

        if data["level_required"] is not None:

            if witch.level >= data["level_required"]:
                available.append(item)

        else:
            if witch.recipes.get(item):
                available.append(item)
    
    # affichage
    for i, item_id in enumerate(available, start=1):

        item = ITEMS[item_id]
        
        meta = TYPE_META.get(item["type"], {"icon": "❓", "color": RESET})

        ingredients = []

        for ingredient, quantity in item["ingredients"].items():
            ingredients.append(f"{INGREDIENTS[ingredient]['name']} x{quantity}")

        print(
            f"[{i}] {meta['color']}{item['name']}{RESET} "
            f"{meta['icon']} {DIM}{', '.join(ingredients)}{RESET}"
        )

    print(f"[0] Retour")

    # choix utilisateur (UNE seule fois)
    try:
        choix = int(input("> "))

        if choix == 0:
            return

        if choix < 1 or choix > len(available):
            print("Entrée inexistante")
            return
    
    except ValueError:
        print("Entrée invalide")
        return

    item_selected = available[choix - 1]

    if not can_craft(witch, item_selected):
        print("Pas assez d'ingrédients")
        return
    
    craft(witch, garden, item_selected)


def can_craft(witch, item_name):
    for ingredient, qty in ITEMS[item_name]["ingredients"].items():
        if witch.inventory.get(ingredient, 0) < qty:
            return False
    return True


def craft(witch, garden, item_name):

    recipe = ITEMS[item_name]["ingredients"]

    for ingredient, quantity in recipe.items():
        if witch.inventory.get(ingredient, 0) < quantity:
            print("Pas assez d'ingrédients")
            return False

    for ingredient, quantity in recipe.items():
        witch.inventory[ingredient] -= quantity

    witch.crafted_once[item_name] = True

    update_victory(witch)
    check_victory(witch)

    print(f"Vous avez créé {ITEMS[item_name]['name']} !")
    

    stock_gestion(witch, item_name)
    
    check_waiting_clients(witch)
    serve_waiting_clients(witch, garden, item_name)

    return True


def stock_gestion(witch, item_name):
    print("\nOù souhaitez-vous ranger cet objet ?")
    print("[1] Le mettre en réserve 📦")
    print("[2] Le mettre en rayon 🛒")

    while True:
        choice = input("> ")

        if choice == "1":

            if item_name not in witch.shop_stock:
                witch.shop_stock.setdefault(item_name, {"quantity": 0})

            witch.shop_stock[item_name]["quantity"] += 1

            print(f"Mise en réserve ➝ {ITEMS[item_name]['name']}.")
            break

        elif choice == "2":

            if item_name not in witch.shop_shelves:
                witch.shop_shelves.setdefault(item_name,{"quantity": 0, "last_sell": time.time()})

            witch.shop_shelves[item_name]["quantity"] += 1

            print(f"Mise en rayon ➝ {ITEMS[item_name]['name']}.")
            break

        else:
            print("Choix invalide.")


def recipe_unlocked(witch, item_id):

    data = ITEMS[item_id]

    if data["level_required"] is not None:
        return witch.level >= data["level_required"]

    return witch.recipes.get(item_id, False)

#============================= AMELIORER ====================================

def upgrade_recipe_menu(witch):

    available = []

    # Recherche des recettes améliorables
    for item_id, data in ITEMS.items():

        # Recettes débloquées par niveau
        if data["level_required"] is not None:

            if witch.level >= data["level_required"]:
                available.append(item_id)

        # Recettes débloquées par les clients/quêtes
        else:

            if witch.recipes.get(item_id):
                available.append(item_id)


    if not available:
        print("Aucune recette disponible à améliorer.")
        return

    
    # Affichage
    print("\n===== AMÉLIORATION DES RECETTES =====")

    for i, item_id in enumerate(available, start=1):

        item = ITEMS[item_id]

        meta = TYPE_META.get(
            item["type"],
            {"icon": "❓", "color": RESET}
        )

        print(
            f"[{i}] "
            f"{meta['color']}{item['name']}{RESET} "
            f"{meta['icon']} "
            f"{DIM}(niveau {witch.recipes_upgrades[item_id]}){RESET} "
            f"- coût : {get_upgrade_cost(witch, item_id)} pièces"
        )

    print("[0] Retour")


    # Choix joueur
    try:

        choix = int(input("> "))

        if choix == 0:
            return

        if choix < 1 or choix > len(available):
            print("Entrée inexistante.")
            return

    except ValueError:
        print("Entrée invalide.")
        return


    # Amélioration
    item_selected = available[choix - 1]
    upgrade_recipe(witch, item_selected)


def upgrade_recipe(witch, item):

    data = ITEMS[item]

    cost = get_upgrade_cost(witch, item)

    if witch.money < cost:
        print("Pas assez d'argent.")
        return

    witch.money -= cost

    witch.recipes_upgrades[item] += 1

    print(
        f"{data['name']} : niveau "
        f"{witch.recipes_upgrades[item]} !"
    )
    

def get_recipe_price(witch, item):

    base_price = ITEMS[item]["price"]
    upgrade = witch.recipes_upgrades.get(item, 0)

    return base_price + (upgrade * 10)


def get_recipe_xp(witch, item):

    base_xp = ITEMS[item]["xp"]
    upgrade = witch.recipes_upgrades.get(item, 0)

    return base_xp + (upgrade * 10)


def get_upgrade_cost(witch, item):

    base_cost = ITEMS[item]["upgrade_cost"]
    upgrade = witch.recipes_upgrades.get(item, 0)

    return int(base_cost * (1.5 ** upgrade))