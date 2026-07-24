import copy
from loot_tables import FOREST_LOOTS
from data import ITEMS
from ui import separator
from class_skill import unlock_skills

def xp_required(level):
    return 50 + ((level - 1) * 25) # niveau 1 = 50 xp requis, niveau 2 = 75 xp requis, niveau 3 = 100 xp requis etc.

def average_level(player_team):
    return sum((character.level) for character in player_team) / len(player_team)

    
def scale_opponent(player_team, opponent):

    opponent_scaled = copy.deepcopy(opponent)

    player_team_level = average_level(player_team)

    facteur = 1 + (player_team_level - opponent.tier) * 0.05
    facteur = max(0.8, min(1.5, facteur))

    for stat in ["life_max", "power", "defense"]:
        opponent_scaled.base_stats[stat] = int(opponent_scaled.base_stats[stat] * facteur)

    opponent_scaled.life = opponent_scaled.base_stats["life_max"]

    return opponent_scaled


def scale_enemy_team(player_team, enemy_team):

    return [scale_opponent(player_team, enemy) for enemy in enemy_team]


def level_up(character):
    character.base_stats["life_max"] += 20
    character.life = character.base_stats["life_max"]

    character.base_stats["power"] += 5
    character.base_stats["speed"] += 5
    character.base_stats["defense"] += 2

    print(f"{character.name} → PV : {character.base_stats['life_max']} - puissance : {character.base_stats['power']} ")
    print(f"- vitesse : {character.base_stats['speed']} - défense : {character.base_stats['defense']}")

    if character.mana > 0:
        character.base_stats["mana_max"] += 10
        character.mana = character.base_stats["mana_max"]
        print(f" - mana : {character.base_stats['mana_max']}")

    if character.mana == 0:
        character.base_stats["mana_max"] == 0
        character.mana = character.base_stats["mana_max"]
          


def gain_xp(player_team, opponent):

    gain_xp = opponent.xp
    
    for character in player_team:
        if character.life > 0:

            character.xp += opponent.xp
            separator()
            print(f"{character.name} gagne {gain_xp} XP !")

            while character.xp >= xp_required(character.level):

                character.xp -= xp_required(character.level)
                character.level += 1
                level_up(character)

                print(f"{character.name} passe niveau {character.level} !")

                unlock_skills(character)



def get_item_stats(item):

    data = ITEMS[item["id"]]

    level = item.get("item_level", 1)

    stats = {}

    for stat, value in data["bonus"].items():

        scaling = data.get("scaling", {}).get(stat, 0)

        stats[stat] = value + int(level * scaling)

    return stats