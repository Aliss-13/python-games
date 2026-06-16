STRUCTURES = {
    "campfire": {
        "label": "Feu de camp 🔥",
        "cost": {"🪵": 5, "🪨": 10},
        "desc": "Cuisson de la nourriture."
    },
    "shelter": {
        "label": "Abri 🛖 ",
        "cost": {"🪵": 10, "🪨": 15},
        "desc": "Meilleure récupération en dormant."
    },
    "sewing_machine": {
        "label": "Machine à coudre 🧵",
        "cost": {"🪵": 10, "🪨": 10},
        "desc": "Fabrication tissu et vêtements."
    },
    "faraday_cage": {
        "label": "Cage de Faraday 🌐",
        "cost": {"💰" : 10},
        "desc": "Protection contre les attaques."
    },
    "portable_shower": {
        "label": "Douche portative 🚿",
        "cost": {"🪵": 10, "🪢" : 5, "🟩" : 5},
        "desc": "+10 santé mentale par nuit."
    },
    "banjo": {
        "label": "Banjo 🪕",
        "cost": {"🪵": 10, "🪢" : 5, "🟩" : 1},
        "desc": "+5 santé mentale par jour."
    },
    "livestock": {
        "label": "Elevage 🐮",
        "cost": {"🪵": 10, "🪨": 10, "💰" : 5},
        "desc": "+1🥩  par nuit en toute saison."
    },
    "creamery": {
        "label": "Laiterie 🥛",
        "cost": {"🪵": 10, "🪨": 10, "🪢" : 5},
        "desc": "+1🥛  par jour en toute saison. Nécessite élevage."
    },
    "dairy": {
        "label": "Fromagerie 🧀",
        "cost": {"🪵": 10, "🪨": 10, "🪢" : 5, "🟩" : 5},
        "desc": "Affinage du fromage. Nécessite laiterie."
    }
}


TOOLS = {
    "axe": {
        "label": "Hache 🪓",
        "cost": {"🪵": 5, "🪨": 5},
        "desc": "Plus de 🪵  récolté."
    },
    "pickaxe": {
        "label": "Pioche ⛏️ ",
        "cost": {"🪵": 5, "🪨": 8},
        "desc": "Plus de 🪨  récoltées."
    },
    "knife": {
        "label": "Couteau de chasse 🗡️ ",
        "cost": {"🪵": 8, "🪨": 3},
        "desc": "Plus de 🥩  récoltée."
    },
    "scythe": {
        "label": "Faux 𓌜",
        "cost": {"🪵": 8, "🪨": 8},
        "desc": "Plus de 🌿  récoltées."
    }
}

STUFF = {
    "tête": {
        "label": "Chapeau 🎩",
        "cost": {"🟩": 1, "🪢": 2},
        "desc": "Protège du froid la nuit et l'hiver."
    },
    "corps": {
        "label": "Manteau 🧥",
        "cost": {"🟩": 3, "🪢": 6},
        "desc": "Protège du froid et de la faim la nuit et l'hiver."
    },
    "mains": {
        "label": "Gants 🧤",
        "cost": {"🟩": 1, "🪢": 1},
        "desc": "Moins de fatigue pendant les récoltes."
    },
    "pieds": {
        "label": "Bottes 🥾",
        "cost": {"🟩": 1, "🪢": 1, "🪵": 3},
        "desc": "Moins de fatigue pendant les récoltes."
    }

}

HOLLANDAIS_VOLANT = {
    "label" : "Hollandais Volant ⚓",
    "parts": [
        "⚙️ Engrenage étrange",
        "🔩 Hélice en acier trempé",
        "💎 Cristal énergétique",
        "⛓️ Turbine hydraulique",
        "☀️ Voile solaire",
        "🧭 Boussole ancestrale",
        "📜 Plans du Hollandais Volant"
        ],
    
    "cost" : 
        {
            "🟩" : 20, 
            "🪢" : 40, 
            "🪵" : 80,
            "🪨" : 40,
            "🧀" : 40
        },

    "desc": "On se tire ou bien ?."

    }

#============================ coût ===========================================
def can_pay(player, cost):
    return all(player.inventory.get(resource, 0) >= amt for resource, amt in cost.items())


def pay(player, cost):
    for resource, amount in cost.items():
        player.inventory[resource] -= amount


#============================ Hollandais Volant ===========================================
def build_flying_dutchman(player):

    if player.flying_dutchman:
        print("Déjà construit.")
        return False

    missing_parts = [
        part
        for part in HOLLANDAIS_VOLANT["parts"]
        if part not in player.flying_dutchman_parts
    ]

    if missing_parts:
        print("Il te manque des pièces :")
        for p in missing_parts:
            print("-", p)
        return False

    cost = HOLLANDAIS_VOLANT["cost"]

    # Vérification
    for resource, amount in cost.items():

        if resource in player.inventory:
            if player.inventory[resource] < amount:
                print(f"Pas assez de {resource}")
                return False

        elif resource in player.food:
            if player.food[resource] < amount:
                print(f"Pas assez de {resource}")
                return False

        else:
            print(f"Ressource inconnue : {resource}")
            return False

    # Paiement
    for resource, amount in cost.items():

        if resource in player.inventory:
            player.inventory[resource] -= amount

        elif resource in player.food:
            player.food[resource] -= amount

    player.flying_dutchman = True

    print("👻 Le Hollandais Volant se matérialise dans la brume...")
    print("🚢 Tu quittes ce monde.")
    print("🏆 VICTOIRE")

    return True


def menu_build_flying_dutchman(player):

    print("\n⚓ HOLLANDAIS VOLANT\n")

    for item, quantity in HOLLANDAIS_VOLANT["cost"].items():
        print(f"- {item} - {quantity}")

    build_flying_dutchman(player)

#============================ Construire, fabriquer, coudre ===========================================
def build(player, key):
    data = STRUCTURES[key]

    if player.structures[key]:
        print("Déjà construit.")
        return

    if not can_pay(player, data["cost"]):
        print("Pas assez de ressources.")
        return

    pay(player, data["cost"])
    player.structures[key] = True

    print(f"Nouvelle structure : {data['label']}.")


def craft(player, key):
    data = TOOLS[key]

    if player.tools[key]:
        print("Déjà fabriqué.")
        return

    if not can_pay(player, data["cost"]):
        print("Pas assez de ressources.")
        return

    pay(player, data["cost"])
    player.tools[key] = True

    print(f"Nouvel outil : {data['label']}.")


def sew(player, key):
    data = STUFF[key]

    if player.stuff[key]:
        print("Déjà cousu.")
        return

    if not can_pay(player, data["cost"]):
        print("Pas assez de ressources.")
        return

    pay(player, data["cost"])
    player.stuff[key] = True

    print(f"Garde-robe : {data['label']}.")

    
#============================ Menu Construire, fabriquer, coudre ===========================================
def menu_build(player, choix):

    options = [k for k in STRUCTURES if not player.structures[k]]

    if not options:
        print("Tout est déjà construit.")
        return

    for i, key in enumerate(options, 1):
        print(f"[{i}] {STRUCTURES[key]['label']} - {STRUCTURES[key]['cost']} - {STRUCTURES[key]['desc']}")

    try:
        choix = int(input("> ")) - 1

        if choix < 0 or choix >= len(options):
            print("Choix invalide")
            return

    except ValueError:
        print("Entrée invalide")
        return

    build(player, options[choix])


def menu_craft(player, choix):
    options = [k for k in TOOLS if not player.tools[k]]

    if not options:
        print("Tout est déjà fabriqué.")
        return

    for i, key in enumerate(options, 1):
        print(f"[{i}] {TOOLS[key]['label']} - {TOOLS[key]['cost']} - {TOOLS[key]['desc']}")

    try:
        choix = int(input("> ")) - 1

        if choix < 0 or choix >= len(options):
            print("Choix invalide")
            return

    except ValueError:
        print("Entrée invalide")
        return
    
    craft(player, options[choix])


def menu_sew(player, choix):
    options = [k for k in STUFF if not player.stuff[k]]

    if not options:
        print("Tout est déjà cousu.")
        return

    for i, key in enumerate(options, 1):
        print(f"[{i}] {STUFF[key]['label']} - {STUFF[key]['cost']} - {STUFF[key]['desc']}")

    try:
        choix = int(input("> ")) - 1

        if choix < 0 or choix >= len(options):
            print("Choix invalide")
            return

    except ValueError:
        print("Entrée invalide")
        return
    
    sew(player, options[choix])


