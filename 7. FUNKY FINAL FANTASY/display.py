
from data import ITEMS
from class_event import FOREST_EVENTS, get_event_by_flag
from class_enemy import get_enemy_by_id, ENEMIES
from inventory import get_stats, remove_item


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

def separator():
    print("\n" + "-" * 40)

def header(title):
    print("\n" + " " * 10 + f"-{title}-" + " " * 10 + "\n")

def ligne(txt):
    print(f"- {txt}")

def section(title):
    print(f"\n{LIGHT_PINK}--- {title} ---{RESET}")

def input_prompt(txt):
    return input(f"> {txt} ")


def display_discovery(event):

    print("\n📜 Découverte !")
    print(f"🌲 {getattr(event, 'name', '')}")

#--------------------------------------------------- OBJETS ---------------------------------------------------
def display_item_details(item):

    rarity = item.get("rarity", "common").lower()
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]

    name = item["name"]

    if item["type"] == "consumable":

        return (
            f"{couleur}{name} ({RARITY[rarity]}){reset} "
            f"x{item.get('quantity', 1)} - "
            f"{DIM}{item.get('description','')}{RESET}"
        )

    if item["type"] == "equipment":

        bonus_text = []

        for stat, value in item.get("bonus", {}).items():
            bonus_text.append(f"{STAT_NAMES.get(stat, stat)} +{value}")

        bonus = " | ".join(bonus_text)

        return (
            f"{couleur}{name} ({RARITY[rarity]}){reset} "
            f"Niv.{item.get('item_level',1)} "
            f"[{bonus}] - "
            f"{DIM}{item.get('description','')}{RESET}"
        )

    return f"{couleur}{name} ({RARITY[rarity]}){reset}"


def display_inventory(inventory):
    separator()
    header("Inventaire")

    if not inventory:
        print("Vide.")
        return

    for i, item in enumerate(inventory):
        print(f"{i} - {display_item_details(item)}")
    


def display_equipment(character):
    print(f"\n{YELLOW}Équipement de {character.name} :{RESET}")

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

    if not loot:
        print("Butin obtenu : rien.")
        return
    
    print("Butin obtenu :")
    for i, item in enumerate(loot):
        print(f"{i} - {display_item_details(item)}")
        
#--------------------------------------------------- PERSONNAGE, EQUIPE ---------------------------------------------------

def display_character(character):

    section(f"{YELLOW}{character.name}{RESET}")

    stats = get_stats(character)

    if stats['mana_max'] > 0:
        print(f"{CYAN}Mana : {character.mana}/{stats['mana_max']}{RESET}")
    
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

#-------------------------------------- PROGRESSION ZONE : DECOUVERTES, QUETES ET BOSS --------------------------------------

def display_zone_light(zone):
    print(f"============ {zone.name} ============")
    print()
    print(f"    {zone.description}    ")
    print()


def display_zone_progression(zone):

    print(f"============ {zone.name} ============")
    print(f"    {zone.description}    ")
    print()

    print(f"        {BLUE}Progression : {zone.progress}/{zone.boss_progress}{RESET}        ")

    # barre visuelle
    bar_size = 20

    filled = int(bar_size * zone.progress / zone.boss_progress)

    bar = "█" * filled + "." * (bar_size - filled)

    print(f"        {BLUE}{bar}{RESET}        ")

    print()


def display_zone_discoveries(zone):

    if zone.flags:
        print(f"\n📜 {YELLOW}Découvertes :{RESET}")
        print("")
    
        for flag in zone.flags:
    
            event = get_event_by_flag(flag, FOREST_EVENTS)
    
            if event:
                print(f"- {event.name}")
            else:
                print(f"- Découverte inconnue ({flag})")


def display_zone_quests(game):

    print(f"\n📜 {YELLOW}Quêtes actives :{RESET}")
    print("")

    if game.active_quests:

        for quest in game.active_quests:

            print(f"{LIGHT_PINK}{quest.name}{RESET}")

            print(f"{quest.description}")

            if quest.objective_type == "kill_each":

                completed = sum(
                                1
                                for count in quest.target_progress.values()
                                if count >= quest.amount
                            )

                print(
                    f"Progression : "
                    f"{completed}/{len(quest.target_progress)}"
                )

                for enemy_id, count in quest.target_progress.items():
                    enemy = get_enemy_by_id(enemy_id, ENEMIES)
                    symbole = "✔️" if count >= quest.amount else "❌"
                    print(f"{symbole} {enemy.name}")

            else:
                print(
                    f"Progression : "
                    f"{quest.progress}/{quest.amount}"
                )

            print(f"XP gagnée : {quest.reward_xp} XP")

            display_zone_quests_loots(quest)
            print()
    else:
        print("- Aucune quête active")


def display_zone_quests_loots(quest):

    print("Loots :")
    
    for item_id in quest.reward_items:
    
        data = ITEMS.get(item_id)
    
        if not data:
            print(f"- Objet inconnu ({item_id})")
            continue
    
        rarity = data.get("rarity", "common").lower()
        couleur = couleurs.get(rarity, "")
        reset = couleurs["reset"]
    
        print(
            f"{couleur}{data['name']} ({RARITY[rarity]}){reset} - "
            f"{data.get('description', '')}"
            )
    
        if data.get("bonus"):
            print("Caractéristiques :")
    
            for stat in data["bonus"]:
                print(f"- {STAT_NAMES.get(stat, stat)}")
    
            print(
                f"{YELLOW}⚠️ Les valeurs seront révélées "
                f"après validation de la quête.{RESET}"
            )
    
        print("")


def display_zone_defeated_enemies(zone):

    print(f"\n⚔️ {RED} Ennemis vaincus :{RESET}")

    if zone.enemy_kills:

        for enemy_id, count in zone.enemy_kills.items():
            enemy = get_enemy_by_id(enemy_id, ENEMIES) # récupère l'objet "ennemi" grâce à son id.
            print(f"- {enemy.name} : {count}")

    else:
        print("- Aucun ennemi vaincu")

    print("")



def display_zone_boss_status(zone):

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


def display_zone_progress(zone, game):
    display_zone_progression(zone)
    display_zone_discoveries(zone)
    display_zone_quests(game)
    display_zone_defeated_enemies(zone)
    display_zone_boss_status(zone)

#--------------------------------------------------- VENTE ITEMS ---------------------------------------------------

def sell_item(game):

    display_inventory(game.inventory)

    try:
        choix = int(input("Objet à vendre : "))

    except ValueError:
        return


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