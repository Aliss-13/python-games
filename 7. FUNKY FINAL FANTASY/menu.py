from sac_a_dos import equip_from_inventory, use_item
from ui import section
from class_skill import SKILL_FUNCTIONS, get_target_name
from display import display_equipment, display_inventory

def menu_inventory(character, player_team, inventory):
    display_equipment(character)
    while True:
        
        display_inventory(inventory)
        print("")
        print("[1] Équiper")
        print("[2] Utiliser objet")
        print("[3] Retour")

        choix = input("> ")

        if choix == "1":
            equip_from_inventory(character, inventory)

        elif choix == "2":
            use_item(player_team, inventory)

        elif choix == "3":
            return

        else:
            print("Choix invalide")

def menu_tour(character, player_team, enemies, inventory):

    while True:

        section("Actions")
        print("[s] Skill")
        print("[i] Inventaire")
        print("[q] Fin du tour")

        choix = input("> ").lower()


        # =====================
        # SKILL
        # =====================
        if choix == "s":
            menu_skill(character, player_team, enemies)
            return "fin_tour"

        # =====================
        # INVENTAIRE
        # =====================
        elif choix == "i":
            menu_inventory(character, player_team, inventory)
            # on reste dans le tour

        # =====================
        # FIN VOLONTAIRE
        # =====================
        elif choix == "q":
            return "fin_tour"

        else:
            print("Choix invalide")


def menu_skill(character, allies, enemies):

    print(f"\nActions de {character.name}")

    for i, skill in enumerate(character.skills, start=1):
        print(f"{i}. {skill.name:<25} Coût : {skill.cost} - Cible {get_target_name(skill)}")
   
    print("0. Retour")

    while True:

        choix = input("> ")

        if choix.isdigit():

            choix = int(choix)

            if choix == 0:
                return None

            skill = character.skills[choix - 1]

            action = SKILL_FUNCTIONS.get(skill.id)

            if action is None:
                print(f"Compétence inconnue : {skill.id}")
                return

            action(character, allies, enemies, skill)
            return

        print("Choix invalide.")