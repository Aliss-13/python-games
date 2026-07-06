import city_state

buildings = {
    "farm": {
        "name": "Ferme",
        "cost": {"wood": 5},
        "production": {"food": 5}
    },

    "fountain": {
        "name": "Fontaine",
        "cost": {"wood": 8},
        "production": {"water": 5}
    },

    "lumberjack": {
        "name": "Scierie",
        "cost": {"wood": 10},
        "production": {"wood": 3}
    },

    "house": {
        "name": "Maison",
        "cost": {"wood": 10},
        "capacity": {"population": 5}
    },

    "bath": {
        "name": "Bains publics",
        "cost": {"wood": 30},
        "capacity": {"population": 5}
    }
}


def build(building):
    print(city_state.city["buildings"])
    print(city_state.city["unlocked_buildings"])

    if building not in buildings:
        print("Ce bâtiment n'existe pas.")
        return
    
    if building not in city_state.city["unlocked_buildings"]:
        print("Bâtiment verrouillé.")
        return

    cost = buildings[building]["cost"]

    if city_state.city["wood"] < cost["wood"]:
        print("Pas assez de bois.")
        return

    city_state.city["wood"] -= cost["wood"]


    buildings_dict = city_state.city["buildings"]

    if building in buildings_dict:
        buildings_dict[building] += 1
    else:
        buildings_dict[building] = 1

    if building == "house":
        city_state.city["housing_capacity"] += 5

    print(f"Construction achevée : {buildings[building]['name']} !")
    print(city_state.city["buildings"])
    print(city_state.city["unlocked_buildings"])
    
    



        