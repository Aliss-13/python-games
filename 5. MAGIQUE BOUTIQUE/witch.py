import random
import time
from garden import INGREDIENTS
from garden import Garden, garden_levels
garden = Garden(garden_levels)


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_PINK = "\033[38;5;218m"
PURPLE = "\033[95m"
RESET = "\033[0m"


TYPE_META = {
    "potion": {"icon": "🫙", "color": "\033[92m"},
    "magic_scroll": {"icon": "📜", "color": "\033[93m"},
    "spell_book": {"icon": "📖", "color": "\033[95m"}
}


SCARABAC_NAMES = {
    "gold_shell": "Coquille dorée",
    "left_wing": "Aile gauche",
    "right_wing": "Aile droite",
    "ruby_eye": "Œil rubis",
    "sharp_mandible": "Mandibule acérée",
    "mechanical_heart": "Cœur mécanique"
}

class Witch:

    def __init__(self):
        self.level = 1
        self.xp = 0
        self.money = 0
        self.inventory = {"herbe_lunaire": 0, "champignon_sombre": 0, "poussiere_etoile": 0}

        self.shop_stock = {
            "item_id": {
            "quantity": 0,
            "last_sell": time.time()
            }
        }

        self.sales = {}

        self.crafted_once = {
        item: False
        for item in ITEMS
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
            "shop_stock": self.shop_stock,
            "sales": self.sales,
            "crafted_once": self.crafted_once,
            "scarabac": self.scarabac,
            "victory_objectives": self.victory_objectives,
            "side_quests": self.side_quests
        }


    def from_dict(self, data):
        self.level = data.get("level", 1)
        self.xp = data.get("xp", 0)
        self.money = data.get("money", 0)
        self.inventory = data.get("inventory", {})

        # self.shop_stock
        saved_shop_stock = data.get("shop_stock", {})
        default = {"quantity": 0, "last_sell": time.time()}

        self.shop_stock = {
            item_id: {
            "quantity": saved_shop_stock.get(item_id, default)["quantity"],
            "last_sell": saved_shop_stock.get(item_id, default)["last_sell"]
            }
        for item_id in ITEMS
        }

        # self.sales
        self.sales = data.get("sales", {})
        
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


def level_up(witch, garden):
    while witch.xp >= witch.level * 10:
        witch.xp -= witch.level * 10
        witch.level += 1
        garden.improve_garden()
        check_victory(witch)
        print(f"Vous passez au niveau {witch.level} ! ")

# ==================================== DATA ====================================================

ITEMS = {

    #===================== POTIONS ============================

    "healing_potion": {
        "name": "Potion de vie", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1},
        "level_required": 1,
        "demand": 0.9,
        "price": 10, 
        "xp": 5,
        "upgrade_level": 0,
        "upgrade_cost": 50
    },


    "mana_potion": {
        "name": "Potion de mana", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 1, "champignon_sombre": 2},
        "level_required": 1,
        "demand": 0.9,
        "price": 12, 
        "xp": 6,
        "upgrade_level": 0,
        "upgrade_cost": 50
    },


    "love_potion": {
        "name": "Philtre d'amour", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "poussiere_etoile": 1},
        "level_required": 2,
        "demand": 0.8,
        "price": 25, 
        "xp": 15,
        "upgrade_level": 0,
        "upgrade_cost": 60
    },


    "empowerment": {
        "name": "Enpouvoirment", 
        "type": "potion",
        "tags": ["corporate"],
        "ingredients": {"ecorce_ancienne": 4, "eau_enchantee": 2, "croc_feroce": 4},
        "level_required": 3,
        "demand": 0.9,
        "price": 30, 
        "xp": 20,
        "upgrade_level": 0,
        "upgrade_cost": 70
    },


    "polyjuice": {
        "name": "Polynectar", 
        "type": "potion",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 2, "croc_feroce": 1},
        "level_required": 4,
        "demand": 0.6,
        "price": 40, 
        "xp": 25,
        "upgrade_level": 0,
        "upgrade_cost": 80
    },


    "bbl": {
        "name": "Brazilian Butt Lift", 
        "type": "potion",
        "tags": ["dat_ass"],
        "ingredients": {"champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 2, "croc_feroce": 1, "pierre_noire": 2},
        "level_required": 6,
        "demand": 0.8,
        "price": 60, 
        "xp": 40,
        "upgrade_level": 0,
        "upgrade_cost": 100
    },


    #===================== SORTS ============================
    
    "ass_worms": {
        "name": "Gratte-cul", 
        "type": "magic_scroll",
        "tags": ["dat_ass"],
        "ingredients": {"herbe_lunaire": 3, "champignon_sombre": 2},
        "level_required": 1,
        "demand": 0.8,
        "price": 15, 
        "xp": 10,
        "upgrade_level": 0,
        "upgrade_cost": 50
    }, 


    "pebble_in_shoe": {
        "name": "Petit caillou dans chaussure", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2},
        "level_required": 2,
        "demand": 0.9,
        "price": 20, 
        "xp": 15,
        "upgrade_level": 0,
        "upgrade_cost": 60
    }, 


    "hr_optimization": {
        "name": "Optimisation des ressources humaines", 
        "type": "magic_scroll",
        "tags": ["corporate"],
        "ingredients": {"herbe_lunaire": 4, "champignon_sombre": 1, "ecorce_ancienne": 2, "eau_enchantee": 1},
        "level_required": 2,
        "demand": 0.7,
        "price": 22, 
        "xp": 17,
        "upgrade_level": 0,
        "upgrade_cost": 60
    }, 


    "knock_pinky": {
        "name": "Pan le petit orteil", 
        "type": "magic_scroll",
        "tags": [],
        "ingredients": {"herbe_lunaire": 4, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 2},
        "level_required": 3,
        "demand": 0.7,
        "price": 25, 
        "xp": 20,
        "upgrade_level": 0,
        "upgrade_cost": 70
    }, 


    "flatulences" : {
        "name": "Flatulences", 
        "type": "magic_scroll", 
        "tags": ["dat_ass"],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 1, "ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 1},
        "level_required": 4,
        "demand": 0.5,
        "price": 45, 
        "xp": 30,
        "upgrade_level": 0,
        "upgrade_cost": 80
    },


    "tax_audit" : {
        "name": "Contrôle fiscal", 
        "type": "magic_scroll",
        "tags": ["irs"],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 1, "bezoard": 2, "ecaille_dragon": 2},
        "level_required": 7,
        "demand": 0.8,
        "price": 80, 
        "xp": 60,
        "upgrade_level": 0,
        "upgrade_cost": 120
    },


    #===================== GRIMOIRES ============================

    "murphys_laws": {
        "name": "Les Lois de Murphy", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3},
        "level_required": 1,
        "demand": 0.5,
        "price": 18, 
        "xp": 12,
        "upgrade_level": 0,
        "upgrade_cost": 50
    },


    "cakes_and_politics": {
        "name": "Cakes et politique", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 6},
        "level_required": 3,
        "demand": 0.8,
        "price": 30, 
        "xp": 30,
        "upgrade_level": 0,
        "upgrade_cost": 70
    },


    "tax_haven_from_hell_to_hell_yeah": {
        "name": "Paradis fiscal : de l'enfer au nirvana", 
        "type": "spell_book",
        "tags": ["irs"],
        "ingredients": {"herbe_lunaire": 2, "champignon_sombre": 3, "ecorce_ancienne": 2, "eau_enchantee": 6, "aile_de_fee": 3},
        "level_required": 4,
        "demand": 0.8,
        "price": 40, 
        "xp": 40,
        "upgrade_level": 0,
        "upgrade_cost": 80
    },


    "sexy_djinns_and_pentagrams": {
        "name": "Djinns sexy et pentagrammes", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"eau_enchantee": 4, "aile_de_fee": 3, "pierre_noire": 3, "aconit": 2},
        "level_required": 5,
        "demand": 0.7,
        "price": 60, 
        "xp": 45,
        "upgrade_level": 0,
        "upgrade_cost": 100
    },


    "agile": {
        "name": "La Méthode à Gilles", 
        "type": "spell_book",
        "tags": ["corporate"],
        "ingredients": {"poussiere_etoile": 2, "ecorce_ancienne": 5, "eau_enchantee": 4, "pierre_noire": 3, "aconit": 5},
        "level_required": 6,
        "demand": 0.6,
        "price": 70, 
        "xp": 50,
        "upgrade_level": 0,
        "upgrade_cost": 110
    }, 

    
    "the_devils_best_breakfast_recipes": {
        "name": "Les petits déj d'enfer du Diable", 
        "type": "spell_book",
        "tags": [],
        "ingredients": {"ecorce_ancienne": 1, "eau_enchantee": 4, "aile_de_fee": 3, "croc_feroce": 3, "bezoard": 2, "ecaille_dragon": 3},
        "level_required": 7, 
        "demand": 0.9,
        "price": 90, 
        "xp": 70,
        "upgrade_level": 0,
        "upgrade_cost": 120
    }
}


crafted_once = {
    item: False
    for item in ITEMS
}


#============================= RECOLTE ====================================

def harvest(witch, garden):

        chance = 0.09 + (garden.level *0.02)
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
    update_victory(witch)
    check_victory(witch)

#============================= CRAFTING ====================================

def available_crafts(witch):
    print("===== Que voulez-vous fabriquer ? =====")

    available_items = []

    for item, data in ITEMS.items():
        if witch.level >= data["level_required"]:
            available_items.append(item)
    
    # affichage
    for i, item_id in enumerate(available_items, start=1):

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

        if choix < 1 or choix > len(available_items):
            print("Entrée inexistante")
            return
    
    except ValueError:
        print("Entrée invalide")
        return

    item_selected = available_items[choix - 1]

    if not can_craft(witch, item_selected):
        print("Pas assez d'ingrédients")
        return
    
    craft(witch, item_selected)


def can_craft(witch, item_name):
    for ingredient, qty in ITEMS[item_name]["ingredients"].items():
        if witch.inventory.get(ingredient, 0) < qty:
            return False
    return True


def craft(witch, item_name):

    recipe = ITEMS[item_name]["ingredients"]

    for ingredient, quantity in recipe.items():
        if witch.inventory.get(ingredient, 0) < quantity:
            print("Pas assez d'ingrédients")
            return False

    for ingredient, quantity in recipe.items():
        witch.inventory[ingredient] -= quantity

    if item_name not in witch.shop_stock:
        witch.shop_stock[item_name] = {
            "quantity": 0,
            "last_sell": time.time()
        }

    witch.shop_stock[item_name]["quantity"] += 1

    witch.crafted_once[item_name] = True

    update_victory(witch)
    check_victory(witch)

    print(f"Vous avez créé {ITEMS[item_name]['name']} !")
    return True


def crafted_everything(witch):
    return all(witch.crafted_once.values())


#============================= VENTE ====================================

def auto_sell(witch, garden):
    now = time.time()

    for item_id, data in witch.shop_stock.items():

        quantity = data["quantity"]
        if quantity <= 0:
            continue

        demand = max(0.1, ITEMS[item_id]["demand"])
        base_time = 5
        interval = base_time / demand

        if now - data["last_sell"] >= interval:

            data["quantity"] -= 1
            data["last_sell"] = now

            witch.money += ITEMS[item_id]["price"]
            witch.xp += ITEMS[item_id]["xp"]
            witch.sales[item_id] = witch.sales.get(item_id, 0) + 1

            print(
                f"Vous vendez {ITEMS[item_id]['name']} ! "
                f"XP +{ITEMS[item_id]['xp']} - "
                f"Argent +{ITEMS[item_id]['price']}"
            )

            level_up(witch, garden)
            check_all(witch)

#============================= AMELIORER ====================================

def upgrade_recipe_menu(witch):
    
    available = []

    for item, data in ITEMS.items():
        if witch.level >= data["level_required"]:
            available.append(item)

    for i, item_id in enumerate(available, start=1):

        item = ITEMS[item_id]
        meta = TYPE_META.get(item["type"], {"icon": "❓", "color": RESET})

        print(
            f"[{i}] "
            f"{meta['color']}{item['name']}{RESET} "
            f"{meta['icon']} "
            f"{DIM}(niveau {item['upgrade_level']}){RESET} "
            f"- coût : {item['upgrade_cost']} pièces"
        )

    print(f"[0] Retour")

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
    upgrade_recipe(witch, item_selected)


def upgrade_recipe(witch, item):

    cost = ITEMS[item]["upgrade_cost"]

    if witch.money < cost:
        print("Pas assez d'argent.")
        return

    witch.money -= cost

    ITEMS[item]["upgrade_level"] += 1

    ITEMS[item]["price"] += 10
    ITEMS[item]["xp"] += 10

    ITEMS[item]["upgrade_cost"] = int(cost * 1.5)

    print(
        f"{ITEMS[item]['name']} : niveau "
        f"{ITEMS[item]['upgrade_level']} !"
    )


def game_tick(witch, garden):

    garden.update_garden()
    auto_sell(witch, garden)


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

    print("\n===== BOUTIQUE =====")

    empty = True
  
    for item, data in witch.shop_stock.items():

        quantity = data["quantity"]
        if quantity <= 0:
            continue

        item_data = ITEMS[item]
        meta = TYPE_META.get(item_data["type"], {"icon": "❓", "color": RESET})

        print(
            f"{meta['color']}{item_data['name']}{RESET} "
            f"{meta['icon']} {quantity}"
        )

        empty = False

    if empty:
        print("Aucun objet en vente.")


# ==================================== OBJECTIFS DE VICTOIRE ====================================================

def display_scarabac_parts(witch):
    print("\n🪲 Scarabac :")
    print("")
    print("Le Scarabac est un artefact extrêmement puissant dont plus personne ne sait se servir... " \
    "Mais ça ferait tellement classe sur la devanture de la boutique...")
    print("")

    for part, owned in witch.scarabac.items():
        status = "✔" if owned else "❌"
        if owned:
            name = SCARABAC_NAMES.get(part, part)
            print(f"{status} {name}")
        else:
            name = SCARABAC_NAMES.get(part, part)
            print(f"{status} {name}")
    
        
def display_crafted_recipes(witch):
    print("\n💫 Crafts déjà réalisés :")

    any_crafted = False

    for recipe, crafted in witch.crafted_once.items():
        if crafted:
            name = ITEMS[recipe]["name"]
            print(f"✔ {name}")
            any_crafted = True

    if not any_crafted:
        print("Aucune recette craftée pour le moment.")


def display_victory(witch):

    print("\n🏆 OBJECTIFS DE VICTOIRE\n")

    print(f"[{'✔' if witch.victory_objectives['craft_all'] else ' '}] Crafter toutes les recettes")
    print(f"[{'✔' if witch.victory_objectives['level_20'] else ' '}] Atteindre le niveau 20")

    scarabac_done = sum(witch.scarabac.values())
    scarabac_total = len(witch.scarabac)

    print(f"[{'✔' if witch.victory_objectives['scarabac_complete'] else ' '}] Scarabac ({scarabac_done}/{scarabac_total})")


def update_craft_objective(witch):
    witch.victory_objectives["craft_all"] = all(witch.crafted_once.values())

def update_level_objective(witch):
    witch.victory_objectives["level_20"] = witch.level >= 20

def update_scarabac_objective(witch):
    witch.victory_objectives["scarabac_complete"] = all(witch.scarabac.values())


def update_victory(witch):
    update_craft_objective(witch)
    update_level_objective(witch)
    update_scarabac_objective(witch)


def check_victory(witch):

    if witch.has_won:
        print("\n🏆 VICTOIRE !")
        print("Vous êtes devenue la plus grande sorcière commerçante du BHV !")
        return True

    if (
        all(witch.crafted_once.values())
        and witch.level >= 20
        and all(witch.scarabac.values())
        ):
            witch.has_won = True
            print("\n🏆 VICTOIRE !")
            print("Vous êtes devenue la plus grande sorcière commerçante du BHV !")
            return True

    return False

# ==================================== OBJECTIFS SECONDAIRES ====================================================

def display_side_quests(witch):

    print("\n🏅 HAUTS-FAITS\n")

    for quest_id, quest in SIDE_QUESTS.items():
        print(f"[{'✔' if witch.side_quests.get(quest_id, False) else ' '}] "
              f"{YELLOW}{quest['name']}{RESET} - {quest['description']}")
    

SIDE_QUESTS = {

    "gringotts" : {
    "name": "La Gringotts",
    "description": "Vendre 2 exemplaires de chaque item contenant une référence à la fiscalité.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if "irs" in data["tags"]
        )
    },

    "dat_ass" : {
    "name": "La Jean-Yves Lafesse",
    "description": "Vendre 2 exemplaires de chaque item contenant une référence de fesses.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if "dat_ass" in data["tags"]
        )
    },

    "steve_carrell" : {
    "name": "La Steve Carrell",
    "description": "Vendre 2 exemplaires de chaque item portant un nom corporate.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if "corporate" in data["tags"]
        )
    },

    "severus_snape" : {
    "name": "La Severus Rogue",
    "description": "Vendre 1 exemplaire de chaque potion.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if data["type"] == "potion"
        )
    },

    "flitwick" : {
    "name": "La Flitwick",
    "description": "Vendre 1 exemplaire de chaque sortilège.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if data["type"] == "magic_scroll"
        )
    }, 

    "jeff_bezos" : {
    "name": "La Jeff Bezos",
    "description": "Vendre 1 exemplaire de chaque grimoire.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in ITEMS.items()
        if data["type"] == "spell_book"
        )
    }
}


def check_all(witch):
    for quest_id, quest in SIDE_QUESTS.items():
        witch.side_quests[quest_id] = quest["condition"](witch)