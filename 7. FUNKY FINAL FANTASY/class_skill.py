from class_skilleffect import SkillEffect

class Skill:

     def __init__(
        self,
        id,
        name,
        cost,
        target,
        actions,
        power=0,
        damage_type=None,
        effects=None,
        message="{caster} lance {skill} !",
        cost_type=None
    ):

        self.id = id
        self.name = name
        self.cost = cost
        self.cost_type= cost_type
        self.target = target
        self.actions = actions
        self.power = power
        self.damage_type = damage_type
        self.effects = effects or []
        self.message = message


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


SKILLS = [
#------------------------------------------ Orcs ------------------------------------------------

    Skill(
        id="dull_thud",
        name="Coup sourd 🫨",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="stun", chance=0.3, target="skill_target")],
    ),

#------------------------------------------ Gobelins ------------------------------------------------

    Skill(
        id="spear_thrust",
        name="Coup de lance ⚔️",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="poison", chance=0.3, target="skill_target")]
    ),

#------------------------------------------ Araignées ------------------------------------------------

    Skill(
        id="bite",
        name="Morsure 😬",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="poison", chance=0.3, target="skill_target")]
    ),

#------------------------------------------ Loups-garous ------------------------------------------------

    Skill(
        id="rage",
        name="Rage 💢",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="hemorrhage", chance=0.3, target="skill_target")]
    ),

#------------------------------------------ Baby Samuel ------------------------------------------------

    Skill(
        id="babys_wail",
        name="Hurlement de bébé 🚼",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="hemorrhage", chance=0.3, target="skill_target"), 
                 SkillEffect(effect_id="melancholy", chance=0.3, target="skill_target"),]
    ),

#------------------------------------------ Corbeaux ------------------------------------------------

    Skill(
        id="peck",
        name="Coup de bec 🐦‍⬛",
        cost=0,
        target="enemy",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="physical",
        effects=[SkillEffect(effect_id="melancholy", chance=0.3, target="skill_target")]
    ),

#------------------------------------------ THE VVITCH ------------------------------------------------

    Skill(
        id="corruption",
        name="Corruption 🫟",
        cost=0,
        target="enemies",
        actions=["damage", "apply_effect"],
        power=10,
        damage_type="magical",
        effects=[SkillEffect(effect_id="corruption", chance=1, target="skill_target")]
    ),

    Skill(
        id="dark_ritual",
        name="Rituel sombre 🕯️",
        cost=0,
        target="enemies",
        actions=["damage", "apply_effect"],
        power=20,
        damage_type="magical",
        effects=[SkillEffect(effect_id="dread", chance=0.4, target="skill_target")]
    ),

    Skill(
        id="sacrifice",
        name="Sacrifice 🗡️",
        cost=15,
        cost_type="mana",
        target="enemies",
        actions=["damage", "apply_effect"],
        power=30,
        damage_type="physical",
        effects=[SkillEffect(effect_id="hemorrhage", chance=1, target="skill_target")],
        message="{caster} lance {skill} (-{cost} mana, {remaining_mana} mana restant) !"
    ),

#------------------------------------------ BLACK PHILLIP ------------------------------------------------

    Skill(
        id="charge",
        name="Charge ♈",
        cost=0,
        target="enemy",
        actions=["damage"],
        power=10,
        damage_type="physical",
        effects=[],
    ),

    Skill(
        id="dark_stare",
        name="Regard sombre 👁️‍🗨️",
        cost=0,
        target="enemies",
        actions=["apply_effect"],
        effects=[SkillEffect(effect_id="dread", chance=1, target="skill_target")]
    ),

    Skill(
        id="black_flame",
        name="Flamme noire ⚫",
        cost=15,
        cost_type="mana",
        target="enemies",
        actions=["damage", "apply_effect"],
        power=20,
        damage_type="magical",
        effects=[SkillEffect(effect_id="burn", chance=0.3, target="skill_target")],
        message="{caster} lance {skill} (-{cost} mana, {remaining_mana} mana restant) !"
    ),


#------------------------------------------ GUERRIER ------------------------------------------------

    Skill(
        id="attack",
        name="Attaque 🤜",
        cost=0,
        target="enemy",
        actions=["damage"],
        power=10,
        damage_type="physical",
        effects=[],
    ),

    Skill(
        id="powerful_blow",
        name="Coup puissant ⚔️",
        cost=10,
        cost_type="life",
        target="enemy",
        actions=["damage", "apply_effect"],
        power=30,
        damage_type="physical",
        effects=[SkillEffect(effect_id="shield", chance=0.4, target="self")],
        message="{caster} lance {skill} (-{cost} PV, {remaining_life} PV restants) !"
    ),

    Skill(
        id="spinning_attack",
        name="Attaque tournoyante 🌀",
        cost=15,
        cost_type="life",
        target="enemies",
        actions=["damage"],
        power=20,
        damage_type="physical",
        effects=[],
        message="{caster} lance {skill} (-{cost} PV, {remaining_life} PV restants) !"
    ),

    Skill(
        id="war_cry",
        name="Cri de guerre 🗣️",
        cost=0,
        target="self",
        actions=["apply_effect"],
        power=20,
        effects=[SkillEffect(effect_id="taunt", chance=1, target="skill_target")]
    ),

#------------------------------------------ MAGE ------------------------------------------------

    Skill(
        id="spark",
        name="Etincelle 💫",
        cost=0,
        target="enemy",
        actions=["damage"],
        power=10,
        damage_type="magical",
        effects=[]
    ),

    Skill(
        id="fireball",
        name="Boule de feu ☄️",
        cost=10,
        cost_type="mana",
        target="enemy",
        actions=["damage", "apply_effect"],
        power=30,
        damage_type="magical",
        effects=[SkillEffect(effect_id="burn", chance=0.3, target="skill_target")],
        message="{caster} lance {skill} (-{cost} mana, {remaining_mana} mana restant) !"
    ),

    Skill(
        id="pyrotechnic_explosion",
        name="Explosion pyrotechnique 💥",
        cost=15,
        cost_type="mana",
        target="enemies",
        actions=["damage"],
        power=20,
        damage_type="magical",
        effects=[],
        message="{caster} lance {skill} (-{cost} mana, {remaining_mana} mana restant) !"
    ),

    Skill(
        id="greek_fire",
        name="Feu grégeois 🛢️",
        cost=10,
        cost_type="mana",
        target="enemy",
        actions=["damage"],
        power=80,
        damage_type="magical",
        effects=[SkillEffect(effect_id="greek_fire", chance=1, target="skill_target")],
        message="{caster} prépare un baril ̗🛢️ (-{cost} mana, {remaining_mana} mana restant) !"
    ),

#------------------------------------------ PRETRE ------------------------------------------------

    Skill(
        id="simple_healing",
        name="Soin simple ✨",
        cost=0,
        target="ally",
        actions=["heal"],
        power=20,
        effects=[]
    ),

    Skill(
        id="blessing",
        name="Bénédiction 🙏",
        cost=10,
        cost_type="mana",
        target="allies",
        actions=["heal", "apply_effect"],
        power=10,
        effects=[SkillEffect(effect_id="regeneration", chance=0.4, target="ally")],
        message="{caster} lance {skill} (-{cost} mana, {remaining_mana} mana restant) !"
    ),

    Skill(
        id="radiant_protection",
        name="Protection radieuse 🔶",
        cost=0,
        target="allies",
        actions=["apply_effect"],
        power=10,
        effects=[SkillEffect(effect_id="light_prism", chance=1, target="allies")]
    ),

    Skill(
        id="penance",
        name="Pénitence 💫",
        cost=0,
        target="enemy",
        actions=["damage"],
        power=20,
        damage_type="magical",
        effects=[SkillEffect(effect_id="melancholy", chance=0.3, target="enemy")]
    ),
]

COST_TYPES = [
    "mana",
    "life"
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






