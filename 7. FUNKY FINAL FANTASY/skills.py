import random
from sac_a_dos import get_stats
from class_effect import create_effect, EFFECT_HANDLERS, EFFECT_IMMEDIATE

#------------------------------------ EFFETS ---------------------------------------------------

def get_effect_targets(context, skill_targets, skill_effect): 

    if skill_effect.target == "self": 
        return [context.caster] 
    
    elif skill_effect.target == "skill_target": 
        return skill_targets 
    
    elif skill_effect.target == "allies":
        return [ally for ally in context.allies if ally.life > 0]
      
    elif skill_effect.target == "ally": 
        vivants = [ally for ally in context.allies if ally.life > 0] 

        if not vivants: 
            return [] 
        
        return [min(vivants, key=lambda ally: ally.life / get_stats(ally)["life_max"])] 

    return []


def apply_skill_effects(context):
    
    targets = get_skill_targets(context)

    for skill_effect in context.skill.effects:

        if random.random() <= skill_effect.chance:

            effect_targets = get_effect_targets(
                context,
                targets,
                skill_effect,
            )


            for target in effect_targets:

                effect = create_effect(
                    skill_effect.effect_id,
                    source=context.caster
                )

                target.effects.append(effect)

                if effect.type in EFFECT_IMMEDIATE:

                    handler = EFFECT_HANDLERS.get(effect.type)

                    if handler:
                        handler(context.caster, target, effect)


#------------------------------------ COUT ---------------------------------------------------

def pay_skill_cost(context):

    skill = context.skill
    caster = context.caster

    if skill.cost_type == "mana":
        if caster.mana < skill.cost:
            print("Pas assez de mana !")
            return False

        caster.mana -= skill.cost

    elif skill.cost_type == "life":
        if caster.life <= skill.cost:
            print("Pas assez de PV !")
            return False

        caster.life -= skill.cost

    return True

#------------------------------------ VIE RESTANTE ---------------------------------------------------

def check_death(target):

    if target.life <= 0:
        target.life = 0
        return True

    return False


def display_remaining_life(targets):

    for target in targets:

        if check_death(target):
            continue

        else:
            print(f"{target.name} n'a plus que {target.life} PV !")

#------------------------------------ DEGATS : CIBLES, CALCUL et APPLICATION ---------------------------------------------------

def get_skill_targets(context):

    enemies = [
        entity for entity in context.enemies
        if entity.life > 0
    ]

    allies = [
        entity for entity in context.allies
        if entity.life > 0
    ]

    if context.skill.target == "enemy":
        return [random.choice(enemies)] if enemies else []

    elif context.skill.target == "enemies":
        return enemies

    elif context.skill.target == "self":
        return [context.caster]

    elif context.skill.target == "ally":
        return [min(allies, key=lambda ally: ally.life / get_stats(ally)["life_max"])] if allies else []

    elif context.skill.target == "allies":
        return allies

    return []

def deal_damage(attacker, defender, skill):
    damage = calculate_damage(attacker, defender, skill) # ATTENTION CET ORDRE EST IMPORTANT, TARGET = DEFENDER
    defender.life = max(defender.life - damage, 0)
    print(f"⚔ {attacker.name} → {defender.name} : -{damage} PV")


def apply_skill_damage_to_targets(context):

    targets = get_skill_targets(context)
    
    for target in targets:
        deal_damage(context.caster, target, context.skill)

    return targets


def calculate_damage(attacker, defender, skill):

    attacker_stats = get_stats(attacker)
    defender_stats = get_stats(defender)

    raw_damage = skill.power + attacker_stats["power"]

    damage = raw_damage - defender_stats["defense"]

    return max(1, damage)

#------------------------------------ SOIN ---------------------------------------------------

def apply_skill_healing(context):

    targets = get_skill_targets(context)

    for target in targets:
        heal_target(context, target)

def heal_target(context, target):
    
    stats_healer = get_stats(context.caster)
    stats_target = get_stats(target)
    healing = stats_healer["power"] + context.skill.power

    if target.life == stats_target["life_max"] :
        print(f"{target.name} est déjà au maximum de ses PV !")

           
    life_before_heal = target.life
    target.life = min(target.life + healing, stats_target["life_max"])
    real_healing = target.life - life_before_heal

    if real_healing > 0:
        print(f"{target.name} gagne {real_healing} PV → PV : {target.life}/{stats_target['life_max']} !")