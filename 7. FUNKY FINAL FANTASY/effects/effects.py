import random

from protagonists.get_stats import get_stats
from protagonists.utils_characters import get_live_characters
from effects.class_effect import Effect, EFFECTS

from protagonists.status import check_death


def start_of_turn(target):

    new_effects = []

    for effect in target.effects:


        if effect.type == "damage_over_time":

            apply_damage_effect(
                effect.source,
                target,
                effect
            )

            effect.duration -= 1


        elif effect.type == "heal_over_time":

            apply_healing_effect(
                effect.source,
                target,
                effect
            )

            effect.duration -= 1


        elif effect.type == "delayed_damage":

            effect.duration -= 1

            if effect.duration <= 0:

                print(f"{effect.name} fait du dégât !")
                apply_damage_effect(effect.source, target, effect)


        elif effect.type in IMMEDIATE_EFFECT:
            effect.duration -= 1


        elif effect.type in EFFECT_DURATION_ONLY:
            effect.duration -= 1


        else:
            print(f"Effet inconnu : {effect.name}")
            continue


        if effect.duration > 0:
            new_effects.append(effect)

        else:
            remove_effect_bonus(target, effect)
            remove_effect_malus(target, effect)
            print(f"L'effet {effect.name} disparaît de {target.name}.")

    target.effects = new_effects




def create_effect(effect_id, source=None):

    data = EFFECTS[effect_id]

    return Effect(
        id=effect_id,
        name=data["name"],
        type=data["type"],
        duration=data["duration"],
        value=data.get("value",0),
        scaling=data.get("scaling"),
        stackable=data.get("stackable",False),
        source=source
    )

def get_effect_by_id(effect_id, effect_list):

    for effect in effect_list:
        if effect.id == effect_id:
            return effect
        
def remove_effect_bonus(target, effect):

    if effect.type != "defense_bonus":
        return

    if hasattr(effect, "applied_value"):
        target.bonus["defense"] -= effect.applied_value


def remove_effect_malus(target, effect):

    if effect.type != "defense_malus":
        return

    if hasattr(effect, "applied_value"):
        target.bonus["defense"] += effect.applied_value


def get_taunt_target(player_team):

    for character in player_team:

        for effect in character.effects:

            if effect.id == "taunt":
                return character

    return None


def apply_choose_target(player_team):

    targets = get_live_characters(player_team)

    if not targets:
        return None

    taunter = get_taunt_target(player_team)

    if taunter:
        return taunter

    return random.choice(targets)


def calculate_effect_value(source, effect):

    value = effect.value

    if source is None:
        return value

    if effect.scaling == "level":
        value += source.level

    elif effect.scaling == "power":
        value += get_stats(source)["power"]

    elif effect.scaling == "defense":
        value += get_stats(source)["defense"]

    return value


def apply_damage_effect(source, target, effect):

    stats = get_stats(target)

    damage = calculate_effect_value(source, effect)
    target.life = max(target.life - damage, 0)

    print(
        f"{target.name} subit {effect.name} "
        f"(-{damage} PV → PV : {target.life}/{stats["life_max"]}) !"
        )

    check_death(target)


def apply_healing_effect(source, target, effect):

    stats = get_stats(target)

    heal = calculate_effect_value(source, effect)
    target.life = min(target.life + heal, stats["life_max"])

    print(
        f"{target.name} bénéficie de {effect.name} "
        f"(+{heal} PV → PV : {target.life}/{stats["life_max"]}) !"
        )


def apply_incapacitating_effect(entite, target, effect):
    print(f"{target.name} subit {effect.name} et est incapacité !")
    return any(effect.id == "stun" for effect in entite.effects)
    


def apply_defense_bonus(character, target, effect):

    bonus = calculate_effect_value(character, effect)

    effect.applied_value = bonus

    target.bonus["defense"] += bonus

    print(
        f"{target.name} bénéficie de {effect.name} "
        f"(+{bonus} défense) !"
    )


def apply_defense_malus(character, target, effect):

    malus = calculate_effect_value(character, effect)

    effect.applied_value = malus

    target.bonus["defense"] -= malus

    print(
        f"{target.name} subit {effect.name} "
        f"(-{malus} défense) !"
    )


IMMEDIATE_EFFECT = ["defense_bonus", "defense_malus", "damage_over_time", "heal_over_time"]

EFFECT_DURATION_ONLY = {
    "incapacitating",
    "forced_target",
}

EFFECT_HANDLERS = {
    "damage_over_time": apply_damage_effect,
    "delayed_damage": apply_damage_effect,
    "heal_over_time": apply_healing_effect, 
    "incapacitating": apply_incapacitating_effect,
    "forced_target": apply_choose_target,
    "defense_bonus": apply_defense_bonus,
    "defense_malus": apply_defense_malus
}

EFFECT_TYPE_LABEL = {
    "damage_over_time": "dégâts périodiques",
    "delayed_damage": "dégâts à retardement",
    "heal_over_time": "soins périodiques", 
    "incapacitating": "incapacitation",
    "forced_target": "ciblage forcé",
    "defense_bonus": "bonus de défense",
    "defense_malus": "malus de défense"

}