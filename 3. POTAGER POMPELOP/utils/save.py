import json
import os
from core.state import GameState

import os
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_PATH = os.path.join(BASE_DIR, "save potager.json")


def load_state():

    data = safe_load_json()

    if data is None:
        return GameState()

    data = normalize_dict(data)

    return GameState.from_dict(data)
    

def safe_load_json():
    
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    
   
    

def normalize_dict(data):

    if not isinstance(data, dict):
        data = {}

    joueur = data.setdefault("joueur", {})

    joueur.setdefault("pieces", 50)
    joueur.setdefault("xp", 0)
    joueur.setdefault("niveau", 1)
    joueur.setdefault("potager_max", 5)
    joueur.setdefault("garde_manger", {})
    joueur.setdefault("inventaire", {})
    joueur.setdefault("potager", [])
    joueur.setdefault("graines_disponibles", [1])
    joueur.setdefault("prestige", 0)

    data.setdefault("commandes_en_cours", [])
    data.setdefault("next_commande_id", 0)
    data.setdefault("tour", 0)

    return data


def sauvegarder(state: GameState):

    print("Sauvegarde vers :", SAVE_PATH)

    with open(SAVE_PATH, "w", encoding="utf-8") as f:

        json.dump(
            state.to_dict(),
            f,
            indent=4,
            ensure_ascii=False
        )
        
    print("Partie sauvegardée ✔")
