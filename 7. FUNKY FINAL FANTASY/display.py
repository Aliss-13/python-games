from inventory.data import ITEMS

from events.class_event import FOREST_EVENTS, get_event_by_flag

from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import get_enemy_by_id
from protagonists.get_stats import get_stats 


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

CHARACTER_CLASS = {
    "hand_to_hand": "Corps à corps",
    "magic": "Magie"
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
YELLOW = "\033[33m"
LIGHT_YELLOW = "\033[93m"
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
    print(f"\n--- {title} ---")

def input_prompt(txt):
    return input(f"> {txt} ")

#--------------------------------------------------- OBJETS ---------------------------------------------------
def display_item_details(item):

    rarity = item.get("rarity", "common").lower()
    couleur = couleurs.get(rarity, "")
    reset = couleurs["reset"]

    name = item["name"]

    if item["type"] in ["consumable", "base_craft"]:

        return (
            f"{couleur}{name} ({RARITY[rarity]}){reset} "
            f"x{item.get('quantity', 1)} - "
            f"{DIM}{item.get('description','')}{RESET}"
        )

    if item["type"] == "equipment":

        classes = item.get("character_class", [])

        if isinstance(classes, list):
            class_name = ", ".join(CHARACTER_CLASS.get(c, c) for c in classes)

        else:
            class_name = CHARACTER_CLASS.get(classes, classes)

        bonus_text = []

        for stat, value in item.get("bonus", {}).items():
            bonus_text.append(f"{STAT_NAMES.get(stat, stat)} +{value}")

        bonus = ", ".join(bonus_text)

        return (
            f"{couleur}{name}{reset} "
            f"- {class_name} "
            f"- Niv.{item.get('item_level',1)} - "
            f"{bonus} - "
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
    print(f"\nÉquipement de {character.name} :")

    for slot, item in character.equipment.items():

        if item is None:
            continue

        print(f"{SLOTS.get(slot, slot)} → {display_item_details(item)}", end="")
        print()
        

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

    section(f"{LIGHT_YELLOW}{character.name}{RESET}")

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

    print(f"        {BLUE}Progression : {zone.progress}/{zone.total_progress}{RESET}        ")

    # barre visuelle
    bar_size = 35

    filled = int(bar_size * zone.progress / zone.boss_progress)

    bar = "█" * filled + "." * (bar_size - filled)

    print(f"{BLUE}{bar}{RESET}")

    print()


def display_completed_quests(game):

    print(f"\n📖 {GREEN}Quêtes terminées :{RESET}\n")

    if not game.completed_quests:
        print("- Aucune quête terminée")
        return

    for quest in game.completed_quests:
        print(f"✔ {GREEN}{quest.name}{RESET}")


def display_zone_discoveries(zone):

    if zone.flags:
        print(f"\n📜 {LIGHT_YELLOW}Découvertes :{RESET}")
        print("")
    
        for flag in zone.flags:
    
            event = get_event_by_flag(flag, FOREST_EVENTS)
    
            if event:
                print(f"- {event.name}")
            else:
                print(f"- Découverte inconnue ({flag})")


def display_zone_quests(game):

    print(f"\n📜 {LIGHT_YELLOW}Quêtes actives :{RESET}")
    print("")

    if game.active_quests:

        for quest in game.active_quests:

            print(f"{LIGHT_PINK}{quest.name}{RESET}")

            print(f"{quest.description}")

            if quest.quest_type == "kill_each":

                progress = quest.get_progress(game)

                completed = sum(1 for objective, count in progress.items() if count >= quest.objectives[objective])

                print(f"Progression : {completed}/{len(quest.objectives)}")
    
                for objective, count in progress.items():
                    required = quest.objectives[objective]
                    symbole = "✔️" if count >= required else "❌"
                    name = get_objective_name(objective)
                    print(f"{symbole} {name} {count}/{required}")


            elif quest.quest_type == "collect_items":

                progress = quest.get_progress(game)

                completed = sum(1 for objective, count in progress.items() if count >= quest.objectives[objective])

                print(f"Progression : {completed}/{len(quest.objectives)}")
                
                for objective, count in progress.items():
                    required = quest.objectives[objective]
                    symbole = "✔️" if count >= required else "❌"
                    name = get_objective_name(objective)
                    print(f"{symbole} {name} {count}/{required}")


            elif quest.quest_type == "discover_each":

                completed = sum(1 for objective, count in quest.objectives_progress.items() if count >= quest.objectives[objective])

                print(f"Progression : {completed}/{len(quest.objectives)}")
                
                for objective, count in quest.objectives_progress.items():
                    required = quest.objectives[objective]
                    symbole = "✔️" if count >= required else "❌"
                    name = get_objective_name(objective)
                    print(f"{symbole} {name} {count}/{required}")

                    
            elif quest.quest_type == "kill_group":

                print(f"Progression : {quest.progress}/{quest.objectives['required']}")

            print(f"Expérience : {quest.reward_xp} XP")

            display_zone_quests_loots(quest)

            print()


def display_zone_quests_loots(quest):

    if quest.reward_items == []:
        print()

    else:
        print("")
        print("Gratification matérielle :")


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
                f"{LIGHT_YELLOW}⚠️ Les valeurs seront révélées "
                f"après validation de la quête.{RESET}"
            )


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
    display_completed_quests(game)
    display_zone_discoveries(zone)
    display_zone_quests(game)
    display_zone_defeated_enemies(zone)
    display_zone_boss_status(zone)


def get_objective_name(objective_id):

    # objet
    if objective_id in ITEMS:
        return ITEMS[objective_id]["name"]

    # découverte / événement
    event = get_event_by_flag(objective_id, FOREST_EVENTS)
    if event:
        return event.name

    # ennemi
    enemy = get_enemy_by_id(objective_id, ENEMIES)
    if enemy:
        return enemy.name

    # secours
    return objective_id


