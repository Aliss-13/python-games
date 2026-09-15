class Effect:

    def __init__(
        self,
        id: str,
        name: str,
        type: str,
        duration: int,
        value: int=0,
        scaling: str | None = None,
        stackable: bool=False,
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


    def to_dict(self) -> dict:

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
        "name": "Brûlure 🔥",
        "type": "damage_over_time",
        "duration": 3,
        "value": 4,
        "scaling": "level",
        "stackable": True, 
    },

    "poison": {
        "name": "Poison 🦠",
        "type": "damage_over_time",
        "duration": 3,
        "value": 5,
        "scaling": "level",
        "stackable": True
    },

    "hemorrhage": {
        "name": "Hémorragie 🩸",
        "type": "damage_over_time",
        "duration": 3,
        "value": 6,
        "scaling": "level",
        "stackable": True
    },

    "corruption": {
        "name": "Corruption 🫟",
        "type": "damage_over_time",
        "duration": 3,
        "value": 6,
        "scaling": "level",
        "stackable": True
    },

    "melancholy": {
        "name": "Mélancolie 🎭",
        "type": "damage_over_time",
        "duration": 3,
        "value": 5,
        "scaling": "level",
        "stackable": True
    },

    # damage
    "greek_fire": {
        "name": "Feu grégeois 🛢️",
        "type": "delayed_damage",
        "duration": 3,
        "value": 80,
        "scaling": "level",
        "stackable": False
    },


    # heal_over_time
    "regeneration": {
        "name": "Régénération 🌟",
        "type": "heal_over_time",
        "duration": 3,
        "value": 6,
        "scaling": "level",
        "stackable": True
    },


    # forced_target
    "taunt": {
        "name": "Provocation 🗣️",
        "type": "forced_target",
        "duration": 3,
        "stackable": False
    },

    "stun": {
        "name": "Etourdissement 😵",
        "type": "incapacitating",
        "duration": 2,
        "stackable": False
    },


    # defense_bonus
    "light_prism": {
        "name": "Prisme lumineux 🔶",
        "type": "defense_bonus",
        "duration": 3,
        "value": 4,
        "scaling": "level",
        "stackable": False
    },

    "shield": {
        "name": "Bouclier 🛡️",
        "type": "defense_bonus",
        "duration": 2,
        "value": 7,
        "scaling": "level",
        "stackable": False
    },

    "iron_skin": {
        "name": "Peau de fer 🦾",
        "type": "defense_bonus",
        "duration": 3,
        "value": 20,
        "stackable": True
    },

    # defense_malus
    "dread": {
        "name": "Terreur 👁️‍🗨️",
        "type": "defense_malus",
        "duration": 3,
        "value": 4,
        "scaling": "level",
        "stackable": False
    }
}