from city_state import city, resource_data
from buildings import buildings, build


def display_all_buildings():

    if not city["buildings"]:
        print("Rien de construit.")
        return


    for item, qty in city["buildings"].items():

        if qty > 0:
        
            item_data = buildings[item]

            print(f"{item_data['name']} : {qty} ")
    print("")


def display_build_menu():

    print("\nConstructions disponibles : ")

    for index, building in enumerate(city["unlocked_buildings"], start=1):
        data = buildings[building]
        costs = ", ".join(f"{qty} {resource_data[resource]['name']}" for resource, qty in data["cost"].items())

        print(f"[{index}] {data['name']} ({costs})")
    
    print("[0] Retour")

    try:
        choix = int(input("> "))

        if not 1 <= choix <= len(city["unlocked_buildings"]):
            print("Entrée inexistante")
            return

    except ValueError:
        print("Entrée invalide")
        return

    item_selected = city["unlocked_buildings"][choix - 1]
    build(item_selected)


def display_needs():

    for resource, qty in city.items():
        if resource in resource_data:
            print(f"{resource_data[resource]['name']} : {qty}")