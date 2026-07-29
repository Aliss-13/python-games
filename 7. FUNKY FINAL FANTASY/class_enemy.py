from copy import deepcopy
from class_skill import get_skill



class Enemy:

    def __init__(
        self,
        id,
        name,
        rarity,
        tier,
        base_stats,
        skills,
        zone_progress,
        rotation=None,
        level=1,
        bonus=None,
        effects=None,
        xp=0,
        is_boss=False,
        is_sub_boss=False
    ):

        self.id = id
        self.name = name
        self.rarity = rarity
        self.tier = tier
        self.life = base_stats.get("life_max",0)
        self.mana = base_stats.get("mana_max",0)
        self.base_stats = base_stats
        self.level = level
        self.skills = skills or []
        self.zone_progress = zone_progress
        self.rotation = rotation or self.skills
        self.sr_index = 0
        self.bonus = bonus or {}
        self.effects = effects or []
        self.xp = xp
        self.is_boss = is_boss
        self.is_sub_boss = is_sub_boss
        self.defeated = False


    def to_dict(self):

        return {
            "id": self.id,
            "defeated": self.defeated
        }

    def __repr__(self):
        return f"{self.name} - {self.rarity}"


ENEMIES = [
# =============================================== GOBELINS

    Enemy(
        id="novice_goblin",
        name="Gobelin novice",
        rarity="common",
        tier=1,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 9, "defense": 5}, 
        skills = [get_skill("spear_thrust")],
        zone_progress = 1,
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
        zone_progress = 2,
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
        zone_progress = 3,
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
        zone_progress = 1,
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
        zone_progress = 1,
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
        zone_progress = 2,
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
        zone_progress = 1,
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
        zone_progress = 1,
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
        zone_progress = 2,
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
        zone_progress = 2,
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
        zone_progress = 2,
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),

# =============================================== BOSS

    Enemy(
        id="black_phillip",
        name="Black Phillip 🐐",
        rarity="epic",
        tier=4,
        base_stats={"life_max": 450, "mana_max": 200, "power": 60, "speed": 20, "defense": 20},

        skills=[
            get_skill("charge"),
            get_skill("dark_stare"),
            get_skill("black_flame")
        ],

        zone_progress = 4, 

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

        zone_progress = 6, 

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
        zone_progress = 1,
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
        zone_progress = 1,
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
        zone_progress = 2,
        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
        xp=35
    ),
]

def create_enemy(enemy_id):

    for enemy in ENEMIES:
        if enemy.id == enemy_id:
            return deepcopy(enemy)
    return None


def get_enemy_by_id(enemy_id, enemy_list):

    for enemy in enemy_list:
        if enemy.id == enemy_id:
            return enemy

    raise ValueError(f"Ennemi inconnu : {enemy_id}")

def get_live_enemies(enemy_team):
    return [enemy for enemy in enemy_team if enemy.life > 0]
  