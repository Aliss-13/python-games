import random
from display import display_opponent_light, display_opponent, display_loot, display_equipment, display_inventory
from ui import separator, header, section
from class_opponent import create_opponent, OPPONENTS
from class_character import get_live_characters
from class_skill import SKILL_FUNCTIONS, get_target_name
from skills import calculate_damage
from class_effect import create_effect, apply_choose_target
from effects import start_of_turn
from class_event import FOREST_EVENTS
from level import scale_enemy_team, gain_xp
from loot_tables import generate_loot, add_loot
from sac_a_dos import get_stats, calcul_stats, equip_from_inventory, use_item
from class_savemanager import SaveManager

def speed_order(player_team, opponent):
    
    tous = player_team + [opponent]
    return sorted(
    tous,
    key=lambda entite: (
        get_stats(entite)["speed"],
        random.random()
    ),
    reverse=True
)

#----------------------------------------- SOUS MENUS ----------------------------------------------

def menu_inventory(character, player_team, inventory):
    display_equipment(character)
    while True:
        
        display_inventory(inventory)
        print("")
        print("[1] Équiper")
        print("[2] Utiliser objet")
        print("[3] Retour")

        choix = input("> ")

        if choix == "1":
            equip_from_inventory(character, inventory)

        elif choix == "2":
            use_item(player_team, inventory)

        elif choix == "3":
            return

        else:
            print("Choix invalide")

def menu_tour(character, player_team, enemies, inventory):

    while True:

        section("Actions")
        print("[s] Skill")
        print("[i] Inventaire")
        print("[q] Fin du tour")

        choix = input("> ").lower()
       
        # SKILL
        if choix == "s":
            menu_skill(character, player_team, enemies)
            return "fin_tour"

     
        # INVENTAIRE
        elif choix == "i":
            menu_inventory(character, player_team, inventory)
            # on reste dans le tour

        # FIN VOLONTAIRE
        elif choix == "q":
            return "fin_tour"

        else:
            print("Choix invalide")


def menu_skill(character, allies, enemies):

    print(f"\nActions de {character.name}")

    for i, skill in enumerate(character.skills, start=1):
        print(f"{i}. {skill.name:<25} Coût : {skill.cost} - Cible {get_target_name(skill)}")
   
    print("0. Retour")

    while True:

        choix = input("> ")

        if choix.isdigit():

            choix = int(choix)

            if choix == 0:
                return None

            skill = character.skills[choix - 1]

            action = SKILL_FUNCTIONS.get(skill.id)

            if action is None:
                print(f"Compétence inconnue : {skill.id}")
                return

            action(character, allies, enemies, skill)
            return

        print("Choix invalide.")


#----------------------------------------- Gestion des effets de début de tour ----------------------------------------------

def manage_start_of_turn(entite):

    if any(effect.id == "stun" for effect in entite.effects):
        print(f"{entite.name} est immobilisé ⛔ et ne joue pas !")
        start_of_turn(entite)
        return False

    start_of_turn(entite)
    return True
   
def apply_opponent_effects(opponent, target):

    for attack_effect in opponent.attack_effects:

        if random.random() <= attack_effect.chance:
            effect = create_effect(
                    attack_effect.effect_id,
                    source=opponent

                )

            target.effects.append(effect) 

#----------------------------------------- Tours ----------------------------------------------

def opponent_turn(player_team, opponent):
    separator()
    header(f"Tour de {opponent.name}")
    if opponent.life <= 0:
        return
    
    if not manage_start_of_turn(opponent):
        return
    
    vivants = get_live_characters(player_team).copy()
    if not vivants:
        return
    
    display_opponent_light(opponent)

    target = apply_choose_target(player_team)

    if target is None:
        return

    damage = calculate_damage(opponent, target)

    target.life -= damage

    print(f"⚔ {opponent.name} → {target.name} : -{damage} PV")
        
    if target.life <= 0:
        target.life = 0
        print(f"{target.name} est mort.")
    
    else:
        print(f"{target.name} n'a plus que {target.life} PV !")
    
    # effets des attaques selon l'ennemi
    apply_opponent_effects(opponent, target)


def character_turn(character, player_team, enemies, inventory):
    separator()
    header(f"Tour de {character.name}")
    calcul_stats(character)
    stats = get_stats(character)
    
    print(f"PV : {character.life}/{stats['life_max']}")

    if character.mana is not None:
        print(f"Mana : {character.mana}/{stats['mana_max']}")
    print(f"Puissance : {stats['power']}") 
    print(f"Vitesse : {stats['speed']}")
    print(f"Défense : {stats['defense']}")

    if not manage_start_of_turn(character):
        return
    
    menu_tour(character, player_team, enemies, inventory)


def one_turn(opponent, player_team, enemies, inventory):
    ordre = speed_order(get_live_characters(player_team), opponent)

    for entite in ordre:
        # mort → skip
        if entite.life <= 0:
            continue
        if entite in player_team:
            character_turn(entite, player_team, enemies, inventory)
            if opponent.life <= 0:
                return "ennemi mort"
        else:
            opponent_turn(player_team, opponent)
            if all(character.life <= 0 for character in player_team):
                return "defaite"
    
    return "continuer"

#----------------------------------------- Combat ----------------------------------------------

def combat(player_team, enemy_team, inventory, zone):

    enemy_team = scale_enemy_team(player_team, enemy_team)

    for enemy in enemy_team:
        display_opponent(enemy)

        while enemy.life > 0:

            result = one_turn(enemy, player_team, enemy_team, inventory)

            if result == "ennemi mort":

                print(f"{enemy.name} disparaît !")
                loot = generate_loot(enemy, zone)
                display_loot(loot)
                add_loot(inventory, loot)
                gain_xp(player_team, enemy)
                enemy.defeated = True

                break


            elif result == "defaite":

                print("GAME OVER")
                return
            
    print("DEBUG ENEMY TEAM")
    for enemy in enemy_team:
        print(enemy, type(enemy))

    SaveManager.save(player_team, enemy_team, inventory)

    print("Victoire totale !")

#----------------------------------------- Génération de l'équipe ennemie ----------------------------------------------

def generate_enemy_team(zone, event):

    if zone.difficulty == 1:
        enemy_count = 1
        possible_rarity = ["common"]

    elif zone.difficulty == 2:
        enemy_count = random.choice([1, 2])
        possible_rarity = ["common", "uncommon"]

    else:
        enemy_count = random.choice([2, 3])
        possible_rarity = ["common", "uncommon"]

    if event.ignore_rarity:
        available = [
            enemy for enemy in OPPONENTS
            if enemy.id in event.enemies
        ]

    else:
        available = [
            enemy for enemy in OPPONENTS
            if enemy.id in event.enemies
            and enemy.rarity in possible_rarity
        ]

    # On cherche d'abord les rares éventuels
    rare_enemies = [
        enemy for enemy in OPPONENTS
        if enemy.id in event.enemies
        and enemy.rarity == "rare"
    ]

    # Chance d'apparition d'un rare
    if rare_enemies and random.random() < event.rare_chance:

        return [
            create_opponent(random.choice(rare_enemies).id)
        ]

    # Sinon équipe normale
    return [
        create_opponent(random.choice(available).id)
        for _ in range(enemy_count)
    ]