import copy
from protagonists.data_enemies import ENEMIES

def create_enemy(enemy_id):

    for enemy in ENEMIES:
        if enemy.id == enemy_id:
            return copy.deepcopy(enemy)
    return None


def get_enemy_by_id(enemy_id, enemy_list):

    for enemy in enemy_list:
        if enemy.id == enemy_id:
            return enemy

    raise ValueError(f"Ennemi inconnu : {enemy_id}")

def get_live_enemies(enemy_team):
    return [enemy for enemy in enemy_team if enemy.life > 0]