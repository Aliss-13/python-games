import json
import os
import sys


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()
SAVE_PATH = os.path.join(BASE_DIR, "save_magique_boutique.json")


def save_game(witch, garden):

    print("Sauvegarde vers :", SAVE_PATH)

    data = {
        "witch": witch.to_dict(),
        "garden": garden.to_dict()
    }

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("🕷️ Partie sauvegardée.")


def load_game(witch, garden):

    if not os.path.exists(SAVE_PATH):
        print("Aucune sauvegarde trouvée.\n")
        return False

    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("🕸️ Partie chargée.")

        witch.from_dict(data["witch"])
        garden.from_dict(data["garden"])

        return True

    except json.JSONDecodeError:
        print("Sauvegarde corrompue.")
        return False
    
    