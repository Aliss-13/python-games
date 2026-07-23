import random
from data import ITEMS



FOREST_LOOTS = {
    "item_level": (1, 10),

    "items": {

        "common" : [
            {"id": "winged_boots", "chance": 0.8},
            {"id": "power_gloves", "chance": 0.8},
            {"id": "embroidered_robe", "chance": 0.6}, 
            {"id": "iron_sword", "chance": 0.5},
            {"id": "shiny_staff", "chance": 0.5},
            {"id": "iron_breastplate", "chance": 0.6},
            {"id": "shiny_breastplate", "chance": 0.2},
            {"id": "claymore", "chance": 0.2},
            {"id": "wizard_robe", "chance": 0.2},
            {"id": "lunar_scepter", "chance": 0.2}
        ],
    
    
        "uncommon" : [
            {"id": "ring_of_domination", "chance": 0.8},
            {"id": "invigorating_potion", "chance": 0.5},
            {"id": "iron_helmet", "chance": 0.4},
            {"id": "black_hood", "chance": 0.4},
            {"id": "chainmail_trousers", "chance": 0.3},
            {"id": "black_trousers", "chance": 0.3},
            {"id": "red_shoes", "chance": 0.6}, 
            {"id": "wizard_robe", "chance": 0.5},
            {"id": "lunar_scepter", "chance": 0.5},
            {"id": "shiny_breastplate", "chance": 0.6},
            {"id": "claymore", "chance": 0.5},
            {"id": "solar_orb", "chance": 0.2},
            {"id": "the_kings_breastplate", "chance": 0.2}
        ],
    
        "rare" : [
            {"id": "shiny_helmet", "chance": 0.4},
            {"id": "mysterious_headband", "chance": 0.4},
            {"id": "shiny_gloves", "chance": 0.4},
            {"id": "immaculate_gloves", "chance": 0.4},
            {"id": "iron_thigh_guard", "chance": 0.3},
            {"id": "star_patterned_hose", "chance": 0.3},
            {"id": "seven_league_boots", "chance": 0.6},
            {"id": "phoenix_feather", "chance": 0.4},
            {"id": "force_field", "chance": 0.6}, 
            {"id": "scimitar", "chance": 0.5},
            {"id": "lunar_scepter", "chance": 0.5},
            {"id": "solar_orb", "chance": 0.6},
            {"id": "the_kings_breastplate", "chance": 0.6},
            ],
    
        "epic" : [
            {"id": "great_golden_helm", "chance": 0.4},
            {"id": "new_moon_tiara", "chance": 0.4},
            {"id": "cosmic_mittens", "chance": 0.4},
            {"id": "obsidian_ring", "chance": 0.4},
            {"id": "seven_league_boots", "chance": 0.6},
            {"id": "light_infused_shoes", "chance": 0.3},
            {"id": "levis_501", "chance": 0.3},
            {"id": "phoenix_feather", "chance": 0.4},
            {"id": "force_field", "chance": 0.6},
            {"id": "the_kings_breastplate", "chance": 0.6}, 
            {"id": "scimitar", "chance": 0.5},
            {"id": "solar_orb", "chance": 0.6},
            {"id": "radiance", "chance": 0.4},
        ],

        "boss": [
            {"id": "dark_armor", "chance": 0.8},
            {"id": "memento_mori", "chance": 0.5},
            {"id": "nothingness", "chance": 0.5},
            {"id": "beyond_the_veil", "chance": 0.4},
            {"id": "black_phillips_signed_ring", "chance": 0.4},
        ]
    }
}


def scale_item_bonus(item, item_level):

    scaled_bonus = {}

    for stat, value in item["bonus"].items():

        scaled_bonus[stat] = int(
            value * (1 + (item_level - 1) * 0.15)
        )

    return scaled_bonus



def create_loot_item(item, zone):

    item_level = random.randint(
        zone.min_item_level,
        zone.max_item_level
    )

    base_item = ITEMS[item["id"]]

    return {
        "id": item["id"],
        "quantity": 1,
        "item_level": item_level,
        "bonus": scale_item_bonus(base_item, item_level)
    }


def generate_loot(enemy, zone):

    loot = []

    if random.random() > enemy.drop_rate:
        return loot

    table = zone.loot_profile["items"][enemy.loot_table]

    nb_loots = random.randint(
        enemy.drop_count[0],
        enemy.drop_count[1]
    )

    for _ in range(nb_loots):
        item = random.choice(table)
        loot.append(create_loot_item(item, zone))

    return loot


def add_loot(inventory, loot):

    for loot_item in loot:

        for item in inventory:

            if (
                item["id"] == loot_item["id"]
                and item["item_level"] == loot_item["item_level"]
            ):

                item["quantity"] += loot_item["quantity"]
                break

        else:
            inventory.append({
                "id": loot_item["id"],
                "quantity": loot_item["quantity"],
                "item_level": loot_item["item_level"]
            })





    