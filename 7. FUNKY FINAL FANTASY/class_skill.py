from class_skilleffect import SkillEffect
from skills import attack, powerful_blow, spinning_attack, war_cry
from skills import spark, fireball, pyrotechnic_explosion, greek_fire
from skills import simple_healing, blessing, radiant_protection, penance

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
        effects=None
    ):

        self.id = id
        self.name = name
        self.cost = cost
        self.target = target
        self.actions = actions
        self.power = power
        self.damage_type = damage_type
        self.effects = effects or []



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
    "opponent": "Ennemi",
    "opponents": "Tous les ennemis",
    "self": "Soi",
    "ally": "Allié",
    "allies": "Tous les alliés"
}


SKILL_FUNCTIONS = {
    "attack": attack,
    "powerful_blow": powerful_blow,
    "spinning_attack": spinning_attack,
    "war_cry": war_cry,
    "spark": spark,
    "fireball": fireball,
    "pyrotechnic_explosion": pyrotechnic_explosion,
    "greek_fire": greek_fire,
    "simple_healing": simple_healing,
    "blessing": blessing,
    "radiant_protection": radiant_protection,
    "penance": penance
}


SKILLS = [

    # GUERRIER

        Skill(
            id="attack",
            name="Attaque",
            cost=0,
            target="opponent",
            actions=["damage"],
            power=10,
            damage_type="physical",
            effects=[],
            
        ),

        Skill(
            id="powerful_blow",
            name="Coup puissant",
            cost=10,
            target="opponent",
            actions=["damage", "apply_effect"],
            power=30,
            damage_type="physical",
            effects=[
                SkillEffect(
                    effect_id="shield",
                    chance=0.4,
                    target="self"
                    )
            ]
        ),

        Skill(
            id="spinning_attack",
            name="Attaque tournoyante",
            cost=15,
            target="opponents",
            actions=["damage"],
            power=20,
            damage_type="physical",
            effects=[]
        ),

        Skill(
            id="war_cry",
            name="Cri de guerre",
            cost=0,
            target="self",
            actions=["apply_effect"],
            power=20,
            effects=[
                SkillEffect(
                    effect_id="taunt",
                    chance=1,
                    target="skill_target"
                    )
            ]
        ),


    # MAGE

        Skill(
            id="spark",
            name="Etincelle",
            cost=0,
            target="opponent",
            actions=["damage"],
            power=10,
            damage_type="magical",
            effects=[]
        ),

        Skill(
            id="fireball",
            name="Boule de feu",
            cost=10,
            target="opponent",
            actions=["damage", "apply_effect"],
            power=30,
            damage_type="magical",
            effects=[
                SkillEffect(
                    effect_id="burn",
                    chance=0.3,
                    target="skill_target"
                    )
            ]
        ),

        Skill(
            id="pyrotechnic_explosion",
            name="Explosion pyrotechnique",
            cost=15,
            target="opponents",
            actions=["damage"],
            power=20,
            damage_type="magical",
            effects=[]
        ),

        Skill(
            id="greek_fire",
            name="Feu grégeois",
            cost=10,
            target="opponent",
            actions=["damage"],
            power=80,
            damage_type="magical",
            effects=[
                SkillEffect(
                effect_id="greek_fire",
                chance=1,
                target="skill_target"
                )
            ]
        ),


    # PRETRE

        Skill(
            id="simple_healing",
            name="Soin simple",
            cost=0,
            target="ally",
            actions=["heal"],
            power=20,
            effects=[]
        ),

        Skill(
            id="blessing",
            name="Bénédiction",
            cost=10,
            target="allies",
            actions=["heal", "apply_effect"],
            power=10,
            effects=[
                SkillEffect(
                    effect_id="regeneration",
                    chance=0.4, 
                    target="ally"
                    )
            ]
        ),

        Skill(
            id="radiant_protection",
            name="Protection radieuse",
            cost=0,
            target="allies",
            actions=["apply_effect"],
            power=10,
            effects=[
                SkillEffect(
                    effect_id="light_prism",
                    chance=1,
                    target="allies"
                    )
            ]
        ),

        Skill(
            id="penance",
            name="Pénitence",
            cost=10,
            target="opponent",
            actions=["damage"],
            power=20,
            damage_type="magical",
            effects=[
                SkillEffect(
                    effect_id="melancholy",
                    chance=0.3, 
                    target="opponent"
                    )
            ]
        ),
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






