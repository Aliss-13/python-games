import random

FOOD = {
    "🥩": {
        "label": "Nourriture crue 🥩",
        "effect": {
            "satiety": (5, 10),
            "stamina": (-10, +8), 
            "mentalhealth" : (-5, 2)
        },
        "random": True
    },
    "🍖": {
        "label": "Nourriture cuite 🍖",
        "effect": {"satiety" : 10, "stamina" : 10, "mentalhealth" : 5}
    },
    "🥛": {
        "label": "Lait 🥛",
        "effect": {"satiety" : 10, "stamina" : 10, "mentalhealth" : 20}
    },
    "🧀": {
        "label": "Fromage 🧀",
        "effect": {"satiety" : 50, "stamina" : 20, "mentalhealth" : 10}
    }

}

def eat(player, food_key):

    if food_key not in FOOD:
        print("❌ Aliment inconnu.")
        return False

    if player.food.get(food_key, 0) <= 0:
        print("❌ Il n'y en a plus.")
        return False

    food = FOOD[food_key]
    effect = food["effect"]

    applied_effects = {}  # 👈 on stocke ce qui a vraiment été appliqué

    for stat, value in effect.items():

        if isinstance(value, tuple):
            value = random.randint(*value)

        setattr(player, stat, getattr(player, stat) + value)
        applied_effects[stat] = value  # 👈 mémoire du résultat

    # clamp
    player.satiety = max(0, player.satiety_max)
    player.stamina = max(0, player.stamina_max)
    player.mentalhealth = max(0, player.mentalhealth_max)
    
    if not player.is_alive:
        return False

    player.food[food_key] -= 1

    # affichage propre
    print(f"🍽️  Tu consommes {food['label']}")

    for stat, value in applied_effects.items():
        if stat == "satiety":
            print(f"😋  Satiété : {value}")
        elif stat == "stamina":
            print(f"⚡ Endurance : {value}")
        elif stat == "mentalhealth":
            print(f"🧠 Santé mentale : {value}")
    
    return True


def menu_eat(player):
    options = [k for k in FOOD if not player.food[k] <= 0]

    for i, key in enumerate(options, 1):
        print(f"[{i}] {FOOD[key]['label']} - Faim : {FOOD[key]['effect']['satiety']} - Endurance : {FOOD[key]['effect']['stamina']} - Santé mentale : {FOOD[key]['effect']['mentalhealth']}")

    try:
        choix = int(input("> ")) - 1

        if choix < 0 or choix >= len(options):
            print("Choix invalide")
            return
        
    except ValueError:
        print("Entrée invalide")
        return

    eat(player, options[choix])
        

        