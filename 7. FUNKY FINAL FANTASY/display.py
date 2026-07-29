
from data import ITEMS
from class_event import FOREST_EVENTS, get_event_by_flag
from class_enemy import get_enemy_by_id, ENEMIES
from ui import header, separator, section
from inventory import get_stats


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
    "head": "Tête",
    "chest": "Torse",
    "hands": "Mains",
    "legs": "Jambes",
    "feet": "Pieds",
    "weapon": "Arme",
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
    "life_max": "PV",
    "mana_max": "Mana"
}


def display_discovery(event):

    print("\n📜 Découverte !")
    print(f"🌲 {getattr(event, 'name', '')}")

#--------------------------------------------------- OBJETS ---------------------------------------------------

def display_item_details(item):

    item_id = item["id"]

    # Les infos fixes viennent de ITEMS
    data = ITEMS[item_id]

    rarity = item.get("rarity", data.get("rarity", "common")).lower()
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]

    name = item.get("name", data["name"])
    description = data.get("description", "")

    if item["type"] == "equipment":
        
        print(
            f"{couleur}{name} ({RARITY[rarity]}){reset} "
            f"{DIM}Niv.{item.get('item_level', 1)}{RESET} - "
            f"{DIM}{description}{RESET}")

        bonus_text = []

        for stat, value in item.get("bonus", {}).items():
            bonus_text.append(f"{STAT_NAMES.get(stat, stat)} +{value}")

        if bonus_text:
            print("   " + " | ".join(bonus_text))


    elif item["type"] == "consumable":
        print(
            f"{couleur}{name} ({RARITY[rarity]}){reset} "
            f"x{item['quantity']}")


def display_inventory(inventory):
    separator()
    header("Inventaire")

    if not inventory:
        print("Vide.")
        return

    for i, item in enumerate(inventory):
        print(f"{i} - ", end="")
        display_item_details(item)
    


def display_equipment(character):
    print(f"\nÉquipement de {character.name} :")

    for slot, item in character.equipment.items():

        if item is None:
            continue

        print(f"{SLOTS.get(slot, slot)} → ", end="")
        display_item_details(item)

#--------------------------------------------------- ENNEMIS et LOOTS ---------------------------------------------------

def display_enemy(enemy):
    rarity = enemy.rarity
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]
    stats = get_stats(enemy)

    print("\n" + " " * 10 + f"{RED}-ENNEMI-{RESET}" + " " * 10 + "\n")

    print(f"{couleur}{enemy.name} ({RARITY[rarity]}){reset}")

    if stats['mana_max'] > 0:
        print(f"Mana : {enemy.mana}/{stats['mana_max']}")

    print(
        f"PV : {enemy.life}/{stats['life_max']} - "
        f"Puissance : {enemy.base_stats['power']} - "
        f"Vitesse : {enemy.base_stats['speed']} - "
        f"Défense : {enemy.base_stats['defense']}")


def display_enemy_light(enemy):

    section(f"{enemy.name}")

    stats = get_stats(enemy)

    if stats['mana_max'] > 0:
        print(f"Mana : {enemy.mana}/{stats['mana_max']}")

    print(
        f"PV restants : {enemy.life}/{stats['life_max']} - "
        f"Puissance : {enemy.base_stats['power']} - "
        f"Vitesse : {enemy.base_stats['speed']} - "
        f"Défense : {enemy.base_stats['defense']}")
        
    print("")

    if enemy.effects:
    
        print("Effets actifs :")
    
        for i, effect in enumerate(enemy.effects, start=1):
            print(
                f"{i} - {effect.name} "
                f"({effect.duration} tours)"
            )
    
    else:
        print("Aucun effet actif.")

    print("")


def display_loot(loot):

    print("Butin obtenu :")

    for i, item in enumerate(loot):
        print(f"{i} - ", end="")
        display_item_details(item)
        
#--------------------------------------------------- PERSONNAGE, EQUIPE ---------------------------------------------------

def display_character(character):

    section(f"{character.name}")

    stats = get_stats(character)

    if stats['mana_max'] > 0:
        print(f"Mana : {character.mana}/{stats['mana_max']}")
    
    print(
        f"PV : {character.life}/{stats['life_max']} - "
        f"Puissance : {character.base_stats['power']} - "
        f"Vitesse : {character.base_stats['speed']} - "
        f"Défense : {character.base_stats['defense']}")
    
    print("")

    if character.effects:

        print("Effets actifs :")

        for i, effect in enumerate(character.effects, start=1):
            print(
                f"{i} - {effect.name} "
                f"({effect.duration} tours)"
            )

    else:
        print("Aucun effet actif.")


def display_player_team(player_team):

    for character in player_team:
        display_character(character)
        separator()
        display_equipment(character)


def display_combat_state(context):
    separator()
    print("ENNEMIS :")

    for enemy in context.enemy_team:
        if enemy.life > 0:
            display_enemy_light(enemy)

    separator()


def display_boss_name(enemy_id):

    enemy = get_enemy_by_id(enemy_id, ENEMIES)

    if enemy:
        return enemy.name

    return "Inconnu"


def display_zone_progress(zone, game):

    separator()

    print(f"🌲 {zone.name}")
    print(zone.description)

    print()

    print(f"Progression : {zone.progress}/{zone.boss_progress}")

    # barre visuelle
    bar_size = 20

    filled = int(bar_size * zone.progress / zone.boss_progress)

    bar = "█" * filled + "-" * (bar_size - filled)

    print(f"[{bar}]")

    print()

    # ------------------------------------------- découvertes

    if zone.flags:
        print("\n📜 Découvertes :")

    for flag in zone.flags:

        event = get_event_by_flag(flag, FOREST_EVENTS)

        if event:
            print(f"- {event.name}")
        else:
            print(f"- Découverte inconnue ({flag})")

    # -------------------------------------------- quêtes

    print("\n📜 Quêtes actives :")

    if game.active_quests:

        for quest in game.active_quests:

            print(f"🌲 {quest.name}")
            print(f"   {quest.description}")
            print(
                f"   Progression : "
                f"{quest.progress}/{quest.amount}"
            )

            print(
                f"   Récompense : "
                f"{quest.reward_xp} XP"
            )

            if quest.reward_items:
                print(
                    f"   Objets : {', '.join(quest.reward_items)}"
                )

    else:
        print("- Aucune quête active")

    # ------------------------------------------ ennemis vaincus

    print("\n⚔️ Ennemis vaincus :")

    if zone.enemy_kills:

        for enemy_id, count in zone.enemy_kills.items():
            enemy = get_enemy_by_id(enemy_id, ENEMIES) # récupère l'objet "ennemi" grâce à son id.
            print(f"- {enemy.name} : {count}")

    else:
        print("- Aucun ennemi vaincu")

    print("")

    # ------------------------------------------- sous-boss, boss

    if zone.sub_boss_unlocked:
        sub_boss = display_boss_name(zone.sub_boss)

        if zone.sub_boss_defeated:
            print(f"🥈 Sous-boss : {sub_boss} vaincu")
        else:
            print(f"🥈 Sous-boss disponible : {sub_boss}")

    else:
        print("🥈 Sous-boss : inconnu")

    print("")


    if zone.boss_unlocked:
        boss = display_boss_name(zone.boss)

        if zone.boss_defeated:
            print(f"🥇 Boss : {boss} vaincu")
        else:
            print(f"🥇 Boss disponible : {boss}")

    else:
        print("🥇 Boss : inconnu")

    print("")