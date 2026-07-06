import time
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"
DIM = "\033[2m"
LIGHT_PINK = "\033[38;5;218m"
RESET = "\033[0m"


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
        self.garden_levels = data.get("garden_levels", self.garden_levels)

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
        for lvl in range(1, level + 1):
            if lvl in self.garden_levels:
                for ingredient in self.garden_levels[lvl]:
                    self.ingredients[ingredient]["unlocked"] = True
                    self.ingredients[ingredient]["last_update"] = time.time()
    

    def display_garden(self):

        print("\n=== JARDIN MAGIQUE ===")
        print(f"{LIGHT_PINK}Niveau : {self.level}{RESET}")

        for ingredient, data in self.ingredients.items():

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


    def improve_garden(self):

        for item, data in self.ingredients.items():
            if data["unlocked"]:
                data["rate_modifier"] *= (1.01 + self.level * 0.001)

        self.level += 1
        self.unlock_up_to_level(self.level)


    def update_garden(self):

        now = time.time()

        for item, data in self.ingredients.items():

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

        return self


          
    

INGREDIENTS = {

    "herbe_lunaire": {
        "name": "Herbe lunaire", 
        "base_rate": 5
        },

    "champignon_sombre": {
        "name": "Champignon sombre", 
        "base_rate": 8
        },

    "poussiere_etoile": {
        "name": "Poussière d'étoile",
        "base_rate": 30
        },

    "ecorce_ancienne": {
        "name": "Ecorce ancienne",
        "base_rate": 15
        },

    "eau_enchantee": {
        "name": "Eau enchantée", 
        "base_rate": 10
        },

    "croc_feroce": {
        "name": "Croc féroce",
        "base_rate": 20
        },

    "aile_de_fee": {
        "name": "Aile de fée", 
        "base_rate": 30
        },

    "pierre_noire": {
        "name": "Pierre noire", 
        "base_rate": 40
        },

    "aconit": {
        "name": "Aconit", 
        "base_rate": 50
        },

    "bezoard": {
        "name": "Bézoard", 
        "base_rate": 60
        },

    "ecaille_dragon": {
        "name": "Ecaille de dragon", 
        "base_rate": 70
        }

    }