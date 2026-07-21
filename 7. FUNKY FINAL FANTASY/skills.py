import random
from sac_a_dos import get_stats
from class_effect import create_effect, EFFECT_HANDLERS, EFFECT_IMMEDIATE


def basic_attack(character, allies, enemies, skill, message):

    print(message)
    apply_skill_damage_to_targets(character, allies, enemies, skill)
    display_remaining_life(enemies)

#------------------------------------ EFFETS ---------------------------------------------------

def get_effect_targets(character, allies, skill_targets, skill_effect):

    if skill_effect.target == "self":
        return [character]

    elif skill_effect.target == "skill_target":
        return skill_targets

    elif skill_effect.target == "allies":
        return allies
    
    elif skill_effect.target == "ally":
        vivants = [ally for ally in allies if ally.life > 0]

        if not vivants:
            return []

        return [min(vivants, key=lambda ally: ally.life / get_stats(ally)["life_max"])]

    return []



def apply_skill_effects(character, allies, enemies, skill):

    targets = get_targets(character, allies, enemies, skill)

    for skill_effect in skill.effects:

        if random.random() <= skill_effect.chance:

            effect_targets = get_effect_targets(
                character,
                allies,
                targets,
                skill_effect,
            )


            for target in effect_targets:

                effect = create_effect(
                    skill_effect.effect_id,
                    source=character
                )

                target.effects.append(effect)

                if effect.type in EFFECT_IMMEDIATE:

                    handler = EFFECT_HANDLERS.get(effect.type)

                    if handler:
                        handler(character, target, effect)


def apply_skill_effects_to_targets(character, allies, enemies, skill):

    targets = get_targets(character, allies, enemies, skill)

    apply_skill_effects(character, targets, enemies, skill)
            

#------------------------------------ COUT ---------------------------------------------------

def pay_skill_cost_life(character, skill):
    cout = skill.cost
    
    if character.life <= cout:
        print(f"{character.name} n'a pas assez d'énergie !")
        return False
    
    character.life -= cout
    return True


def pay_skill_cost_mana(character, skill):
    
    cout = skill.cost
    
    if character.mana < cout:
        print(f"{character.name} n'a pas assez de mana !")
        return False
    
    character.mana -= cout
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

def get_targets(character, allies, enemies, skill, target=None):

    if skill.target == "opponent":
        return [enemy for enemy in enemies if enemy.life > 0]

    elif skill.target == "opponents":
        return enemies
    
    elif skill.target == "self":
        return [character]
    

    elif skill.target == "ally":

        vivants = [ally for ally in allies if ally.life > 0]

        if not vivants:
            return []

        return [min(vivants, key=lambda ally: ally.life / get_stats(ally)["life_max"])]

    elif skill.target == "allies":
        return allies
    
    else:
        return []
    

def deal_damage(attacker, defender, skill):
    damage = calculate_damage(attacker, defender, skill.power) # ATTENTION CET ORDRE EST IMPORTANT, TARGET = DEFENDER
    defender.life = max(defender.life - damage, 0)
    print(f"⚔ {attacker.name} → {defender.name} : -{damage} PV")


def apply_skill_damage_to_targets(character, allies, enemies, skill):

    targets = get_targets(character, allies, enemies, skill)

    for target in targets:
        deal_damage(character, target, skill)


def calculate_damage(attacker, defender, skill_power=0):

    attacker_stats = get_stats(attacker)
    defender_stats = get_stats(defender)

    raw_damage = attacker_stats["power"] + skill_power

    damage = max(raw_damage - defender_stats["defense"], 1)

    return damage

#------------------------------------ SOIN ---------------------------------------------------

def heal_target(character, target, skill):
    
    stats_healer = get_stats(character)
    stats_target = get_stats(target)
    healing = stats_healer["power"] + skill.power

    if target.life == stats_target["life_max"] :
        print(f"{target.name} est déjà au maximum de ses PV !")

           
    life_before_heal = target.life
    target.life = min(target.life + healing, stats_target["life_max"])
    real_healing = target.life - life_before_heal

    if real_healing > 0:
        print(f"{target.name} gagne {real_healing} PV → PV : {target.life}/{stats_target['life_max']} !")
        
#------------------------------------ GUERRIER ---------------------------------------------------

def attack(character, allies, enemies, skill):

    basic_attack(character, allies, enemies, skill, f"{character.name} lance Attaque 🤜 !")

def powerful_blow(character, allies, enemies, skill):

    if not pay_skill_cost_life(character, skill):
        return
    
    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance un Coup puissant ⚔️ (-{skill.cost} PV, {character.life} PV restants) !"
    )

    # effet bouclier
    apply_skill_effects_to_targets(character, allies, enemies, skill)
    


def spinning_attack(character, allies, enemies, skill):

    if not pay_skill_cost_life(character, skill):
        return
    
    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance Attaque tournoyante 🌀 (-{skill.cost} PV, {character.life} PV restants) !"
    )


def war_cry(character, allies, enemies, skill):
    
    print(f"{character.name} pousse un hurlement guttural ̗🗣️ !")
    
    apply_skill_effects_to_targets(character, allies, enemies, skill)
    
#------------------------------------ MAGE ---------------------------------------------------

def spark(character, allies, enemies, skill):

    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance Etincelle 💫 !"
    )


def fireball(character, allies, enemies, skill):
    
    if not pay_skill_cost_mana(character, skill):
        return

    # dégâts normaux
    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance Boule de feu ̗☄️ (-{skill.cost} mana, {character.mana} mana restant) !"
    )

    # effet brûlure
    
    apply_skill_effects_to_targets(character, allies, enemies, skill)


def pyrotechnic_explosion(character, allies, enemies, skill):

    if not pay_skill_cost_mana(character, skill):
        return
    
    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance Explosion pyrotechnique 💥 (-{skill.cost} mana, {character.mana} mana restant) !"
    )

def greek_fire(character, allies, enemies, skill):
    
    if not pay_skill_cost_mana(character, skill):
        return
    
    print(f"{character.name} prépare un baril ̗🛢️ (-{skill.cost} mana, {character.mana} mana restant) !")

    apply_skill_effects_to_targets(character, allies, enemies, skill)

#------------------------------------ PRETRE ---------------------------------------------------

def simple_healing(character, allies, enemies, skill): # MERCI DE NE PAS ENLEVER ENNEMIES

    injured_allies = []

    for ally in allies:
        stats = get_stats(ally)

        if 0 < ally.life < stats["life_max"]:
            injured_allies.append(ally)

    if not injured_allies:
        print("Personne à soigner !")
        return

    target = min(
        injured_allies,
        key=lambda ally: ally.life / get_stats(ally)["life_max"]
    )

    print(f"{character.name} lance Soin simple 🌿 !")
    heal_target(character, target, skill)


def blessing(character, allies, enemies, skill):

    if not pay_skill_cost_mana(character, skill):
        return
    
    print(f"{character.name} lance Bénédiction 🙏 (-{skill.cost} mana, {character.mana} mana restant) !")
    
    targets = get_targets(character, allies, enemies, skill)
    
    for target in targets:
        if target.life > 0:
            heal_target(character, target, skill)
    
    apply_skill_effects_to_targets(character, allies, enemies, skill)


def radiant_protection(character, allies, enemies, skill):
    
    apply_skill_effects_to_targets(character, allies, enemies, skill)


def penance(character, allies, enemies, skill):

    if not pay_skill_cost_mana(character, skill):
        return
    
    basic_attack(
        character,
        allies,
        enemies,
        skill,
        f"{character.name} lance Pénitence 💫 !"
    )

    # effet mélancolie
    
    apply_skill_effects_to_targets(character, allies, enemies, skill)