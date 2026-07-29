import copy
from class_skill import unlock_skills

def xp_required(level):
    return 50 * level ** 1.5 # niveau 1 : 50 - niveau 5 : ~559 - niveau 10 : ~1581


def average_level(player_team):
    return sum((character.level) for character in player_team) / len(player_team)

def scale_enemy(player_team, enemy):

    enemy_scaled = copy.deepcopy(enemy)

    player_team_level = average_level(player_team)

    enemy_scaled.level = max(1, int(player_team_level))

    facteur = 1 + (player_team_level - 1) * 0.05
    facteur = max(1.0, min(1.5, facteur))

    for stat in ["life_max", "mana_max", "power", "defense", "speed"]:
        enemy_scaled.base_stats[stat] = int(enemy_scaled.base_stats[stat] * facteur)

    enemy_scaled.life = enemy_scaled.base_stats["life_max"]
    enemy_scaled.mana = enemy_scaled.base_stats["mana_max"]

    return enemy_scaled



def scale_enemy_team(player_team, enemy_team):

    return [scale_enemy(player_team, enemy) for enemy in enemy_team]


def level_up(character):

    character.level += 1

    increase_stats(character)
    unlock_skills(character)


def increase_stats(character):
    print("")
    print(f"----{character.name}----")
    print(f"{character.name} passe niveau {character.level} !")

    character.base_stats["life_max"] += 20
    character.life = character.base_stats["life_max"]

    if character.base_stats["mana_max"] > 0:
        character.base_stats["mana_max"] += 10
        character.mana = character.base_stats["mana_max"]

    character.base_stats["power"] += 5
    character.base_stats["speed"] += 5
    character.base_stats["defense"] += 2

    if character.base_stats["mana_max"] > 0:
        print(f"Mana : {character.mana}/{character.base_stats["mana_max"]}")
        
    print(
        f"PV : {character.life}/{character.base_stats['life_max']} - "
        f"Puissance : {character.base_stats['power']} - "
        f"Vitesse : {character.base_stats['speed']} - "
        f"Défense : {character.base_stats['defense']}")

    