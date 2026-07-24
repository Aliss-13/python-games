import copy
import json
import os
import sys

from class_character import Character, CHARACTERS, get_character_by_id
from class_opponent import OPPONENTS
from data import inventory

SAVE_FILE = "funky_final_fantasy.json"

class SaveManager:

    SAVE_VERSION = 1

    @staticmethod
    def get_base_dir():
        if getattr(sys, "frozen", False):
            return os.path.dirname(sys.executable)

        return os.path.dirname(os.path.abspath(__file__))

    SAVE_PATH = os.path.join(get_base_dir.__func__(), SAVE_FILE)


    @classmethod
    def save(cls, player_team, enemy_team, inventory):

        data = {
            "version": cls.SAVE_VERSION,
            "team": [character.to_dict() for character in player_team],
            "enemy_team": [enemy.to_dict() for enemy in enemy_team],
            "inventory": inventory
        }

        with open(cls.SAVE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("📜 Partie sauvegardée.")


    @classmethod
    def load(cls):

        if not os.path.exists(cls.SAVE_PATH):
            print("Aucune sauvegarde.")
            return False

        with open(cls.SAVE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        data = cls.update_save(data)

        player_team = cls.load_characters(data["team"])
        enemy_team = cls.load_enemy_progress(data["enemy_team"])
        inventory = data["inventory"]
        

        print("⌛ Partie chargée.")

        return player_team, enemy_team, inventory


    @classmethod
    def load_characters(cls, saved_characters):

        return [
            Character.from_dict(character)
            for character in saved_characters
        ]

    @classmethod
    def load_enemy_progress(cls, saved_enemies):

        enemy_team = copy.deepcopy(OPPONENTS)

        for enemy in enemy_team:

            for saved in saved_enemies:

                if enemy.id == saved["id"]:
                    enemy.defeated = saved["defeated"]

        return enemy_team

    @classmethod
    def new_game(cls):

        player_team = [
            get_character_by_id("warrior", CHARACTERS),
            get_character_by_id("warlock", CHARACTERS),
            get_character_by_id("priest", CHARACTERS),
        ]

        enemy_team = copy.deepcopy(OPPONENTS)

        return player_team, enemy_team, inventory


    @classmethod
    def update_save(cls, data):

        version = data.get("version", 1)

        if version < cls.SAVE_VERSION:

            if version == 1:
                pass

        data["version"] = cls.SAVE_VERSION

        return data
    