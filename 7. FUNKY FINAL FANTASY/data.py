# dans Data, stocker uniquement des structures
# pas de fonction !

couleurs = {
    "common": "\033[90m",       # gris
    "uncommon": "\033[92m",   # vert
    "rare" : "\033[94m",        # bleu
    "epic": "\033[95m",       # violet
    "legendary" : "\033[93m",   # orange
    "reset" : "\033[0m"
}

RARITY = {
    "common": "commun",
    "uncommon": "inhabituel",
    "rare": "rare",
    "epic": "épique",
    "legendary": "légendaire"
}


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_PINK = "\033[38;5;218m"
PURPLE = "\033[95m"
RESET = "\033[0m"


inventory = [
    {
        "id": "phoenix_feather",
        "quantity": 1
    }
]

ITEMS = {
    "phoenix_feather": {
        "id": "phoenix_feather",
        "name": "Plume de phénix",
        "description": "Résurrection personnage avec 50 PV",
        "type": "consommable", 
        "rarity": "rare", 
        "effect": "resurrection",
        "healing": 50,
        "cost": 0
        },

    "invigorating_potion": {
        "id": "invigorating_potion",
        "name": "Potion revigorante",
        "description": "+80 PV",
        "type": "consommable", 
        "rarity": "uncommon", 
        "effect": "gain_life", 
        "healing": 80,
        "cost": 10
        },

    "power_gloves" : {
        "id": "power_gloves",
        "name": "Gants de puissance",
        "description": "+10 puissance",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "mains", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "cost": 20
        },

    "ring_of_domination" : {
        "id": "ring_of_domination",
        "name": "Anneau de domination",
        "description": "+10 puissance",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "mains", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "cost": 20
        },

    "shiny_gloves" : {
        "id": "shiny_gloves",
        "name": "Gants rutilants",
        "description": "+20 vie maximum",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "mains", 
        "rarity": "uncommon", 
        "bonus": {"life_max" : 20},
        "cost": 30
        },

    "winged_boots" : {
        "id": "winged_boots",
        "name": "Bottes ailées",
        "description": "+3 vitesse",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "pieds", 
        "rarity": "common", 
        "bonus": {"speed" : 3},
        "cost": 20
        },

    "red_shoes" : {
        "id": "red_shoes",
        "name": "Souliers rouges",
        "description": "+5 vitesse",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "pieds", 
        "rarity": "uncommon", 
        "bonus": {"speed" : 5},
        "cost": 30
        },

    "seven_league_boots" : {
        "id": "seven_league_boots",
        "name": "Bottes de 7 lieues",
        "description": "+7 vitesse",
        "type": "equipment", 
        "class": ["magic", "hand-to-hand"], 
        "slot": "pieds", 
        "rarity": "rare", 
        "bonus": {"speed" : 7},
        "cost": 40
        },

    "embroidered_robe" : {
        "id": "embroidered_robe",
        "name": "Robe brodée",
        "description": "+10 mana maximum",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "armure", 
        "rarity": "common", 
        "bonus": {"mana_max" : 10},
        "cost": 20
        },

    "wizard_robe" : {
        "id": "wizard_robe",
        "name": "Robe de sorcier",
        "description": "+20 mana maximum",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "armure", 
        "rarity": "uncommon", 
        "bonus": {"mana_max" : 20},
        "cost": 30
        },

    "force_field" : {
        "id": "force_field",
        "name": "Champ de force",
        "description": "+40 vie maximum",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "armure", 
        "rarity": "rare", 
        "bonus": {"life_max" : 40},
        "cost": 40
        },

    "radiance" : {
        "id": "radiance",
        "name": "Radiance",
        "description": "+60 vie maximum",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "armure", 
        "rarity": "epic", 
        "bonus": {"life_max" : 60},
        "cost": 70
        },

    "iron_sword" : {
        "id": "iron_sword",
        "name": "Epée de fer",
        "description": "+10 puissance brute",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "arme", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "cost": 20
        },

    "claymore" : {
        "id": "claymore",
        "name": "Claymore",
        "description": "+20 puissance brute",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "arme", 
        "rarity": "uncommon", 
        "bonus": {"power" : 20},
        "cost": 30
        },

    "scimitar" : {
        "id": "scimitar",
        "name": "Cimeterre",
        "description": "+40 puissance brute",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "arme", 
        "rarity": "rare", 
        "bonus": {"power" : 40},
        "cost": 40
        },

    "iron_breastplate" : {
        "id": "iron_breastplate",
        "name": "Plastron de fer",
        "description": "+20 vie maximum",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "armure", 
        "rarity": "common", 
        "bonus": {"life_max" : 20},
        "cost": 20
        },

    "shiny_breastplate" : {
        "id": "shiny_breastplate",
        "name": "Plastron rutilant",
        "description": "+30 vie maximum",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "armure", 
        "rarity": "uncommon", 
        "bonus": {"life_max" : 30},
        "cost": 30
        },

    "the_kings_breastplate" : {
        "id" : "the_kings_breastplate",
        "name": "Plastron du Roi",
        "description": "+40 vie maximum",
        "type": "equipment", 
        "class": ["hand-to-hand"], 
        "slot": "armure", 
        "rarity": "rare", 
        "bonus": {"life_max" : 40},
        "cost": 40
        },

    "shiny_staff" : {
        "id": "shiny_staff",
        "name": "Bâton brillant",
        "description": "+10 puissance magique",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "arme", 
        "rarity": "common", 
        "bonus": {"power" : 10},
        "cost": 20
        },

    "lunar_scepter" : {
        "id": "lunar_scepter",
        "name": "Sceptre lunaire",
        "description": "+20 puissance magique",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "arme", 
        "rarity": "uncommon", 
        "bonus": {"power" : 20},
        "cost": 30
        },

    "solar_orb" : {
        "id": "solar_orb",
        "name": "Orbe solaire",
        "description": "+30 puissance magique",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "arme", 
        "rarity": "rare", 
        "bonus": {"power" : 30},
        "cost": 40
        },

    "cosmic_vortex" : {
        "id": "cosmic_vortex",
        "name": "Vortex cosmique",
        "description": "+50 puissance magique",
        "type": "equipment", 
        "class": ["magic"], 
        "slot": "arme", 
        "rarity": "epic", 
        "bonus": {"power" : 50},
        "cost": 70
        }
    }

loot_tables = {
    "basic" : [
        {"id" : "winged_boots", "chance" : 0.8},
        {"id" : "power_gloves", "chance" : 0.8},
        {"id" : "embroidered_robe", "chance" : 0.6}, 
        {"id" : "iron_sword", "chance" : 0.5},
        {"id" : "shiny_staff", "chance" : 0.5},
        {"id" : "iron_breastplate", "chance" : 0.6},
        {"id" : "shiny_breastplate", "chance" : 0.2},
        {"id" : "claymore", "chance" : 0.2},
        {"id" : "wizard_robe", "chance" : 0.2},
        {"id" : "lunar_scepter", "chance" : 0.2}
        ],

    "improved" : [
        {"id" : "ring_of_domination", "chance" : 0.8},
        {"id" : "invigorating_potion", "chance" : 0.5},
        {"id" : "red_shoes", "chance" : 0.6}, 
        {"id" : "wizard_robe", "chance" : 0.5},
        {"id" : "lunar_scepter", "chance" : 0.5},
        {"id" : "shiny_breastplate", "chance" : 0.6},
        {"id" : "claymore", "chance" : 0.5},
        {"id" : "solar_orb", "chance" : 0.2},
        {"id" : "the_kings_breastplate", "chance" : 0.2}
        ],

    "rare" : [
        {"id" : "seven_league_boots", "chance" : 0.6},
        {"id" : "phoenix_feather", "chance" : 0.4},
        {"id" : "force_field", "chance" : 0.6}, 
        {"id" : "scimitar", "chance" : 0.5},
        {"id" : "lunar_scepter", "chance" : 0.5},
        {"id" : "solar_orb", "chance" : 0.6},
        {"id" : "the_kings_breastplate", "chance" : 0.6},
        {"id" : "cosmic_vortex", "chance" : 0.2},
        {"id" : "radiance", "chance" : 0.2}
        ]
}

player_team = []

enemy_team = []