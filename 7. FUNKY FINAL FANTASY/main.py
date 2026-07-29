import traceback
from ui import header
from display import display_inventory, display_character
from class_savemanager import SaveManager
from class_combatcontext import CombatContext
from debug import debug_level, debug_enemy
from menu import menu_zone

try:
    print("\n• “. ,, .¤° ´¯` • Funky Final Fantasy • ´¯` °¤. ,, . ” •")

    game = SaveManager.load()

    if game:
        print("⌛ Partie chargée.")
        
    else: 
        game = SaveManager.new_game()
        print("🧭 Nouvelle aventure !")

    header(game.current_zone.name)
    print(game.current_zone.description)

    for character in game.player_team:
        display_character(character)

    display_inventory(game.inventory)

    

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





