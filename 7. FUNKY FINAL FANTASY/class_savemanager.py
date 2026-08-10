import copy
import json
import os
import sys

from protagonists.class_character import Character
from protagonists.data_characters import CHARACTERS
from protagonists.utils_characters import get_character_by_id
from protagonists.data_enemies import ENEMIES

from zones.data_zones import ZONES
from zones.utils_zones import get_zone_by_id

from quests.class_quest import Quest
from quests.data_quests import FOREST_QUESTS

from class_gamestate import GameState

from inventory.item_generator import generate_item

SAVE_FILE = "funky_final_fantasy.json"

class SaveManager:

    SAVE_VERSION = 1

    @staticmethod
    def get_base_dir():
        if getattr(sys, "frozen", False):
            return os.path.dirname(sys.executable)

        return os.path.dirname(os.path.abspath(__file__))

    SAVE_PATH = os.path.join(get_base_dir.__func__(), SAVE_FILE)

# ----------------------------------------------------- SAVE --------------------------------------------

    @classmethod
    def update_save(cls, data):
        data.setdefault("version", 1)
        return data


    @classmethod
    def save(cls, game):

        data = {
            "version": cls.SAVE_VERSION,
            "team": cls.save_characters(game.player_team),
            "enemy_team": cls.save_enemy_progress(game.enemy_team),
            "inventory": cls.save_inventory(game.inventory),
            "zone": cls.save_zone(game.current_zone),
            "active_quests": cls.save_quest_list(game.active_quests),
            "completed_quests": cls.save_quest_list(game.completed_quests),
            "defeated_unique_enemies": list(game.defeated_unique_enemies),
            "gold": game.gold,
            "met_npcs": list(game.met_npcs),
            "npcs_with_new_dialogue": list(game.npcs_with_new_dialogue),
            "unlocked_shops": list(game.unlocked_shops)
        }

        with open(cls.SAVE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("")
        print("   🔖 Partie sauvegardée.   ")


    @classmethod
    def save_characters(cls, player_team):
        return [character.to_dict() for character in player_team]


    @classmethod
    def save_enemy_progress(cls, enemy_team):

        return [
            {
                "id": enemy.id,
                "defeated": enemy.defeated,
            }
            for enemy in enemy_team
        ]


    @classmethod
    def save_inventory(cls, inventory):
        return copy.deepcopy(inventory)

    
    @classmethod
    def save_zone(cls, zone):
        return zone.to_dict()


    @classmethod
    def save_quest_list(cls, quests):
        return [quest.to_dict() for quest in quests]

# ----------------------------------------------------- LOAD --------------------------------------------

    @classmethod
    def load(cls):

        if not os.path.exists(cls.SAVE_PATH):
            print("")
            print("      Aucune sauvegarde.      ")
            print("   🧭 Nouvelle aventure !   ")
            print("")
            return False

        with open(cls.SAVE_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            print("")
            print("      Sauvegarde trouvée.      ")
            print("     ⌛ Partie chargée !     ")
            print("")

        data = cls.update_save(data)

        # données indispensables
        player_team = cls.load_characters(data["team"])

        # données qui peuvent évoluer
        enemy_team = cls.load_enemy_progress(data.get("enemy_team", []))
        inventory = cls.load_inventory(data.get("inventory", []))
        zone = cls.load_zone(data.get("zone"))
        loaded_active_quests = cls.load_quest_list(data.get("active_quests", []))
        loaded_completed_quests = cls.load_quest_list(data.get("completed_quests", []))
        defeated_unique_enemies = data.get("defeated_unique_enemies", [])
        gold = data.get("gold", 0)
        met_npcs = data.get("met_npcs", [])
        npcs_with_new_dialogue = data.get("npcs_with_new_dialogue", [])
        unlocked_shops = data.get("unlocked_shops", [])

        return GameState(
            player_team=player_team,
            enemy_team=enemy_team,
            inventory=inventory,
            current_zone=zone,
            active_quests=loaded_active_quests,
            completed_quests=loaded_completed_quests,
            defeated_unique_enemies=defeated_unique_enemies,
            gold=gold,
            met_npcs=met_npcs,
            npcs_with_new_dialogue=npcs_with_new_dialogue,
            unlocked_shops=unlocked_shops

        )


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
    
    def load_inventory(cls, inventory_data):

        inventory = []

        for item in inventory_data:

            new_item = copy.deepcopy(item)

            new_item.setdefault("item_level", 1)
            new_item.setdefault("bonus", {})

            inventory.append(new_item)

        return inventory

    
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
    def load_quest_list(cls, quest_data_list):

        quests = []

        for data in quest_data_list:

            quest = Quest.from_dict(
                data,
                FOREST_QUESTS
            )

            quests.append(quest)

        return quests
    
# ----------------------------------------------------- NEW GAME --------------------------------------------

    @classmethod
    def new_game(cls):
        
        player_team = [
            get_character_by_id("warrior", CHARACTERS),
            get_character_by_id("warlock", CHARACTERS),
            get_character_by_id("priest", CHARACTERS),
        ]

        enemy_team = []

        inventory = [generate_item("phoenix_feather")]

        zone = ZONES[0]

        return GameState(
        player_team=player_team,
        enemy_team=enemy_team,
        inventory=inventory,
        current_zone=zone,
    )


    
    