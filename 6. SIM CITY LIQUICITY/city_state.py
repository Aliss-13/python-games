city = {
    "day": 1,
    "population": 10,
    "housing_capacity": 10,
    "level": 1,
    "food": 50, 
    "water" : 30,
    "wood": 20,
    "happiness": 100,
    "buildings": {"lumberjack": 1},
    
    "production_bonus": 1,
    
    "unlocked_buildings": ["farm", "fountain", "lumberjack", "house"]
}


resource_data = {
    "food": {
        "name": "Nourriture",
        "unlocked": True
    },
    "water": {
        "name": "Eau",
        "unlocked": True
    },
    "wood": {
        "name": "Bois",
        "unlocked": True
    }
}


def check_city_level():
    
    if city["population"] >= 20 and city["level"] == 1:
        unlock_level_2()


def unlock_level_2():

    if city["level"] >= 2:
        return
     
    city["level"] = 2
    print("🏙️ Niveau 2 débloqué ! La ville évolue.")

    # 1. Bonus de production
    city["production_bonus"] = 1.5

    # 3. Déblocage du bâtiment bath
    if "bath" not in city["unlocked_buildings"]:
        city["unlocked_buildings"].append("bath")

    print("✔ Production boostée (+50%)")
    print("✔ Bains publics disponibles")

    