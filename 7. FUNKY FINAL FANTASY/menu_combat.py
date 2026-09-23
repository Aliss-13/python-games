from display import display_equipment, display_inventory
from display import section, separator, LIGHT_PINK, RESET, RED

from inventory.inventory import equip_from_inventory, use_item, sell_item

from skills.class_skillcontext import SkillContext
from skills.skill_engine import execute_skill
from skills.skills import get_target_name, COST_TYPES

# =================================================== GAMESTATE MENUS ===================================================

def menu_inventory(game):

    while True:

        separator()

        print("Choisir un personnage :")
        print()

        for index, character in enumerate(game.player_team, start=1):
            print(f"[{index}] {character.name}")

        print("[0] Retour")
        print(f"💰 = {game.gold} pièces d'or")

        choix = input("> ")

        if choix == "0":
            return

        if choix.isdigit():

            index = int(choix) - 1

            if 0 <= index < len(game.player_team):

                menu_character_inventory(
                    game,
                    game.player_team[index]
                )

            else:
                print("Personnage invalide.")

        else:
            print("Choix invalide.")


def menu_character_inventory(game, character):
    display_equipment(character)
    while True:
        
        display_inventory(game.inventory)
        print("")
        print("[1] Équiper")
        print("[2] Utiliser objet")
        print("[3] Vendre objet")
        print("[4] Retour")

        choix = input("> ")

        if choix == "1":
            equip_from_inventory(character, game.inventory)

        elif choix == "2":
            use_item(game.player_team, game.inventory)

        elif choix == "3":
            display_inventory(game.inventory)

            try:
                choix = int(input("Objet à vendre : "))
            except ValueError:
                return

            sell_item(game, choix)

        elif choix == "4":
            return

        else:
            print("Choix invalide")

# =================================================== CONTEXT MENUS ===================================================

def menu_skill(context, character):

    print(f"\nActions de {character.name}")

    for i, skill in enumerate(character.skills, start=1):

        if skill.cost_type is None:
            cost_display = "Gratuit"
        else:
            cost_display = f"Coût : {skill.cost} {skill.cost_type}"

        print(
            f"{i}. {LIGHT_PINK}{skill.name:<20}{RESET}"
            f"{cost_display:<20}"
            f"{RED}Cible : {get_target_name(skill)}{RESET}"
        )

    print("0. Retour")


    while True:

        choix = input("> ")

        if not choix.isdigit():
            print("Choix invalide")
            continue

        choix = int(choix)

        if choix == 0:
            return

        if 1 <= choix <= len(character.skills):

            skill = character.skills[choix-1]

            skill_context = SkillContext(
                caster=character,
                allies=context.player_team,
                enemies=context.enemy_team,
                skill=skill
            )

            execute_skill(skill_context)
            return


def menu_tour(context, character):

    while True:

        section(f"{LIGHT_PINK}Actions{RESET}")
        print("[s] Skill")
        print("[i] Inventaire")
        print("[q] Fin du tour")

        choix = input("> ").lower()
       
        # SKILL
        if choix == "s":
            menu_skill(context, character)
            # on reste dans le tour


        # INVENTAIRE
        elif choix == "i":
            menu_character_inventory(context.game, character)
            # on reste dans le tour

        # FIN VOLONTAIRE
        elif choix == "q":
            return

        else:
            print("Choix invalide")


