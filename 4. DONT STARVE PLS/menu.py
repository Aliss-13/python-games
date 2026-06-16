import display
import save
import buildings
import food

def menu_construire(player):
    while True:
        display.display_inventaire(player)
        print("[1] Structures")
        print("[2] Outils")
        print("[3] Vêtements")
        print("[4] Tire toi de là...")
        print("[5] Retour")

        choix = input("> ").lower()

        if choix == "1":
            buildings.menu_build(player)

        elif choix == "2":
            buildings.menu_craft(player)

        elif choix == "3":
            buildings.menu_sew(player)

        elif choix == "4":
            display.display_inventaire(player)
            display.display_food(player)
            display.display_flying_dutchman_parts(player)
            buildings.menu_build_flying_dutchman(player)

        elif choix == "5":
            return

        else:
            print("Choix invalide")
            return


def menu_manger(player):
        display.display_food(player)
        food.menu_eat(player)
        display.display_bars_simple(player)
    

def menu_map(player, world):
    while True:
        print("[1] Afficher la carte")
        print("[2] Explorer les environs...")
        print("[3] Explorer une nouvelle zone")
        print("[4] Se déplacer sur une zone")
        print("[5] Retour")

        choix = input("> ").lower()
    
        if choix == "1":
            display.display_map(world)

        elif choix == "2":
            world.search_flying_dutchman_parts(player)
            display.display_bars_simple(player)
    
        elif choix == "3":
            world.explore_area(player)
            display.display_bars_simple(player)

        elif choix == "4":
            print("Zones connues :", world.explored_areas)
            new_area = input("> ")

            if new_area not in world.explored_areas:
                print("Zone inconnue.")
            else:
                world.move_player(player, new_area)
                display.display_bars_simple(player)

        elif choix == "5":
            return

        else:
            print("Choix invalide")
            return


def enhance_basic_resources(player):
    while True:
        display.display_inventaire(player)
        display.display_food(player)
        print("[1] Cuire 🥩")
        print("[2] Affiner 🧀")
        print("[3] Tresser 🪢")
        print("[4] Tisser 🟩")
        print("[5] Retour")

        choix = input("> ").lower()

        if choix == "1":
            player.cook_food()
        elif choix == "2":
            player.cheese_making()
        elif choix == "3":
            player.braid_rope()
        elif choix == "4":
            player.make_cloth()
        elif choix == "5":
            return

        else:
            print("Choix invalide")
            return


def menu(player, world):

    while True:
        print("\n┌=================˗ˏˋ ´ˎ˗=================┐")
        print("[1] Couper bois")
        print("[2] Tailler pierre")
        print("[3] Chercher nourriture")
        print("[4] Couper herbe")
        print("[5] Explorer")
        print("[6] Cuire/Affiner - Tresser - Tisser")
        print("[7] Stats joueur - monde")
        print("[8] Manger")
        print("[9] Dormir")
        print("[10] Structures - Outils - Vêtements")
        print("[11] Objectifs et brotips")
        print("[12] Sauver")
        print("[13] Quitter")
        print("└=================˗ˏˋ ´ˎ˗=================┘")
    
        choix = input("> ").lower()
    
        if choix == "1":
            player.gather("🪵", world, 1, 4)

        elif choix == "2":
            player.gather("🪨", world, 1, 3)
        
        elif choix == "3":
            player.gather("🥩", world, 1, 5)

        elif choix == "4":
            player.gather("🌿", world, 1, 3)

        elif choix == "5":
            menu_map(player, world)

        elif choix == "6":
            enhance_basic_resources(player)

        elif choix == "7":
            display.display_stats(player, world)
            display.display_food(player)
            display.display_inventaire(player)

        elif choix == "8":
            menu_manger(player)

        elif choix == "9":
            player.sleep(world)

        elif choix == "10":
            menu_construire(player, choix)

        elif choix == "11":
            display.display_objectifs(player, world)

        elif choix == "12":
            save.save_game(player, world)
    
        elif choix == "13":
            print("Au revoir.")
            return False

        else:
            print("Choix invalide")


def exit_menu():
    print("Au revoir.")
    return False 