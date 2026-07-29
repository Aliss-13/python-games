from class_effect import IMMEDIATE_EFFECT, EFFECT_DURATION_ONLY
from class_effect import apply_damage_effect, apply_healing_effect, remove_effect_bonus, remove_effect_malus


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