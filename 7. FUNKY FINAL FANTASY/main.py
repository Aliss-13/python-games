import traceback
from ui import header
from data import inventory
from display import display_inventory, display_character
from combat import combat
from save import load_game, new_game
from class_zone import ZONES
from exploration import explore_zone


try:
    print("\n• “. ,, .¤° ´¯` • Funky Final Fantasy • ´¯` °¤. ,, . ” •")

    result = load_game()

    if result:
        player_team, inventory, enemy_pool = result
        

    else: 
        player_team, inventory, enemy_pool = new_game()

        print("🧭 Nouvelle aventure !")
        
        for character in player_team:
            display_character(character)

        display_inventory(inventory)

        current_zone = ZONES[0]
        header(current_zone.name)
        print(current_zone.description)  

        enemy = explore_zone(current_zone)

    combat(player_team, [enemy], inventory)

except Exception as e:
    traceback.print_exc()
    input("Appuie sur entrée pour quitter")