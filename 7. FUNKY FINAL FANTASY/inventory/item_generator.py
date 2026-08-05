from inventory.data import ITEMS


def generate_item(item_id, item_level=1):

    if item_id not in ITEMS:
        return None

    data = ITEMS[item_id]

    if data["type"] == "base_craft":
        pass

    item = {
        "id": item_id,
        "name": data["name"],
        "description": data.get("description", ""),
        "type": data["type"],
        "rarity": data["rarity"],
        "quantity": 1,
        "item_level": item_level,
        "bonus": {},
        "cost": data.get("cost", 1) * item_level
    }

    if data["type"] == "equipment":

        item["slot"] = data.get("slot")
        item["class"] = data.get("class", [])

        for stat, value in data["bonus"].items():
            scaling = data.get("scaling", {}).get(stat, 0)
            item["bonus"][stat] = (value + int(item_level * scaling))

    return item