import random
import time

import recipes
from recipes_actions import get_recipe_price, get_recipe_xp

from colors_and_names import RESET, TYPE_META, SCARABAC_NAMES
from garden_ingredients import INGREDIENTS

from progression import level_up, check_victory, update_victory_objectives, register_sale

from sale_dialogues import random_sale_dialogue

from clients import CLIENTS, check_client_event

from clients_queue import WaitingClient

from garden import update_garden

class Witch:

    def __init__(self):
        self.level = 1
        self.xp = 0
        self.money = 0
        self.inventory = {"herbe_lunaire": 0, "champignon_sombre": 0, "poussiere_etoile": 0}

        self.recipes = {}

        self.recipes_upgrades = {item: 0 for item in recipes.ITEMS}

        self.shop_stock = {item_id: {"quantity": 0} for item_id in recipes.ITEMS}

        self.shop_shelves = {item_id: {"quantity": 0, "last_sell": time.time()} for item_id in recipes.ITEMS}

        self.sales = {}

        self.waiting_clients = []

        self.crafted_once = {
        item: False
        for item in recipes.ITEMS
        }

        self.scarabac = {
            "gold_shell": False,
            "left_wing": False,
            "right_wing": False,
            "ruby_eye": False,
            "sharp_mandible": False,
            "mechanical_heart": False
        }

        self.victory_objectives = {
            "craft_all": False,
            "level_20": False,
            "scarabac_complete": False
        }

        self.side_quests = {
            "gringotts": False,
            "dat_ass": False,
            "steve_carrell": False,
            "jeff_bezos": False,
            "severus_snape": False,
            "flitwick": False
        }

        self.has_won = False
       

    def to_dict(self):

        return {
            "level": self.level,
            "xp": self.xp,
            "money": self.money,
            "inventory": self.inventory,
            "recipes": self.recipes,
            "recipes_upgrades": self.recipes_upgrades,
            "shop_stock": self.shop_stock,
            "shop_shelves": self.shop_shelves,
            "sales": self.sales,
            

            "waiting_clients": [waiting.to_dict() for waiting in self.waiting_clients],


            "crafted_once": self.crafted_once,
            "scarabac": self.scarabac,
            "victory_objectives": self.victory_objectives,
            "side_quests": self.side_quests,
            "has_won": self.has_won
        }


    def from_dict(self, data):
        self.level = data.get("level", 1)
        self.xp = data.get("xp", 0)
        self.money = data.get("money", 0)
        self.inventory = data.get("inventory", {})
        self.recipes = data.get("recipes", {})
        self.recipes_upgrades = data.get("recipes_upgrades", {})
        
        # self.shop_stock
        saved_shop_stock = data.get("shop_stock", {})

        self.shop_stock = {
            item_id: {
                "quantity": saved_shop_stock.get(item_id, {}).get("quantity", 0)
                } 
        for item_id in recipes.ITEMS
        }

        # self.shop_shelves
        saved_shop_shelves = data.get("shop_shelves", {})
        default = {"quantity": 0, "last_sell": time.time()}

        self.shop_shelves = {
            item_id: {
            "quantity": saved_shop_shelves.get(item_id, default)["quantity"],
            "last_sell": saved_shop_shelves.get(item_id, default)["last_sell"]
            }
        for item_id in recipes.ITEMS
        }

        # self.sales
        self.sales = data.get("sales", {})


        # self.waiting_clients
        self.waiting_clients = []

        for waiting in data.get("waiting_clients", []):
            client_id = waiting.get("client_id")

            if client_id not in CLIENTS:
                continue

            client = CLIENTS[client_id]

            choice_index = waiting.get("choice_index")

            if choice_index is None or choice_index >= len(client.choices):
                continue

            selected_choice = client.choices[choice_index]

            arrival_time = waiting.get("arrival_time")

            self.waiting_clients.append(
                WaitingClient(
                    client,
                    selected_choice,
                    arrival_time
                )
        )

        
        # self.crafted_once
        saved_crafted_once = data.get("crafted_once", {})
        for item in self.crafted_once:
            if item in saved_crafted_once:
                self.crafted_once[item] = saved_crafted_once[item]
        
        # self.scarabac
        saved_scarabac = data.get("scarabac", {})
        for item in self.scarabac:
            if item in saved_scarabac:
                self.scarabac[item] = saved_scarabac[item]

        # self.victory_objectives
        saved_victory_objectives = data.get("victory_objectives", {})
        for item in self.victory_objectives:
            if item in saved_victory_objectives:
                self.victory_objectives[item] = saved_victory_objectives[item]

        # self.side_quests
        saved_side_quests = data.get("side_quests", {})
        self.side_quests = {k: saved_side_quests.get(k, False) for k in self.side_quests}

        self.has_won = data.get("has_won", False)


#============================= RECOLTE ====================================

def harvest(witch, garden):

        chance = 0.002 + (garden.level *0.02)
        if random.random() < chance:  # exemple : 0.05%
            try_drop_scarabac(witch)

        total = 0
        print(f"Récolte : ")

        for item, data in garden.ingredients.items():

            if data["unlocked"] and data["count"] > 0:
                witch.inventory[item] = witch.inventory.get(item, 0) + data["count"]
                print(f"- {INGREDIENTS[item]['name']} x{data['count']}")

                total += data["count"]
                data["count"] = 0

        if total == 0:
            print("nulle.")


def try_drop_scarabac(witch):
    missing = [k for k, v in witch.scarabac.items() if not v]
   
    if not missing:
        return

    fragment = random.choice(missing)
    witch.scarabac[fragment] = True
    fragment_name = SCARABAC_NAMES.get(fragment, fragment)
    print(f"🪲 Fragment du Scarabac trouvé : {fragment_name} !")
    update_victory_objectives(witch)
    check_victory(witch)

#============================= VENTE ====================================

def auto_sell(witch, garden):
    now = time.time()

    for item_id, data in witch.shop_shelves.items():

        quantity = data["quantity"]
        if quantity <= 0:
            continue

        demand = max(0.1, recipes.ITEMS[item_id]["demand"])
        base_time = 5
        interval = base_time / demand

        if now - data["last_sell"] >= interval:

            data["quantity"] -= 1
            data["last_sell"] = now

            witch.money += get_recipe_price(witch, item_id)
            witch.xp += get_recipe_xp(witch, item_id)
            
            register_sale(witch, [item_id])

            print(f"\nVous avez vendu {recipes.ITEMS[item_id]["name"]} !")
            print(random_sale_dialogue(recipes.ITEMS[item_id]["name"]))
            print(
                f"XP +{get_recipe_xp(witch, item_id)} - "
                f"Argent +{get_recipe_price(witch, item_id)}"
            )

            level_up(witch, garden)

#============================= GAME TICK ====================================

def game_tick(witch, garden):

    update_garden(garden)
    auto_sell(witch, garden)
    check_client_event(witch, garden)

#============================= AFFICHAGE ====================================

def display_inventory(witch):

    print("\n===== INVENTAIRE =====")

    empty = True

    for ingredient, qty in witch.inventory.items():

        if qty > 0:
            print(f"{INGREDIENTS[ingredient]['name']} : {qty}")
            empty = False

    if empty:
        print("Aucun ingrédient.")


def display_shop_stock(witch):

    print("\n===== STOCK ARRIERE-BOUTIQUE =====")

    empty = True

    for item, data in witch.shop_stock.items():

        quantity = data["quantity"]
        if quantity <= 0:
            continue

        item_data = recipes.ITEMS[item]
        meta = TYPE_META.get(item_data["type"], {"icon": "❓", "color": RESET})

        print(
            f"{meta['color']}{item_data['name']}{RESET} "
            f"{meta['icon']} {quantity}"
        )

        empty = False

    if empty:
        print("Aucun article en réserve.")


def display_shop_shelves(witch):

    print("\n===== BOUTIQUE =====")

    empty = True
  
    for item, data in witch.shop_shelves.items():

        quantity = data["quantity"]
        if quantity <= 0:
            continue

        item_data = recipes.ITEMS[item]
        meta = TYPE_META.get(item_data["type"], {"icon": "❓", "color": RESET})

        print(
            f"{meta['color']}{item_data['name']}{RESET} "
            f"{meta['icon']} {quantity}"
        )

        empty = False

    if empty:
        print("Aucun article en vente.")