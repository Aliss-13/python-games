
from data import ITEMS
from ui import header, separator
from sac_a_dos import get_stats


couleurs = {
    "common": "\033[90m",       # gris
    "uncommon": "\033[92m",   # vert
    "rare" : "\033[94m",        # bleu
    "epic": "\033[95m",       # violet
    "legendary" : "\033[93m",   # orange
    "reset" : "\033[0m"
}

RARITY = {
    "common": "commun",
    "uncommon": "inhabituel",
    "rare": "rare",
    "epic": "épique",
    "legendary": "légendaire"
}


SLOTS = {
    "head": "tête",
    "chest": "torse",
    "hands": "mains",
    "legs": "jambes",
    "feet": "pieds",
    "weapon": "arme",
}


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_PINK = "\033[38;5;218m"
PURPLE = "\033[95m"
RESET = "\033[0m"


STAT_NAMES = {
    "power": "Puissance",
    "defense": "Défense",
    "speed": "Vitesse",
    "life_max": "Points de vie",
    "mana_max": "Mana"
}

#--------------------------------------------------- OBJETS ---------------------------------------------------

def display_item(item):

    item_id = item["id"]
    
    if item_id not in ITEMS:
        print("Objet inconnu")
        return

    data_item = ITEMS[item_id]

    rarity = data_item.get("rarity", "common").lower()

    couleur = couleurs.get(rarity, "")
    reset = "\033[0m"

    print(
        f"{couleur}{data_item['name']} ({RARITY[rarity]}){reset} - {DIM}{data_item['description']}{RESET}")

    display_item_details(item)



def display_item_details(item):
    
    if item["type"] == "equipment":

        print(f"Niveau : {item['item_level']}")

        bonus_text = []

        for stat, value in item["bonus"].items():

            stat_name = STAT_NAMES.get(stat, stat)

            bonus_text.append(f"{stat_name} : +{value}")

        print(" - ".join(bonus_text))

    elif item["type"] == "consumable":

        print(f"x{item['quantity']}")


def display_inventory(inventory):
    separator()
    header("Inventaire")

    if not inventory:
        print("Vide.")
        return

    for i, item in enumerate(inventory):
        print(f"{i} - ", end="")
        display_item(item)
    


def display_equipment(character):
    print(f"\nÉquipement de {character.name} :")
    for slot, item_id in character.equipment.items():
        if item_id is None:
            continue
        name = ITEMS[item_id]["name"]
        description = ITEMS[item_id]["description"]
        item = ITEMS[item_id]
        couleur = couleurs.get(item["rarity"], "")
        reset = couleurs["reset"]
        print(f" {slot} → {couleur}{name}{reset} - {DIM}{description}{RESET}")

#--------------------------------------------------- ENNEMIS et LOOTS ---------------------------------------------------

def display_enemy(enemy):
    rarity = enemy.rarity
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]

    print("\n" + " " * 10 + f"{RED}-ENNEMI-{RESET}" + " " * 10 + "\n")
    print(f"{couleur}{enemy.name} ({RARITY[rarity]}){reset}")
    print(f"PV : {enemy.life}")
    print(f"Puissance : {enemy.base_stats['power']}")
    print(f"Vitesse : {enemy.base_stats['speed']}")
    print(f"Défense : {enemy.base_stats['defense']}")


def display_enemy_light(enemy):
    print(f"\n{enemy.name}")
    print(f"PV restants : {enemy.life}")


def display_loot(loot):
    separator()
    print("Butin obtenu :")

    for i, item in enumerate(loot):
        print(f"{i} - ", end="")
        display_item(item)
        
#--------------------------------------------------- PERSONNAGE, EQUIPE ---------------------------------------------------

def display_character(character):

    separator()
    header(f"{character.name}")
    stats = get_stats(character)
    print(f"PV : {character.life}/{stats['life_max']}")

    if character.mana is not None:
        print(f"Mana : {character.mana}/{stats['mana_max']}")
    print(f"Puissance : {stats['power']}") 
    print(f"Vitesse : {stats['speed']}")
    print(f"Défense : {stats['defense']}")


def display_player_team(player_team):

    for character in player_team:
        separator()
        header(f"{character.name}")
        stats = get_stats(character)
        print(f"PV : {character.life}/{stats['life_max']}")
        
        if character.mana is not None:
            print(f"Mana : {character.mana}/{stats['mana_max']}")
        print(f"Puissance : {stats['power']}") 
        print(f"Vitesse : {stats['speed']}")
        print(f"Défense : {stats['defense']}")

        separator()
        display_equipment(character)


def display_combat_state(context):
    separator()
    print("ENNEMIS :")

    for enemy in context.enemy_team:
        if enemy.life > 0:
            display_enemy_light(enemy)

    separator()

