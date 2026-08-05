import random
from display import display_player_team, display_zone_progress, section
from menu_combat import menu_inventory
from combat import combat
from class_savemanager import SaveManager
from protagonists.class_npc import get_available_npcs
from quests.quests import start_quest

def menu_zone(game):

    while True:

        section("Actions")
        print("[1] Explorer")
        print("[2] Discuter avec les habitants")
        print("[3] Equipe")
        print("[4] Inventaire")
        print("[5] Progression")
        print("[6] Sauvegarder")
        print("[7] Quitter")

        choix = input("> ").lower()

        if choix == "1":
            combat(game)

        elif choix == "2":
            socialize(game)

        elif choix == "3":
            display_player_team(game.player_team)

        elif choix == "4":
            menu_inventory(game)
            

        elif choix == "5":
            display_zone_progress(game.current_zone, game)

        elif choix == "6":
            SaveManager.save(game)

        elif choix == "7":
            print("À bientôt.")
            return

        else:
            print("Choix invalide")


def socialize(game):

    available_npcs = get_available_npcs(
        game,
        game.current_zone
    )

    if not available_npcs:
        print("Vous avez déjà rencontré tout le monde dans cette zone.")
        return

    npc = random.choice(available_npcs)

    game.met_npcs.append(npc.id)

    print(f"\n👤 Vous rencontrez {npc.name}")
    print("")
    print(npc.description)

    if npc.dialogues:
        print("")
        print(npc.dialogues)

    for quest_id in npc.quests:
        start_quest(game, quest_id)