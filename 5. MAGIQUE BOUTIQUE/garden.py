import time
from colors_and_names import DIM, YELLOW, RESET, LIGHT_PINK
from garden_ingredients import INGREDIENTS


garden_levels = {
    1: ["herbe_lunaire", "champignon_sombre", "poussiere_etoile"],
    2: ["ecorce_ancienne", "eau_enchantee"],
    3: ["croc_feroce", "aile_de_fee"],
    4: [],
    5: ["pierre_noire", "aconit"],
    6: [],
    7: ["bezoard", "ecaille_dragon"]
}

class Garden:

    def __init__(self, garden_levels):
        self.level = 1
        self.garden_levels = garden_levels

        self.ingredients = {
            ingredient: {
                "count": 0,
                "unlocked": False,
                "rate_modifier": 1,
                "last_update": time.time()
            }
            for ingredient in INGREDIENTS
        }

        # unlock initial level
        self.unlock_up_to_level(1)


    def to_dict(self):
        return {
            "level": self.level,
            "garden_levels": self.garden_levels,
            "ingredients": {
                ingredient: {
                    "count": data["count"],
                    "unlocked": data["unlocked"],
                    "rate_modifier": data["rate_modifier"],
                    "last_update": data["last_update"]
                }
                for ingredient, data in self.ingredients.items()
            }
        }


    def from_dict(self, data):
        self.level = data.get("level", 1)

        self.garden_levels.update(data.get("garden_levels", {}))

        saved = data.get("ingredients", {})

        now = time.time()

        self.ingredients = {}
        for k, default in INGREDIENTS.items():
            saved_data = saved.get(k, {})

            self.ingredients[k] = {
                "count": saved_data.get("count", 0),
                "unlocked": saved_data.get("unlocked", False),
                "rate_modifier": saved_data.get("rate_modifier", 1),
                "last_update": now
            }

        self.unlock_up_to_level(self.level)


    def unlock_up_to_level(self, level):
        
        self.level = level

        for lvl in range(1, level + 1):

            if lvl in self.garden_levels:

                for ingredient in self.garden_levels[lvl]:
                    self.ingredients[ingredient]["unlocked"] = True
                    self.ingredients[ingredient]["last_update"] = time.time()
    

def display_garden(garden):

    print("\n=== JARDIN MAGIQUE ===")
    print(f"{LIGHT_PINK}Niveau : {garden.level}{RESET}")

    for ingredient, data in garden.ingredients.items():

        if not data["unlocked"]:
            continue

        base_rate = INGREDIENTS[ingredient]["base_rate"]
        rate_modifier = data["rate_modifier"]

        effective_rate = max(0.5, base_rate / (rate_modifier ** 0.9))

        print(
            f"{YELLOW}{INGREDIENTS[ingredient]['name']}{RESET}"
            f" : {int(data['count'])}"
            f"{DIM} | {effective_rate:.1f}s{RESET}"
        )


def improve_garden(garden):

    for item, data in garden.ingredients.items():
        if data["unlocked"]:
            data["rate_modifier"] *= (1.01 + garden.level * 0.001)

    garden.level += 1

    garden.unlock_up_to_level(garden.level)


def update_garden(garden):

    now = time.time()

    for item, data in garden.ingredients.items():

        if not data["unlocked"]:
            continue

        elapsed = now - data["last_update"]


        base_rate = INGREDIENTS[item]["base_rate"]
        rate_modifier = data["rate_modifier"]
        effective_rate = max(0.5, base_rate / (rate_modifier ** 0.9))

        produced = int(elapsed // effective_rate)

        if produced > 0:
            data["count"] += produced

            # on conserve le "temps restant"
            data["last_update"] = now - (elapsed % effective_rate)

    return garden