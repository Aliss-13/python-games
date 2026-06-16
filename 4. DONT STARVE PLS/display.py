RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def get_bar_color(current, maximum):

    ratio = current / maximum

    if ratio > 0.6:
        return "\033[92m"   # vert

    elif ratio > 0.3:
        return "\033[93m"   # jaune

    else:
        return "\033[91m"   # rouge
    
#============================ Etat world - joueur ===========================================

def display_stats(player, world):
    print(f"Jour : {world.day_count}")
    print(f"Saison : {world.season}")
    print(f"Moment : {world.time_of_day}")
    print(f"Actions restantes : {world.actions_remaining}")
    print(f"Zone : {world.current_area}")
    print("")
    display_winteriscoming(world)
    print("")
    display_bars(player)
    print("")

#============================ objectifs ===========================================
def display_objectifs(player, world):

    # survivre à l'hiver
    if not world.first_winter_survived:
        print("")
        print(f"{BLUE}1. Survis à l'hiver{RESET} ❄️")
        print("")
        print("Les bons conseils de Tonton Ned : ")
        print("")
        print("La nourriture et les plantes vont disparaître...")
        print("Puis la chaleur...")
        print("Puis la confiance en tes décisions...")
        print("Anticipe ! Tu as 30 jours pour te préparer.")
        print("")
    else:
        print(f"{GREEN}✔ 1. Survis à l'hiver accompli{RESET}")

    # explorer la carte
    if len(world.explored_areas) < len(world.areas):
        print(f"{BLUE}2. Explore la carte du monde{RESET} 🗺️")
        print("")
        print("Les bons conseils de Tonton Xav : ")
        print("")
        print("Plus t'explores, plus tu découvres des trucs !")
        print("Et surtout, moins on te retrouve...")
        print("")
    else:
        print(f"{GREEN}✔ 2. Carte entièrement explorée{RESET}")

    # fabriquer le hollandais volant
    needed = len(world.flying_dutchman_parts)
    have = len(player.flying_dutchman_parts)
    if have < needed:
        print(f"{BLUE}3. Construis le Hollandais Volant ({have}/{needed}){RESET} 🚢")
        print("")
        print("Les bons conseils de Tonton Jones : ")
        print("Si tu entends ton nom soufflé par la mer, tu as déjà perdu l'option « Retour à terre »...")
        print("Une rumeur parle d'un navire maudit capable de traverser les tempêtes...")
        print("On dit que ses pièces ne devraient jamais être réassemblées...")
        print("🎵🤘 Ohé ohé capitaine abandonné !🤘🎶 Hum pardon je m'égare.")
        print("Explore les environs de chaque zone de la carte pour récupérer les pièces détachées.")
        print("Tu auras aussi besoin de bois, de pierres, de corde et de tissu.")
        print("Ta réserve de nourriture devra être suffisante pour un long voyage.")
        print("")
    else:
        print(f"{GREEN}✔ 3. Hollandais Volant prêt{RESET}")

#============================ Joueur ===========================================

def display_inventaire(player):
    print("\nInventaire :")
    for item, quantity in player.inventory.items():
        if quantity !=0:
            print(f"- {item} : {quantity}")


def display_food(player):
    print("\nGarde-manger :")
    for item, quantity in player.food.items():
        if quantity !=0:
            print(f"- {item} : {quantity}")


def display_stuff(player):
    print("\nVêtements :")
    for item, clothing in player.stuff.items():
        print(f"{item} - {clothing}")


def display_flying_dutchman_parts(player):
    print("\nPièces en ta possession :")
    for part in player.flying_dutchman_parts:
        print(f"- {part}")


def display_bars_simple(player):

    display_gauges_simple("🍽️", player.satiety, player.satiety_max)
    display_gauges_simple("⚡", player.stamina, player.stamina_max)
    display_gauges_simple("🧠", player.mentalhealth, player.mentalhealth_max)


def display_bars(player):

    display_gauges("🍽️", player.satiety, player.satiety_max)
    display_gauges("⚡", player.stamina, player.stamina_max)
    display_gauges("🧠", player.mentalhealth, player.mentalhealth_max)


def display_gauges_simple(icon, current, maximum):

    percentage = (current / maximum) * 100

    color = get_bar_color(current, maximum)

    print(f"{icon} {color}{percentage:.0f}%{RESET}")


def display_gauges(icon, current, maximum):

    percentage = (current / maximum) * 100

    color = get_bar_color(current, maximum)

    barres = int(current / maximum * 20)
    vide = 20 - barres

    print(f"{icon} {color}{'█' * barres}{'.' * vide} {percentage:.0f}%{RESET}")

#============================ Arrivée hiver ===========================================

def display_winteriscoming(world):

    season_to_winter = {
        "automne": 0,
        "été": 10,
        "printemps": 20,
        "hiver": None
    }

    if world.season == "hiver":
        print("❄️  L'hiver est là ! Ned t'avait prévenu...")
        return

    remaining = (10 - world.season_day) + season_to_winter[world.season]

    print(f"❄️  L'hiver arrive dans {remaining} jours.")
    
#============================ Carte ===========================================
def display_area(world, area):

    if area == world.current_area:
        return f"📍 {area.upper()}"

    elif area in world.explored_areas:
        return area.upper()

    else:
        return "......."
    

def display_map(world):
    print("\n┌────────────────────── 🗺️ CARTE ──────────────────────┐")

    grotte = display_area(world, "grotte")
    montagne = display_area(world, "montagne")
    foret = display_area(world, "forêt")
    plaine = display_area(world, "plaine")
    desert = display_area(world, "désert")
    jungle = display_area(world, "jungle")
    riviere = display_area(world, "rivière")

    print(f"""
                [ {grotte} ]
                    |
                    |
                [ {montagne} ]
                    |
                    |
[ {jungle} ] -- [ {foret} ] -- [ {plaine} ] -- [ {desert} ]
    |                                               |
    |                                               |
    └─────────────────[ {riviere} ]───────────────────┘
""")