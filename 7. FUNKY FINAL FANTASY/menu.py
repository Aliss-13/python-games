from ui import section
from display import display_player_team
from combat import combat, generate_enemy_team, menu_inventory
from class_zone import explore
from class_savemanager import SaveManager

def menu_zone(character, player_team, enemy_team, inventory, current_zone):

    while True:

        section("Actions")
        print("[1] Explorer")
        print("[2] Equipe")
        print("[3] Inventaire")
        print("[4] Sauvegarder")
        print("[5] Quitter")

        choix = input("> ").lower()

        if choix == "1":
            result = explore(current_zone)

            if result and result["type"] == "combat":
                enemies = generate_enemy_team(current_zone, result["event"])
                combat(player_team, enemies, inventory, current_zone)

        elif choix == "2":
            display_player_team(player_team)

        elif choix == "3":
            menu_inventory(character, player_team, inventory)

        elif choix == "4":
            SaveManager.save(player_team, enemy_team, inventory)

        else:
            print("Choix invalide")