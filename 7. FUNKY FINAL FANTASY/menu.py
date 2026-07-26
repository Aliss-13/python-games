from ui import section
from display import display_player_team
from menu_combat import menu_inventory
from combat import combat
from class_savemanager import SaveManager
from class_combatcontext import CombatContext

def menu_zone(game, context):

    context = CombatContext(
        player_team=game.player_team,
        enemy_team=game.enemy_team,
        inventory=game.inventory,
        zone=game.current_zone,
        game=game
    )

    while True:

        section("Actions")
        print("[1] Explorer")
        print("[2] Equipe")
        print("[3] Inventaire")
        print("[4] Sauvegarder")
        print("[5] Quitter")

        choix = input("> ").lower()

        if choix == "1":
            combat(game)

        elif choix == "2":
            display_player_team(game.player_team)

        elif choix == "3":
            menu_inventory(context)

        elif choix == "4":
            SaveManager.save(game)

        elif choix == "5":
            print("À bientôt.")
            return

        else:
            print("Choix invalide")