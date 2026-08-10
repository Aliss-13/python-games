import random
from display import display_player_team, display_zone_progress
from menu_combat import menu_inventory
from combat import handle_explore
from class_savemanager import SaveManager
from npcs.utils_npcs import get_available_npcs
from quests.talk_to_npcs import talk_to_npc

from inventory.inventory import menu_shop

def menu_zone(game):

    while True:
        
        actions = {
            "1": ("Explorer", lambda: handle_explore(game)),
            "2": ("Discuter avec les habitants", lambda: socialize(game)),
            "3": ("Boutique (verrouillée)", None),
            "4": ("Equipe", lambda: display_player_team(game.player_team)),
            "5": ("Inventaire", lambda: menu_inventory(game)),
            "6": ("Progression", lambda: display_zone_progress(game.current_zone, game)),
            "7": ("Sauvegarder", lambda: SaveManager.save(game)),
            "8": ("Quitter", None)
        }

        if game.unlocked_shops:
            actions["3"] = ("Boutique", lambda: menu_shop(game))

        print("\n")
        
        for key, (name, _) in sorted(actions.items()):
            print(f"[{key}] {name}")

        choix = input("> ")

        if choix in actions:
            name, action = actions[choix]
            
            if action:
                action()
               
            else:
                print("À bientôt.")
                return

        else:
            print("Choix invalide.")


def socialize(game):

    available_npcs = get_available_npcs(
        game,
        game.current_zone
    )

    if not available_npcs:
        print("Vous avez déjà rencontré tout le monde dans cette zone.")
        return

    npc = random.choice(available_npcs)

    print(f"\n👤 Vous rencontrez {npc.name}")
    print("")

    talk_to_npc(game, npc)