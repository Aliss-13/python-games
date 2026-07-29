from data import ITEMS
import random


def generate_item(item_id, item_level=1):

    if item_id not in ITEMS:
        return None

    data = ITEMS[item_id]

    item = {
        "id": item_id,
        "name": data["name"],
        "type": data["type"],
        "rarity": data["rarity"],
        "quantity": 1
    }


    if data["type"] == "equipment":

        item["item_level"] = item_level

        item["bonus"] = {}

        for stat, value in data["bonus"].items():

            scaling = data.get("scaling", {}).get(stat, 0)

            item["bonus"][stat] = (
                value + int(item_level * scaling)
            )


    return item