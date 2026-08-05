from skills.skills import get_skill
from protagonists.class_enemy import Enemy

ENEMIES = [
# =============================================== GOBELINS

    Enemy(
        id="novice_goblin",
        name="Gobelin novice",
        rarity="common",
        tier=1,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 9, "defense": 5}, 
        skills = [get_skill("spear_thrust")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=15
    ),

    Enemy(
        id="trained_goblin",
        name="Gobelin entraîné",
        rarity="uncommon",
        tier=2,
        base_stats={"life_max": 220, "mana_max": 0, "power": 40, "speed": 12, "defense": 8}, 
        skills = [get_skill("spear_thrust")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=25
    ),

    Enemy(
        id="veteran_goblin",
        name="Gobelin vétéran",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 260, "mana_max": 0, "power": 60, "speed": 15, "defense": 12}, 
        skills = [get_skill("spear_thrust")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),


#-------------------------------------------------- FORET -----------------------------------------------------

# =============================================== ARAIGNEES
    Enemy(
        id="black_spider",
        name="Araignée noire",
        rarity="common",
        tier=1,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 10, "defense": 7}, 
        skills = [get_skill("bite")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=15
    ),

    Enemy(
        id="black_widow",
        name="Veuve noire",
        rarity="uncommon",
        tier=2,
        base_stats={"life_max": 200, "mana_max": 0, "power": 40, "speed": 20, "defense": 10}, 
        skills = [get_skill("bite")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=25
    ),

    Enemy(
        id="recluse",
        name="Recluse",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 240, "mana_max": 0, "power": 50, "speed": 25, "defense": 15}, 
        skills = [get_skill("bite")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),

# =============================================== CORBEAUX

    Enemy(
        id="sick_raven",
        name="Corbeau Malade",
        rarity="common",
        tier=1,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 10, "defense": 7}, 
        skills = [get_skill("peck")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=15
    ),

    Enemy(
        id="sick_great_raven",
        name="Grand Corbeau Malade",
        rarity="uncommon",
        tier=2,
        base_stats={"life_max": 250, "mana_max": 0, "power": 40, "speed": 10, "defense": 10}, 
        skills = [get_skill("peck")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=25
    ),

    Enemy(
        id="putrid_great_raven",
        name="Grand Corbeau Putride",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 260, "mana_max": 0, "power": 50, "speed": 15, "defense": 7}, 
        skills = [get_skill("peck")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),

    Enemy(
        id="werewolf",
        name="Loup-garou",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 260, "mana_max": 0, "power": 50, "speed": 15, "defense": 10}, 
        skills = [get_skill("rage")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),

    Enemy(
        id="baby_samuel",
        name="Bébé Samuel",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 260, "mana_max": 0, "power": 40, "speed": 20, "defense": 5}, 
        skills = [get_skill("babys_wail")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),

# =============================================== BOSS

    Enemy(
        id="black_phillip",
        name="Black Phillip",
        rarity="epic",
        tier=4,
        base_stats={"life_max": 450, "mana_max": 200, "power": 60, "speed": 20, "defense": 20},

        skills=[
            get_skill("charge"),
            get_skill("dark_stare"),
            get_skill("black_flame")
        ], 

        rotation=[
            get_skill("charge"),
            get_skill("black_flame"),
            get_skill("dark_stare"),
            get_skill("black_flame")
        ],
        xp=80,
        is_sub_boss=True
    ),

    Enemy(
        id="the_vvitch",
        name="The VVitch",
        rarity="legendary",
        tier=5,
        base_stats={"life_max": 450, "mana_max": 200, "power": 60, "speed": 20, "defense": 20},

        skills=[
            get_skill("corruption"),
            get_skill("dark_ritual"),
            get_skill("sacrifice")
        ],

        rotation=[
            get_skill("corruption"),
            get_skill("dark_ritual"),
            get_skill("sacrifice"),
            get_skill("sacrifice")
        ],

        xp=100,
        is_boss=True
        ),

# =============================================== ORCS

    Enemy(
        id="grumpy_orc",
        name="Orc grognon",
        rarity="common",
        tier=1,
        base_stats={"life_max": 160, "mana_max": 0, "power": 25, "speed": 5, "defense": 4}, 
        skills = [get_skill("dull_thud")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=15
    ),

    Enemy(
        id="hot_tempered_orc",
        name="Orc colérique",
        rarity="uncommon",
        tier=2,
        base_stats={"life_max": 220, "mana_max": 0, "power": 35, "speed": 10, "defense": 10}, 
        skills = [get_skill("dull_thud")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=25
    ),

    Enemy(
        id="enraged_orc",
        name="Orc enragé",
        rarity="rare",
        tier=3,
        base_stats={"life_max": 260, "mana_max": 0, "power": 40, "speed": 12, "defense": 15}, 
        skills = [get_skill("dull_thud")],
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),
]