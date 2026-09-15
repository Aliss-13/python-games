# progression.py
# │
# ├── give_client_reward()
# ├── level_up()
# ├── update_victory()
# ├── check_victory()
# ├── crafted_everything()
# └── éventuellement des fonctions de déblocage futures

from colors_and_names import YELLOW, RESET, SCARABAC_NAMES
import recipes
from garden import improve_garden


def level_up(witch, garden):
    while witch.xp >= witch.level * 50:
        witch.xp -= witch.level * 50
        witch.level += 1
        improve_garden(garden)
        check_victory(witch)
        print(f"Vous passez au niveau {witch.level} ! ")



def gain_rewards(witch, garden, result):
    witch.money += result.money
    witch.xp += result.xp

    for item in result.items:
        witch.inventory[item] = witch.inventory.get(item, 0) + 1

    for recipe in result.recipes:
        if not witch.recipes.get(recipe):
            witch.recipes[recipe] = True
            print(f"✧.*{recipes.ITEMS[recipe]['name']}✧.*")

    level_up(witch, garden)
    update_victory(witch)


# ==================================== OBJECTIFS DE VICTOIRE ====================================================

def update_victory(witch):
    update_craft_objective(witch)
    update_level_objective(witch)
    update_scarabac_objective(witch)

def update_craft_objective(witch):
    witch.victory_objectives["craft_all"] = crafted_everything(witch)

def update_level_objective(witch):
    witch.victory_objectives["level_20"] = witch.level >= 20

def update_scarabac_objective(witch):
    witch.victory_objectives["scarabac_complete"] = all(witch.scarabac.values())


def check_victory(witch):

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


def display_scarabac_parts(witch):
    print("\n🪲 Scarabac :")
    print("")
    print("Le Scarabac est un artefact extrêmement puissant dont plus personne ne sait se servir... " \
    "Mais ça ferait tellement classe sur la devanture de la boutique...")
    print("")

    for part, owned in witch.scarabac.items():
               
        status = "✔" if owned else "❌"
        name = SCARABAC_NAMES.get(part, part)

        print(f"{status} {name}")
        
    
        
def display_remaining_recipes(witch):
    print("\n💫 Crafts :")
    print("")

    for recipe, crafted in witch.crafted_once.items():
        status = "✔" if crafted else "❌"
        name = recipes.ITEMS[recipe]["name"]
        print(f"{status} {name}")


def crafted_everything(witch):
    return all(witch.crafted_once.values())


def register_sale(witch, items):

    if isinstance(items, str):
        items = [items]

    for item in items:
        witch.sales[item] = witch.sales.get(item, 0) + 1

    check_all(witch)


def display_victory(witch):

    print("\n🏆 OBJECTIFS DE VICTOIRE\n")

    print(f"[{'✔' if witch.victory_objectives['craft_all'] else ' '}] Crafter toutes les recettes")
    print(f"[{'✔' if witch.victory_objectives['level_20'] else ' '}] Atteindre le niveau 20")

    scarabac_done = sum(witch.scarabac.values())
    scarabac_total = len(witch.scarabac)

    print(f"[{'✔' if witch.victory_objectives['scarabac_complete'] else ' '}] Scarabac ({scarabac_done}/{scarabac_total})")


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
        for item_id, data in recipes.ITEMS.items()
        if "irs" in data["tags"]
        )
    },

    "dat_ass" : {
    "name": "La Jean-Yves Lafesse",
    "description": "Vendre 2 exemplaires de chaque item contenant une référence de fesses.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in recipes.ITEMS.items()
        if "dat_ass" in data["tags"]
        )
    },

    "steve_carrell" : {
    "name": "La Steve Carrell",
    "description": "Vendre 2 exemplaires de chaque item portant un nom corporate.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 2
        for item_id, data in recipes.ITEMS.items()
        if "corporate" in data["tags"]
        )
    },

    "severus_snape" : {
    "name": "La Severus Rogue",
    "description": "Vendre 1 exemplaire de chaque potion.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 1
        for item_id, data in recipes.ITEMS.items()
        if data["type"] == "potion"
        )
    },

    "flitwick" : {
    "name": "La Flitwick",
    "description": "Vendre 1 exemplaire de chaque sortilège.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 1
        for item_id, data in recipes.ITEMS.items()
        if data["type"] == "magic_scroll"
        )
    }, 

    "jeff_bezos" : {
    "name": "La Jeff Bezos",
    "description": "Vendre 1 exemplaire de chaque grimoire.",
    "condition": lambda witch: all(
        witch.sales.get(item_id, 0) >= 1
        for item_id, data in recipes.ITEMS.items()
        if data["type"] == "spell_book"
        )
    }
}


def check_all(witch):
    for quest_id, quest in SIDE_QUESTS.items():
        witch.side_quests[quest_id] = quest["condition"](witch)


