from class_skill import get_skill
from class_effect import create_effect
import copy

class Character:
    def __init__(
            self, 
            id, 
            name, 
            character_class, 
            skills, 
            life, 
            mana, 
            base_stats, 
            level=1, 
            xp=0, 
            equipment=None,
            effects=None,
            bonus=None,
            ):
        
        self.id = id
        self.name = name
        self.character_class = character_class
        self.skills = skills
        self.life = life
        self.mana = mana
        self.base_stats = base_stats
        self.level = level
        self.xp = xp
        self.equipment = equipment or {}
        self.effects = effects or []
        self.bonus = bonus or {}


    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "character_class": self.character_class,
            "skills": [skill.id for skill in self.skills],
            "life": self.life,
            "mana": self.mana,
            "base_stats": self.base_stats,
            "level": self.level,
            "xp": self.xp,
            "equipment": self.equipment,
            "effects": [effect.id for effect in self.effects],
            "bonus": self.bonus,
        }
        
    @classmethod
    def from_dict(cls, data):

        return cls(

            id=data["id"],
            name=data["name"],
            character_class=data["character_class"],

            skills=[
                get_skill(skill_id)
                for skill_id in data.get("skills", [])
            ],

            life=data["life"],
            mana=data["mana"],
            base_stats=data["base_stats"],

            level=data["level"],
            xp=data["xp"],

            equipment=data.get("equipment", {}),

            effects=[
                create_effect(effect_id)
                for effect_id in data.get("effects", [])
            ],

            bonus=data.get("bonus", {})
        )

    
CLASS = ["magic", "hand-to-hand", "distance"]
    
CHARACTERS = [

    Character(
        id = "warlock",
        name = "Mage",
        character_class = "magic",
        skills = [get_skill("spark"), get_skill("fireball")],
        life = 70,
        mana = 50, 
        base_stats = {"life_max": 70, "mana_max" : 50, "power": 15,"speed": 12, "defense": 5}, 
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        bonus = {"life_max": 0, "mana_max" : 0, "power": 0,"speed": 0, "defense": 0} 
    ),    



    Character(
        id = "priest",
        name = "Prêtre",
        character_class = "magic",
        skills = [get_skill("simple_healing"), get_skill("blessing")],
        life = 60,
        mana = 50,
        base_stats = {"life_max": 60, "mana_max": 50, "power": 20, "speed": 10, "defense": 10},
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        bonus = {"life_max": 0, "mana_max" : 0, "power": 0,"speed": 0, "defense": 0}
    ),


    Character(
        id = "warrior",
        name = "Guerrier",
        character_class = "hand-to-hand",
        skills = [get_skill("attack"), get_skill("powerful_blow")],
        life = 100,
        mana = 0,
        base_stats = {"life_max": 100, "mana_max": 0, "power": 20,"speed": 8, "defense": 8},
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"arme" : None, "armure" : None, "mains" : None, "pieds" : None},
        bonus = {"life_max": 0, "power": 0,"speed": 0, "defense": 0}
    )
]


def get_live_characters(player_team):
    return [character for character in player_team if character.life > 0]

def get_dead_characters(player_team):
    return [character for character in player_team if character.life <= 0]

def get_character_by_id(character_id, character_list):

    for character in character_list:
        if character.id == character_id:
            return copy.deepcopy(character)

    return None