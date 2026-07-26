import traceback
from ui import header
from data import inventory
from display import display_inventory, display_character
from class_savemanager import SaveManager
from class_combatcontext import CombatContext
from class_gamestate import GameState
from menu import menu_zone


try:
    print("\n• “. ,, .¤° ´¯` • Funky Final Fantasy • ´¯` °¤. ,, . ” •")

    load_result = SaveManager.load()

    if load_result:
        player_team, enemy_team, inventory, zone = load_result
        
    else: 
        player_team, enemy_team, inventory, zone = SaveManager.new_game()
        print("🧭 Nouvelle aventure !")

    header(zone.name)
    print(zone.description)

    for character in player_team:
        display_character(character)

    display_inventory(inventory)

    game = GameState(
        player_team,
        enemy_team,
        inventory,
        zone
    )

    context = CombatContext(
        player_team=game.player_team,
        enemy_team=game.enemy_team,
        inventory=game.inventory,
        zone=game.current_zone,
        game=game
    )

    menu_zone(game, context)
        
except Exception as e:
    traceback.print_exc()
    input("Appuie sur entrée pour quitter")