from city_state import city, check_city_level
from buildings import buildings
from ui import display_all_buildings, display_build_menu, display_needs


def next_day():

    city["day"] += 1

    # --- PRODUCTION ---
    for b, qty in city["buildings"].items():

        production = buildings[b].get("production", {})

        for resource, amount in production.items():
            if resource in city:
                city[resource] += int(amount * qty * city["production_bonus"])

    # --- FOOD / WATER / HYGIENE ---
    food_needed = city["population"]
    water_needed = city["population"]

    # gestion nourriture
    city["food"] -= food_needed

    if city["food"] < 0:
        city["happiness"] -= 10
        city["food"] = 0
        

    # gestion hygiène - LEVEL 2
        
        bath_capacity = city["buildings"].get("bath", 0) * 20

        if city["population"] > bath_capacity:
            city["happiness"] -= (city["population"] - bath_capacity) // 5
            city["happiness"] = max(0, city["happiness"])

        # coût d’entretien
        city["water"] -= city["buildings"].get("bath", 0)
        city["water"] = max(0, city["water"])

    # gestion eau
    city["water"] -= water_needed

    if city["water"] < 0:
        city["happiness"] -= 15
        city["water"] = 0


    if city["happiness"] == 0:
        print("GAME OVER")


    # --- EVOLUTION POPULATION ---
    if (city["population"] < city["housing_capacity"]
    and city["food"] > city["population"]
    and city["water"] > city["population"]
    and city["happiness"] > 50):

        city["population"] += 1

def run_game():
    
    print("------ ”(SIM CITY LIQUICITY)“ ------")
    print("La simulation préférée de tous les politiques !")
    print("")

    while True:
        
        # Ville
        print(
            f"-------------------------------------" 
            f"\nJour {city['day']}"
            f"\nPopulation : {city['population']}" 
            f"\nBonheur : {city['happiness']}"
            f"\n-------------------------------------")
        display_needs()
        print("-------------------------------------")
        display_all_buildings()

        # Actions joueur
        display_build_menu()
        

        # Jour suivant
        next_day()
        check_city_level()


if __name__ == "__main__":
    run_game()