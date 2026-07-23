import random
from class_opponent import get_opponent_by_id, OPPONENTS


def explore_zone(zone):

    enemy_id = random.choice(zone.enemies)

    enemy = get_opponent_by_id(
        enemy_id,
        OPPONENTS
    )

    return enemy
