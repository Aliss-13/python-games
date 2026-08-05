import copy

def get_live_characters(player_team):
    return [character for character in player_team if character.life > 0]

def get_dead_characters(player_team):
    return [character for character in player_team if character.life <= 0]

def get_character_by_id(character_id, character_list):

    for character in character_list:
        if character.id == character_id:
            return copy.deepcopy(character)

    return None