import random
from display import display_opponent_light, display_opponent, display_loot
from ui import separator, header
from class_opponent import get_available_opponents
from class_character import get_live_characters
from level import scale_opponent, generate_loot, add_loot, gain_xp
from class_effect import create_effect, apply_choose_target
from effects import start_of_turn
from menu import menu_tour
from sac_a_dos import get_stats, calcul_stats
from skills import calculate_damage
from save import save_game


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


def manage_start_of_turn(entite):

    if any(effect.id == "stun" for effect in entite.effects):
        print(f"{entite.name} est immobilisé ⛔ et ne joue pas !")
        start_of_turn(entite)
        return False

    start_of_turn(entite)
    return True
   


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


def apply_opponent_effects(opponent, target):

    for attack_effect in opponent.attack_effects:

        if random.random() <= attack_effect.chance:
            effect = create_effect(
                    attack_effect.effect_id,
                    source=opponent

                )

            target.effects.append(effect) 
            

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


def combat(player_team, enemy_pool, inventory):

    while enemy_pool:

        enemy_base = random.choice(get_available_opponents(enemy_pool)
)
        enemy = scale_opponent(player_team, enemy_base)

        enemy_team = [enemy]

        display_opponent(enemy)

        while enemy.life > 0:

            result = one_turn(enemy, player_team, enemy_team, inventory)

            if result == "ennemi mort":
                if result == "ennemi mort":
                    print(f"{enemy.name} est vaincu !")
                    loot = generate_loot(enemy)
                
                    display_loot(loot)
                    add_loot(inventory, loot)
                    gain_xp(player_team, enemy)
                    enemy_base.defeated = True
                    save_game(player_team, inventory, enemy_pool)
                
                    break
            
            if result == "defaite":
                print("GAME OVER")
                return
    
    print("Victoire totale !")