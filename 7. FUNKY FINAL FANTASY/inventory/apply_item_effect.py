from protagonists.get_stats import get_stats
from effects.choose_target import choose_target
from effects.effects import create_effect, apply_defense_bonus


def apply_item_effect(player_team, item):

    effects = item.get("effects", {})

    success = False

    for effect, amount in effects.items():

        if effect == "heal":
            success |= heal_target(player_team, amount)

        elif effect == "heal_all":
            success |= heal_all(player_team, amount)

        elif effect == "restore_mana":
            success |= restore_mana(player_team, amount)

        elif effect == "resurrection":
            success |= resurrect(player_team, amount)

        elif effect == "iron_skin":
            success |= apply_buff(player_team, effect)


    return success


def apply_buff(player_team, effect_id):

    for target in player_team:

        if target.life <= 0:
            continue

        effect = create_effect(effect_id)

        apply_defense_bonus(None, target, effect)

        target.effects.append(effect)

    return True


def heal_all(player_team, amount):

    allies = [character for character in player_team if character.life > 0 and character.life < get_stats(character)["life_max"]]
        
    if not allies:
        print("Tout le monde est déjà au maximum de vie.")
        return False

    healed_anyone = False

    for target in allies:

        stats_target = get_stats(target)

        life_before = target.life

        target.life = min(
            target.life + amount,
            stats_target["life_max"]
        )

        real_healing = target.life - life_before

        if real_healing > 0:
            print(
                f"{target.name} gagne {real_healing} PV "
                f"→ PV : {target.life}/{stats_target['life_max']} !"
            )
            healed_anyone = True

    return healed_anyone


def heal_target(player_team, amount):

    allies = [character for character in player_team if character.life > 0 and character.life < get_stats(character)["life_max"]]
        
    if not allies:
        print("Tout le monde est déjà au maximum de vie.")
        return False
        
    target = min(allies, key=lambda character: character.life/get_stats(character)["life_max"])
    # key (= critère de comparaison) lambda range les personnages en fonction de leur pourcentage de vie
    # cible le personnage qui a le moins de vie en pourcentage
    stats_target = get_stats(target)
    healing = amount
    life_before_heal = target.life
    target.life = min(target.life + healing, stats_target["life_max"])
    real_healing = target.life - life_before_heal

    if real_healing > 0:
        print(f"{target.name} gagne {real_healing} PV → PV : {target.life}/{stats_target["life_max"]} !")

    if real_healing == 0:
        print(f"{target.name} est déjà au maximum de ses PV !")

    return True


def restore_mana(player_team, amount):
    targets = [character for character in player_team if character.life > 0
            and character.mana < get_stats(character)["mana_max"]]

    if not targets:
        print("Tout le monde a déjà son mana au maximum.")
        return False

    target = choose_target(targets, "Personnage à restaurer")

    if target is None:
        return False
    
    stats = get_stats(target)

    before = target.mana

    target.mana = min(target.mana + amount, stats["mana_max"])

    restored = target.mana - before

    print(f"{target.name} récupère {restored} points de mana !")

    return restored > 0


def resurrect(player_team, amount):
    
    dead = [character for character in player_team if character.life <= 0]

    target = choose_target(dead)

    if target is None:
        return False

    stats = get_stats(target)

    target.life = min(amount, stats["life_max"])

    print(f"{target.name} revient à la vie avec {target.life} PV !")

    return True