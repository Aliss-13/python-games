import random
from protagonists.get_stats import get_stats
from protagonists.status import check_death
from effects.effects import create_effect, EFFECT_HANDLERS, IMMEDIATE_EFFECT
from skills.class_skill import SKILLS


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

                if effect.type in IMMEDIATE_EFFECT:

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
        check_death(target)

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

#-------------------------------------------------------------------------------------------------------------------------

COST_TYPES = [
    "mana",
    "PV"
]

SKILL_UNLOCKS = {

    "warlock": {

        1: ["spark", "fireball"],
        2: ["pyrotechnic_explosion"],
        3: ["greek_fire"]

    },

    "warrior": {

        1: ["attack", "powerful_blow"],
        2: ["spinning_attack"],
        3: ["war_cry"]

    },

    "priest": {

        1: ["simple_healing", "blessing"],
        2: ["radiant_protection"], 
        3: ["penance"] 

    }

}


def unlock_skills(character):

    unlocks = SKILL_UNLOCKS.get(character.id, {})

    if character.level in unlocks:

        for skill_id in unlocks[character.level]:

            skill = get_skill(skill_id)

            if skill not in character.skills:
                character.skills.append(skill)
                print(f"{character.name} apprend {skill.name} !")


def get_target_name(skill):
    return TARGET_NAMES.get(skill.target)


def get_skill(skill_id):

    for skill in SKILLS:
        if skill.id == skill_id:
            return skill

    return None


TARGET_NAMES = {
    "enemy": "Ennemi",
    "enemies": "Tous les ennemis",
    "self": "Soi",
    "ally": "Allié",
    "allies": "Tous les alliés"
}


def display_skill_message(context):

    values = {
        "caster": context.caster.name,
        "skill": context.skill.name,
        "cost": context.skill.cost,
        "remaining_life": context.caster.life,
        "remaining_mana": context.caster.mana
    }

    print(
        context.skill.message.format(**values)
    )