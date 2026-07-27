import copy
import json
import os
import sys

from class_character import Character, CHARACTERS, get_character_by_id
from class_enemy import ENEMIES
from class_zone import ZONES, get_zone_by_id
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
    def save(cls, game):

        data = {
            "version": cls.SAVE_VERSION,
            "team": [character.to_dict() for character in game.player_team],
            "enemy_team": [enemy.to_dict() for enemy in game.enemy_team],
            "inventory": game.inventory,
            "zone": game.current_zone.to_dict()
            
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

        # données indispensables
        player_team = cls.load_characters(data["team"])

        # données qui peuvent évoluer
        enemy_team = cls.load_enemy_progress(data.get("enemy_team", []))
        inventory = data.get("inventory", [])
        zone = cls.load_zone(data.get("zone"))
        
        print("⌛ Partie chargée.")

        return player_team, enemy_team, copy.deepcopy(inventory), zone


    @classmethod
    def load_characters(cls, saved_characters):

        return [
            Character.from_dict(character)
            for character in saved_characters
        ]

    @classmethod
    def load_enemy_progress(cls, saved_enemies):

        enemy_team = copy.deepcopy(ENEMIES)

        saved_dict = {
            enemy["id"]: enemy
            for enemy in saved_enemies
        }

        for enemy in enemy_team:

            saved_enemy = saved_dict.get(enemy.id)

            if saved_enemy:
                enemy.defeated = saved_enemy.get("defeated", False)

        return enemy_team

    
    @classmethod
    def load_zone(cls, saved_zone):

        if not saved_zone:
            return ZONES[0]

        zone_id = saved_zone["id"]

        zone = copy.deepcopy(get_zone_by_id(zone_id, ZONES))

        if zone:
            zone.load_state(saved_zone)

        return zone

    
    @classmethod
    def new_game(cls):

        player_team = [
            get_character_by_id("warrior", CHARACTERS),
            get_character_by_id("warlock", CHARACTERS),
            get_character_by_id("priest", CHARACTERS),
        ]

        enemy_team = []
        
        zone = ZONES[0]

        return player_team, enemy_team, inventory, zone


    @classmethod
  
    def update_save(cls, data):

        data.setdefault("version", 1)

        return data
    