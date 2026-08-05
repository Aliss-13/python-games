def is_dead(entity):
    return entity.life <= 0


def check_death(entity):

    if is_dead(entity):
        print(f"💀 {entity.name} tombe au combat !")