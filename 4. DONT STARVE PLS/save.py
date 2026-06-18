import json
import os
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_PATH = os.path.join(BASE_DIR, "save dont starve.json")

def save_game(player, world):
    os.makedirs(SAVE_PATH, exist_ok=True)

    data = {
        "player": player.to_dict(),
        "world": world.to_dict()
    }

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

        print("💾 Partie sauvegardée.")


def load_game(player, world):
    
    if not os.path.exists(SAVE_PATH):
        print("Aucune sauvegarde trouvée.")
        print("")
        return
    
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        player.from_dict(data["player"])
        world.from_dict(data["world"])

        print("📂 Partie chargée.")

    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")

