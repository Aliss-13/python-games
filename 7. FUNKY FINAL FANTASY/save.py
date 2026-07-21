import json
import os
import sys
import copy
from data import inventory
from class_character import Character, CHARACTERS, get_character_by_id
from class_opponent import get_opponent_by_id, OPPONENTS


def get_base_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()
SAVE_PATH = os.path.join(BASE_DIR, "funky_final_fantasy.json")


def save_game(player_team, inventory, enemy_pool):

    print("Sauvegarde vers :", SAVE_PATH)

    data = {
        "team": [character.to_dict() for character in player_team],
        "inventory": inventory,
        "enemy_pool": [opponent.to_dict() for opponent in enemy_pool]
    }

    with open(SAVE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    print("📜 Partie sauvegardée.")



def load_game():

    if not os.path.exists(SAVE_PATH):
        print("Aucune sauvegarde trouvée.\n")
        return False

    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("⌛ Partie chargée.")

        player_team = load_characters(data["team"])
        inventory = data["inventory"]
        enemy_pool = load_enemy_progress(data.get("enemy_pool", []))
        return player_team, inventory, enemy_pool

    except json.JSONDecodeError:
        print("Sauvegarde corrompue.")
        return False
  

def load_characters(saved_characters):

    characters = []

    for data in saved_characters:

        character = Character.from_dict(data)
        characters.append(character)

    return characters


def load_enemy_progress(saved_enemies):

    for saved_enemy in saved_enemies:

        enemy = get_opponent_by_id(
            saved_enemy["id"],
            OPPONENTS
        )

        if enemy:
            enemy.defeated = saved_enemy["defeated"]


def new_game():

    character_list = CHARACTERS

    player_team = [
        get_character_by_id("warrior", character_list),
        get_character_by_id("warlock", character_list),
        get_character_by_id("priest", character_list)
    ]
    
    enemy_pool = copy.deepcopy(OPPONENTS)
        
    return player_team, inventory, enemy_pool