from class_skilleffect import SkillEffect
from loot_tables import FOREST_LOOTS
from copy import deepcopy



class Opponent:

    def __init__(
        self,
        id,
        name,
        tier,
        life,
        base_stats,
        level=1,
        skills=None,
        bonus=None,
        effects=None,
        attack_effects=None,
        loot_table=None,
        drop_rate=1,
        drop_count=(1, 1),
        rarity="common",
        xp=0
    ):

        self.id = id
        self.name = name
        self.tier = tier
        self.life = life
        self.base_stats = base_stats
        self.level = level
        self.skills = skills or []
        self.bonus = bonus or {}
        self.effects = effects or []
        self.attack_effects = attack_effects or []
        self.loot_table = loot_table
        self.drop_rate = drop_rate
        self.drop_count = drop_count
        self.rarity = rarity
        self.xp = xp
        self.defeated = False


    def to_dict(self):

        return {
            "id": self.id,
            "defeated": self.defeated
        }


OPPONENTS = [

# =============================================== GOBELINS

    Opponent(
        id="novice_goblin",
        name="Gobelin novice",
        tier=1,
        life=160,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 9, "defense": 5}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.3, 
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="common",
        drop_rate = 0.35,
        drop_count = (1, 1),
        rarity="common",
        xp=200
    ),

    Opponent(
        id="trained_goblin",
        name="Gobelin entraîné",
        tier=2,
        life=220,
        base_stats={"life_max": 220, "mana_max": 0, "power": 40, "speed": 12, "defense": 8}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="uncommon",
        drop_rate = 0.70,
        drop_count = (1, 2),
        rarity="uncommon",
        xp=300
    ),

    Opponent(
        id="veteran_goblin",
        name="Gobelin vétéran",
        tier=3,
        life=260,
        base_stats={"life_max": 260, "mana_max": 0, "power": 60, "speed": 15, "defense": 12}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="rare",
        drop_rate = 1.00,
        drop_count = (2, 3),
        rarity="rare",
        xp=300
    ),


#-------------------------------------------------- FORET -----------------------------------------------------

# =============================================== ARAIGNEES
    Opponent(
        id="black_spider",
        name="Araignée noire",
        tier=1,
        life=160,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 10, "defense": 7}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="common",
        drop_rate = 0.35,
        drop_count = (1, 1),
        rarity="common",
        xp=150
    ),

    Opponent(
        id="black_widow",
        name="Veuve noire",
        tier=2,
        life=200,
        base_stats={"life_max": 200, "mana_max": 0, "power": 40, "speed": 20, "defense": 10}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.5,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="uncommon",
        drop_rate = 0.70,
        drop_count = (1, 2),
        rarity="uncommon",
        xp=150
    ),

    Opponent(
        id="recluse",
        name="Recluse",
        tier=2,
        life=240,
        base_stats={"life_max": 240, "mana_max": 0, "power": 50, "speed": 25, "defense": 15}, 

        attack_effects=[
            SkillEffect(
                effect_id="poison",
                chance=0.6,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="rare",
        drop_rate = 1.00,
        drop_count = (2, 3),
        rarity="rare",
        xp=150
    ),

# =============================================== CORBEAUX

    Opponent(
        id="sick_raven",
        name="Corbeau Malade",
        tier=1,
        life=160,
        base_stats={"life_max": 160, "mana_max": 0, "power": 30, "speed": 10, "defense": 7}, 

        attack_effects=[
            SkillEffect(
                effect_id="melancholy",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="common",
        drop_rate = 0.35,
        drop_count = (1, 1),
        rarity="common",
        xp=150
    ),

    Opponent(
        id="sick_great_raven",
        name="Grand Corbeau Malade",
        tier=2,
        life=250,
        base_stats={"life_max": 250, "mana_max": 0, "power": 40, "speed": 10, "defense": 10}, 

        attack_effects=[
            SkillEffect(
                effect_id="melancholy",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="uncommon",
        drop_rate = 0.70,
        drop_count = (1, 2),
        rarity="uncommon",
        xp=200
    ),

    Opponent(
        id="putrid_great_raven",
        name="Grand Corbeau Putride",
        tier=3,
        life=260,
        base_stats={"life_max": 260, "mana_max": 0, "power": 50, "speed": 15, "defense": 7}, 

        attack_effects=[
            SkillEffect(
                effect_id="melancholy",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="rare",
        drop_rate = 1.00,
        drop_count = (2, 3),
        rarity="rare",
        xp=300
    ),

    Opponent(
        id="werewolf",
        name="Loup-garou",
        tier=3,
        life=260,
        base_stats={"life_max": 260, "mana_max": 0, "power": 50, "speed": 15, "defense": 10}, 

        attack_effects=[
            SkillEffect(
                effect_id="hemorrhage",
                chance=0.4,
                target="opponent"
            ),
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="rare",
        drop_rate = 1.00,
        drop_count = (2, 3),
        rarity="rare",
        xp=300
    ),

    Opponent(
            id="doomed_baby_samuel",
            name="Bébé Samuel",
            tier=3,
            life=230,
            base_stats={"life_max": 260, "mana_max": 0, "power": 50, "speed": 20, "defense": 5}, 
    
            attack_effects=[
                SkillEffect(
                    effect_id="hemorrhage",
                    chance=0.4,
                    target="opponent"
                ),
                
                SkillEffect(
                    effect_id="melancholy",
                    chance=0.3,
                    target="opponent"
                ),
            ],
    
            bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},
    
            loot_table = ["rare"],
            drop_rate = 1.00,
            drop_count = (2, 3),
            rarity="rare",
            xp=300
        ),

# =============================================== BOSS

    Opponent(
        id="black_phillip",
        name="Black Phillip 🐐",
        tier="sub_boss",
        life=350,
        base_stats={"life_max": 350, "mana_max": 0, "power": 50, "speed": 9, "defense": 12},
        skills=["charge", "corruption"],
        loot_table=["epic"],
        drop_rate = 1.00,
        drop_count = (3, 4),
        rarity="epic",
        xp=250
    ),

    Opponent(
        id="the_vvitch",
        name="The VVitch",
        tier="sub_boss",
        life=450,
        base_stats={"life_max": 450, "mana_max": 0, "power": 50, "speed": 9, "defense": 15},
        skills=["charge","corruption"],
        loot_table="boss",
        drop_rate = 1.00,
        drop_count = (3, 4),
        rarity="legendary",
        xp=250
        ),

# =============================================== ORCS

    Opponent(
        id="grumpy_orc",
        name="Orc grognon",
        tier=1,
        life=160,
        base_stats={"life_max": 160, "mana_max": 0, "power": 25, "speed": 5, "defense": 4}, 

        attack_effects=[
            SkillEffect(
                effect_id="stun",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="basic",
        drop_rate = 0.35,
        drop_count = (1, 1),
        rarity="common",
        xp=150
    ),

    Opponent(
        id="hot_tempered_orc",
        name="Orc colérique",
        tier=2,
        life=220,
        base_stats={"life_max": 220, "mana_max": 0, "power": 35, "speed": 10, "defense": 10}, 

        attack_effects=[
            SkillEffect(
                effect_id="stun",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="uncommon",
        drop_rate = 0.70,
        drop_count = (1, 2),
        rarity="uncommon",
        xp=200
    ),

    Opponent(
        id="enraged_orc",
        name="Orc enragé",
        tier=3,
        life=260,
        base_stats={"life_max": 260, "mana_max": 0, "power": 40, "speed": 12, "defense": 15}, 

        attack_effects=[
            SkillEffect(
                effect_id="stun",
                chance=0.3,
                target="opponent"
            )
        ],

        bonus = {"life_max": 0, "mana_max": 0, "power": 0,"speed": 0, "defense": 0},

        loot_table="rare",
        drop_rate = 1.00,
        drop_count = (2, 3),
        rarity="rare",
        xp=300
    ),

    
]

def create_opponent(opponent_id):

    for opponent in OPPONENTS:
        if opponent.id == opponent_id:
            return deepcopy(opponent)
    return None


def get_opponent_by_id(opponent_id, opponent_list):

    for opponent in opponent_list:
        if opponent.id == opponent_id:
            return opponent

    raise ValueError(f"Ennemi inconnu : {opponent_id}")
  