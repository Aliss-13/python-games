from witch import upgrade_recipe_menu, available_crafts, game_tick, display_shop_stock, display_inventory, display_victory, update_victory
from witch import display_scarabac_parts, display_crafted_recipes, display_side_quests, SIDE_QUESTS, harvest
from garden import Garden, garden_levels
from save import save_game

garden = Garden(garden_levels)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_PINK = "\033[38;5;218m"
RESET = "\033[0m"

def menu(witch, garden):

    while True:
        print("\n=========== MENU ===========")
        print("[1] Craft")
        print("[2] Récolte")
        print("[3] Améliorations")
        print("[4] Ingrédients - Stock magasin - Bourse - Niveau")
        print("[5] Jardin")
        print("[6] Progression")
        print("[7] Sauvegarder")
        print("[8] Quitter")
    
        choix = input("> ").lower()
    

        if choix == "1":
            display_inventory(witch)
            print("")
            available_crafts(witch)
            game_tick(witch, garden)


        elif choix == "2":
            harvest(witch, garden)
            save_game(witch, garden)
            game_tick(witch, garden)


        elif choix == "3":
            print(f"Pièces : {witch.money}")
            upgrade_recipe_menu(witch)
            game_tick(witch, garden)


        elif choix == "4":
            display_inventory(witch)
            display_shop_stock(witch)
            print(f"\nPièces : {witch.money}")
            print(f"\n{LIGHT_PINK}Niveau : {witch.level}{RESET}")
            game_tick(witch, garden)


        elif choix == "5":
            garden.display_garden()
            game_tick(witch, garden)
    

        elif choix == "6":
            update_victory(witch)
            display_victory(witch)

            display_scarabac_parts(witch)
            display_crafted_recipes(witch)
            display_side_quests(witch)


        elif choix == "7":
            save_game(witch, garden)


        elif choix == "godmode123":
            debug_menu(witch, garden)


        elif choix == "8":
            print("Au revoir.")
            return False
        

        else:
            print("Choix invalide")

#============================= DEBUG ====================================

def debug_menu(witch, garden):

    while True:
        print("\n=== DEBUG MENU ===")
        print("[1] Level up +10")
        print("[2] Set level 20")
        print("[3] Crafter toutes les recettes")
        print("[4] Compléter scarabac")
        print("[5] Gagner 10000 pièces")
        print("[6] Forcer victoire")
        print("[7] Tester side quests")
        print("[8] Valider all side quests")
        print("[0] Retour")

        choice = input("> ")

        if choice == "1":
            witch.level += 10

        elif choice == "2":
            witch.level = 20
            garden.unlock_up_to_level(20)

        elif choice == "3":
            for k in witch.crafted_once:
                witch.crafted_once[k] = True

        elif choice == "4":
            for k in witch.scarabac:
                witch.scarabac[k] = True

        elif choice == "5":
            witch.money += 10000

        elif choice == "6":
            force_win(witch)

        elif choice == "7":
            debug_complete_quest(witch)

        elif choice == "8":
            debug_unlock_all_quests(witch)

        elif choice == "0":
            return


def force_win(witch):
    witch.level = 20

    for k in witch.crafted_once:
        witch.crafted_once[k] = True

    for k in witch.scarabac:
        witch.scarabac[k] = True

    witch.has_won = True

    print("🏆 Victoire forcée activée")



def debug_complete_quest(witch):
    print("\n=== DEBUG QUESTS ===")

    for i, (quest_id, quest) in enumerate(SIDE_QUESTS.items(), start=1):
        print(f"[{i}] {quest['name']}")

    print("[0] Retour")

    choice = int(input("> "))

    if choice == 0:
        return

    quest_id = list(SIDE_QUESTS.keys())[choice - 1]

    witch.side_quests[quest_id] = True
    print(f"✔ {SIDE_QUESTS[quest_id]['name']} validée (DEBUG)")


def debug_unlock_all_quests(witch):
    for quest_id in SIDE_QUESTS:
        witch.side_quests[quest_id] = True

    print("✔ Toutes les side quests sont validées (DEBUG)")


def debug_recompute_quests(witch):
    for quest_id, quest in SIDE_QUESTS.items():
        witch.side_quests[quest_id] = quest["condition"](witch)

    print("✔ Quêtes recalculées")
