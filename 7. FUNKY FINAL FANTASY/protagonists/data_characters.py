from skills.skills import get_skill
from protagonists.class_character import Character

CHARACTERS = [

    Character(
        id = "warlock",
        name = "Mage",
        character_class = "magic",
        skills = [get_skill("spark"), get_skill("fireball")],
        base_stats = {"life_max": 70, "mana_max" : 50, "power": 15,"speed": 12, "defense": 5}, 
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"weapon" : None, "head" : None, "chest" : None, "hands" : None, "legs" : None, "feet" : None},
        bonus = {"life_max": 0, "mana_max" : 0, "power": 0,"speed": 0, "defense": 0} 
    ),    



    Character(
        id = "priest",
        name = "Prêtre",
        character_class = "magic",
        skills = [get_skill("simple_healing"), get_skill("blessing")],
        base_stats = {"life_max": 60, "mana_max": 50, "power": 20, "speed": 10, "defense": 10},
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"weapon" : None, "head" : None, "chest" : None, "hands" : None, "legs" : None, "feet" : None},
        bonus = {"life_max": 0, "mana_max" : 0, "power": 0,"speed": 0, "defense": 0}
    ),


    Character(
        id = "warrior",
        name = "Guerrier",
        character_class = "hand_to_hand",
        skills = [get_skill("attack"), get_skill("powerful_blow")],
        base_stats = {"life_max": 100, "mana_max": 0, "power": 20,"speed": 8, "defense": 8},
        effects = [],
        level = 1,
        xp = 0,
        equipment = {"weapon" : None, "head" : None, "chest" : None, "hands" : None, "legs" : None, "feet" : None},
        bonus = {"life_max": 0, "power": 0,"speed": 0, "defense": 0}
    )
]

