from data import ITEMS, couleurs, DIM, RESET, RARITY, RED
from ui import header, separator

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
        f"{couleur}{data_item['name']} ({RARITY[rarity]}){reset} x{item['quantity']} - {DIM}{data_item['description']}{RESET}")
    
    
    if item["type"] == "equipment":
        print(f" Niveau : {item['item_level']}")

        for stat, value in item["bonus"].items():
            print(f" {stat} : +{value}")


def display_inventory(inventory):
    separator()
    header("Inventaire")

    if not inventory:
        print("Vide.")
        return
    
    for item in inventory:
        display_item(item)


def display_equipment(character):
    print(f"\nÉquipement de {character.name} :")
    for slot, item_id in character.equipment.items():
        if item_id is None:
            continue
        name = ITEMS[item_id]["name"]
        description = ITEMS[item_id]["description"]
        item = ITEMS[item_id]
        couleur = couleurs.get(item["rarity"], "\033[0m")
        reset = couleurs["reset"]
        print(f" {slot} → {couleur}{name}{reset} - {DIM}{description}{RESET}")


def display_opponent(opponent):
    rarity = opponent.rarity
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]

    print("\n" + " " * 10 + f"{RED}-ENNEMI-{RESET}" + " " * 10 + "\n")
    print(f"{couleur}{opponent.name} ({RARITY[rarity]}){reset}")
    print(f"PV : {opponent.life}")
    print(f"Puissance : {opponent.base_stats["power"]}")
    print(f"Vitesse : {opponent.base_stats["speed"]}")
    print(f"Défense : {opponent.base_stats["defense"]}")


def display_opponent_light(opponent):
    print(f"\n{opponent.name}")
    print(f"PV restants : {opponent.life}")


def display_loot(loot):
    separator()
    print("Butin obtenu :")

    for i, item in enumerate(loot):
        print(f"{i} - ", end="")
        display_item(item)
        

def display_character(character):

    separator()
    header(f"{character.name}")
    stats = character.base_stats
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
        stats = character.base_stats
        print(f"PV : {character.life}/{stats['life_max']}")
        
        if character.mana is not None:
            print(f"Mana : {character.mana}/{stats['mana_max']}")
        print(f"Puissance : {stats['power']}") 
        print(f"Vitesse : {stats['speed']}")
        print(f"Défense : {stats['defense']}")

        separator()
        display_equipment(character)

