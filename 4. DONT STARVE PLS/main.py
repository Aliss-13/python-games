from player import Player
from world import World
import menu
import display
import traceback
import save

def main():

    print("\n===== DO NOT STARVE PLS =====")
    print("\n« Tu vas mourir ici mon petit pote... »")
    print("")
   
    player = Player()
    world = World()

    save.load_game(player, world)
    display.display_stats(player, world)
    running = True
    
    while running:

        try:
            
            running = menu.menu(player, world)
            
            if not running:
                break
            
        except Exception:
            traceback.print_exc()
            input("Erreur détectée. Appuie sur entrée pour quitter")
            break


if __name__ == "__main__":
    main()