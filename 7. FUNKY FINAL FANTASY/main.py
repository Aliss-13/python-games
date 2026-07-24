import traceback
from ui import header
from data import inventory
from display import display_inventory, display_character
from class_savemanager import SaveManager
from class_zone import ZONES
from menu import menu_zone


try:
    print("\n• “. ,, .¤° ´¯` • Funky Final Fantasy • ´¯` °¤. ,, . ” •")

    result = SaveManager.load()

    if result:
        player_team, enemy_team, inventory = result
        

    else: 
        player_team, enemy_team, inventory = SaveManager.new_game()

        print("🧭 Nouvelle aventure !")
        
        for character in player_team:
            display_character(character)

        display_inventory(inventory)

        current_zone = ZONES[0]
        header(current_zone.name)
        print(current_zone.description)  

    menu_zone(character, player_team, enemy_team, inventory, current_zone)

except Exception as e:
    traceback.print_exc()
    input("Appuie sur entrée pour quitter")