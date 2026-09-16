from witch import harvest, game_tick, display_shop_stock, display_inventory
from recipes_actions import upgrade_recipe_menu, available_crafts, put_on_shelf
from progression import display_scarabac_parts, display_remaining_recipes, display_side_quests, SIDE_QUESTS, display_victory, update_victory_objectives
from garden import display_garden
from save import save_game
from clients import display_waiting_clients, check_waiting_clients

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
        print("[4] Ingrédients récoltés - Stock magasin - Bourse - Niveau")
        print("[5] Jardin")
        print("[6] Récupérer des articles en réserve")
        print("[7] Progression")
        print("[8] Sauvegarder")
        print("[9] Quitter")
    
        choix = input("> ").lower()
    

        if choix == "1":
            display_inventory(witch)
            print("")
            check_waiting_clients(witch)
            display_waiting_clients(witch)
            print()
            available_crafts(witch, garden)
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
            display_garden(garden)
            game_tick(witch, garden)


        elif choix == "6":
            put_on_shelf(witch)
    

        elif choix == "7":
            update_victory_objectives(witch)
            display_victory(witch)

            display_scarabac_parts(witch)
            display_remaining_recipes(witch)
            display_side_quests(witch)


        elif choix == "8":
            save_game(witch, garden)


        elif choix == "godmode123":
            debug_menu(witch, garden)


        elif choix == "9":
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
            witch.level = 10
            garden.unlock_up_to_level(witch.level)


        elif choice == "2":
            witch.level = 20
            garden.unlock_up_to_level(witch.level)

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
