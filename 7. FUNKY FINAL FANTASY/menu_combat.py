from display import display_equipment, display_inventory
from inventory import equip_from_inventory, use_item
from class_skill import get_target_name
from display import section, separator, sell_item
from class_skillcontext import SkillContext
from skill_engine import execute_skill


def menu_inventory(context):

    while True:

        separator()

        print("Choisir un personnage :")
        print()

        for index, character in enumerate(context.player_team, start=1):
            print(f"[{index}] {character.name}")

        print("[0] Retour")

        choix = input("> ")

        if choix == "0":
            return

        if choix.isdigit():

            index = int(choix) - 1

            if 0 <= index < len(context.player_team):

                character_inventory_menu(
                    context,
                    context.player_team[index]
                )

            else:
                print("Personnage invalide.")

        else:
            print("Choix invalide.")


def character_inventory_menu(context, character):
    display_equipment(character)
    while True:
        
        display_inventory(context.inventory)
        print("")
        print("[1] Équiper")
        print("[2] Utiliser objet")
        print("[3] Vendre objet")
        print("[4] Retour")

        choix = input("> ")

        if choix == "1":
            equip_from_inventory(character, context.inventory)

        elif choix == "2":
            use_item(context.player_team, context.inventory)

        elif choix == "3":
            display_inventory(context.inventory)

            try:
                choix = int(input("Objet à vendre : "))
            except ValueError:
                return

            sell_item(context.inventory, choix)

        elif choix == "4":
            return

        else:
            print("Choix invalide")


def menu_skill(context, character):

    print(f"\nActions de {character.name}")

    for i, skill in enumerate(character.skills, start=1):
        print(
            f"{i}. {skill.name:<25} "
            f"Coût : {skill.cost} "
            f"Cible : {get_target_name(skill)}"
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

        section("Actions")
        print("[s] Skill")
        print("[i] Inventaire")
        print("[q] Fin du tour")

        choix = input("> ").lower()
       
        # SKILL
        if choix == "s":
            menu_skill(context, character)
            return

     
        # INVENTAIRE
        elif choix == "i":
            character_inventory_menu(context, character)
            # on reste dans le tour

        # FIN VOLONTAIRE
        elif choix == "q":
            return

        else:
            print("Choix invalide")


