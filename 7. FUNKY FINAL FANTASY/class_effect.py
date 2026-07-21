import random
from sac_a_dos import get_stats

class Effect:

    def __init__(
        self,
        id,
        name,
        type,
        duration,
        value=0,
        scaling=None,
        stackable=False,
        source=None
    ):
        self.id = id
        self.name = name
        self.type = type
        self.duration = duration
        self.value = value
        self.scaling = scaling
        self.stackable = stackable
        self.source = source


def to_dict(self):

    return {
        "id": self.id,
        "name": self.name,
        "type": self.type,
        "duration": self.duration,
        "value": self.value,
        "scaling": self.scaling,
        "stackable": self.stackable,
        "source": self.source
    }

EFFECTS = {

    # damage_over_time
    "burn": {
        "id": "burn",
        "name": "Brûlure 🔥",
        "type": "damage_over_time",
        "duration": 3,
        "value": 4,
        "scaling": "defense",
        "stackable": True, 
    },

    "poison": {
        "id": "poison",
        "name": "Poison 🦠",
        "type": "damage_over_time",
        "duration": 3,
        "value": 5,
        "scaling": "defense",
        "stackable": True
    },

    "hemorrhage": {
        "id": "hemorrhage",
        "name": "Hémorragie 🩸",
        "type": "damage_over_time",
        "duration": 3,
        "value": 6,
        "scaling": "defense",
        "stackable": True
    },

    "melancholy": {
        "id": "melancholy",
        "name": "Mélancolie 🎭",
        "type": "damage_over_time",
        "duration": 3,
        "value": 5,
        "scaling": "defense",
        "stackable": True
    },

    # damage
    "greek_fire": {
        "id": "greek_fire",
        "name": "Feu grégeois 🛢️",
        "type": "delayed_damage",
        "duration": 3,
        "value": 80,
        "scaling": "defense",
        "stackable": True
    },


    # heal_over_time
    "regeneration": {
        "id": "regeneration",
        "name": "Régénération 🌟",
        "type": "heal_over_time",
        "duration": 3,
        "value": 6,
        "scaling": "defense",
        "stackable": True
    },


    # forced_target
    "taunt": {
        "id": "taunt",
        "name": "Provocation 🗣️",
        "type": "forced_target",
        "duration": 3,
        "stackable": False
    },

    "stun": {
        "id": "stun",
        "name": "Etourdissement 😵",
        "type": "incapacitating",
        "duration": 2,
        "stackable": False
    },


    # defense_buff
    "light_prism": {
        "id": "light_prism",
        "name": "Prisme lumineux 🔶",
        "type": "defense_buff",
        "duration": 3,
        "value": 4,
        "scaling": "power",
        "stackable": True
    },

    "shield": {
        "id": "shield",
        "name": "Bouclier 🛡️",
        "type": "defense_buff",
        "duration": 2,
        "value": 7,
        "scaling": "power",
        "stackable": True
    }
}


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

def remove_effect_bonus(target, effect):

    if effect.type != "defense_buff":
        return

    if hasattr(effect, "applied_value"):
        target.bonus["defense"] -= effect.applied_value


def get_taunt_target(player_team):

    for character in player_team:

        for effect in character.effects:

            if effect.id == "taunt":
                return character

    return None


def apply_choose_target(player_team):
    from class_character import get_live_characters

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

    damage = calculate_effect_value(source, effect)
    target.life = max(target.life - damage, 0)

    print(f"{target.name} subit {effect.name} ")
    print(f"{target.name} subit {damage} dégâts de {effect.name} !")


def apply_healing_effect(source, target, effect):

    stats = get_stats(target)

    heal = calculate_effect_value(source, effect)
    target.life = min(target.life + heal, stats["life_max"])

    print(f"{target.name} bénéficie de {effect.name} ")
    print(f"{target.name} → +{heal} PV → PV : {target.life}/{stats["life_max"]} !")


def apply_incapacitating_effect(entite, target, effect):
    print(f"{target.name} subit {effect.name} et est incapacité !")
    return any(effect.id == "stun" for effect in entite.effects)
    


def apply_protection_effect(character, target, effect):

    bonus = calculate_effect_value(character, effect)

    effect.applied_value = bonus

    target.bonus["defense"] += bonus

    print(
        f"{target.name} bénéficie de {effect.name} "
        f"(+{bonus} défense) !"
    )
   
EFFECT_IMMEDIATE = ["defense_buff"]

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
    "defense_buff": apply_protection_effect
}

EFFECT_TYPE_LABEL = {
    "damage_over_time": "dégâts périodiques",
    "delayed_damage": "dégâts à retardement",
    "heal_over_time": "soins périodiques", 
    "incapacitating": "incapacitation",
    "forced_target": "ciblage forcé",
    "defense_buff": "bonus défensif"
}



