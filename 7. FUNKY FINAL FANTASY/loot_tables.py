import random
from data import ITEMS
from item_generator import generate_item
from inventory import add_item


FOREST_LOOTS = {

    "common": [
        "iron_helmet",
        "black_hood",
        "power_gloves",
        "ring_of_domination",
        "chainmail_trousers",
        "black_trousers",
        "winged_boots",
        "embroidered_robe",
        "iron_breastplate",
        "iron_sword",
        "shiny_staff"
    ],

    "uncommon": [
        "invigorating_potion",
        "shiny_helmet",
        "mysterious_headband",
        "shiny_gloves",
        "immaculate_gloves",
        "iron_thigh_guard",
        "star_patterned_hose",
        "red_shoes",
        "wizard_robe",
        "shiny_breastplate",
        "claymore",
        "lunar_scepter"
    ],

    "rare": [
        "phoenix_feather",
        "great_golden_helm",
        "new_moon_tiara",
        "cosmic_mittens",
        "obsidian_ring",
        "levis_501",
        "seven_league_boots",
        "force_field",
        "the_kings_breastplate",
        "scimitar",
        "solar_orb",
    ],

    "epic": [
        "nothingness",
        "memento_mori",
        "dark_armor",
        "radiance",
        "light_infused_shoes",
        "black_phillips_signed_ring"
    ],

    "legendary": []
}


LOOT_ZONES_PROFILES = {

    "dark_forest": {

        "item_level": (1, 10),
        "loots": FOREST_LOOTS
    }
}

LOOT_ENEMIES_PROFILES = {

    "common": {

        "drop_rate": 0.35,
        "drop_count": (1, 1),

        "rarity_chances": {
            "common": 0.90,
            "uncommon": 0.09,
            "rare": 0.01
        }
    },


    "uncommon": {

        "drop_rate": 0.55,
        "drop_count": (1, 2),

        "rarity_chances": {
            "common": 0.60,
            "uncommon": 0.35,
            "rare": 0.05
        }
    },


    "rare": {

        "drop_rate": 0.80,
        "drop_count": (2, 3),

        "rarity_chances": {
            "common": 0.20,
            "uncommon": 0.50,
            "rare": 0.30
        }
    },


    "epic": {

        "drop_rate": 1,
        "drop_count": (2, 3),

        "rarity_chances": {
            "uncommon": 0.30,
            "rare": 0.30,
            "epic": 0.40
        }
    },

    "legendary": {
    
        "drop_rate": 1,
        "drop_count": (3, 4),

        "rarity_chances": {
            "rare": 0.20,
            "epic": 0.50,
            "legendary": 0.30
        }
    }
}


def scale_item_bonus(item, item_level): # utilisée dans create_loot_item

    if item["type"] != "equipment":
        return {}

    scaled_bonus = {}

    for stat, value in item["bonus"].items():
        scaled_bonus[stat] = int(value * (1 + (item_level - 1) * item["scaling"] * 0.1))

    return scaled_bonus


def create_loot_item(item_id, zone): # utilisée dans generate_loot

    base_item = ITEMS[item_id]
    zone_profile = LOOT_ZONES_PROFILES[zone.id]

    item_level = random.randint(
        *zone_profile["item_level"]
    )

    loot = {
        "id": item_id,
        "name": base_item["name"],
        "rarity": base_item["rarity"],
        "type": base_item["type"],
        "quantity": 1,
        "item_level": item_level
    }

    if base_item["type"] == "equipment":
        loot["bonus"] = scale_item_bonus(base_item, item_level)

    elif base_item["type"] == "consumable":
        loot["effect"] = base_item["effect"]
        loot["healing"] = base_item.get("healing", 0)

    return loot


def choose_rarity(chances):

    roll = random.random()

    current = 0

    for rarity, chance in chances.items():

        current += chance

        if roll <= current:
            return rarity

        
def generate_loot(enemy, zone):

    loot = []

    enemy_profile = LOOT_ENEMIES_PROFILES[enemy.rarity]
    zone_profile = LOOT_ZONES_PROFILES[zone.id]


    if random.random() > enemy_profile["drop_rate"]:
        return loot


    nb_loots = random.randint(*enemy_profile["drop_count"])


    for _ in range(nb_loots):

        rarity = choose_rarity(enemy_profile["rarity_chances"])

        items = zone_profile["loots"].get(rarity, [])

        if not items:
            continue

        item_id = random.choice(items)

        item_level = enemy.level

        item = generate_item(item_id, item_level)

        if item:
            loot.append(item)

    return loot


def add_loot(inventory, loot):

    for item in loot:
        add_item(inventory, item)
    





    