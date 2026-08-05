from skills.skills import get_skill
from effects.effects import create_effect


class Character:
    def __init__(
            self, 
            id, 
            name, 
            character_class, 
            skills, 
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
        self.life = base_stats.get("life_max",0)
        self.mana = base_stats.get("mana_max",0)
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
    @property
    def has_mana(self):
        return self.base_stats["mana_max"] > 0
    
    def __repr__(self):
        return f"{self.name} (lvl {self.level})"

    


