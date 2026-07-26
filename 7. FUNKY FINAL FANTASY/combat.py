import random
from display import display_enemy, display_enemy_light, display_loot
from ui import separator, header
from class_enemy import create_enemy, ENEMIES
from skill_engine import execute_skill
from class_skillcontext import SkillContext
from class_combatcontext import CombatContext
from effects import start_of_turn
from level import scale_enemy_team, unlock_skills, level_up, xp_required
from loot_tables import generate_loot, add_loot
from sac_a_dos import get_stats, calcul_stats
from class_savemanager import SaveManager
from menu_combat import menu_tour
from class_zone import explore

RARE_CHANCE = 0.05

#----------------------------------------- Ordre en fonction de la rapidité ----------------------------------------------

def speed_order(context: CombatContext):

    return sorted(
        context.get_live_entities(),
        key=lambda entity: (
            get_stats(entity)["speed"],
            random.random()
        ),
        reverse=True
    )

#----------------------------------------- Gestion des effets de début de tour ----------------------------------------------

def has_stun(entity):

    return any(
        effect.id == "stun"
        for effect in entity.effects
    )


def manage_start_of_turn(entity):

    start_of_turn(entity)

    if has_stun(entity):
        print(f"{entity.name} est immobilisé ⛔")
        return False

    return True

#----------------------------------------- Tours ----------------------------------------------

def choose_skill(enemy):

    skill = enemy.rotation[enemy.sr_index]

    enemy.sr_index += 1

    if enemy.sr_index >= len(enemy.rotation):
        enemy.sr_index = 0

    return skill


def enemy_turn(context, enemy):

    separator()
    header(f"Tour de {enemy.name}")

    display_enemy_light(enemy)

    skill = choose_skill(enemy)

    skill_context = SkillContext(
        caster=enemy,
        allies=context.enemy_team,
        enemies=context.player_team,
        skill=skill,
    )

    execute_skill(skill_context)


def character_turn(context, character):

    separator()
    
    if character.life <= 0:
        return

    header(f"Tour de {character.name}")
    calcul_stats(character)
    stats = get_stats(character)

    print(f"PV : {character.life}/{stats['life_max']}")

    if character.mana is not None:
        print(f"Mana : {character.mana}/{stats['mana_max']}")

    print(f"Puissance : {stats['power']}")
    print(f"Vitesse : {stats['speed']}")
    print(f"Défense : {stats['defense']}")
    
    menu_tour(context, character)


def play_entity_turn(context, entity):

    if entity.life <= 0:
        return

    if not manage_start_of_turn(entity):
        return

    if entity in context.player_team:
        character_turn(context, entity)

    else:
        enemy_turn(context, entity)


def one_turn(context : CombatContext):

    order = speed_order(context)

    for entity in order:

        # mort → skip
        if entity.life <= 0:
            continue

        play_entity_turn(context, entity)

        if not context.get_live_enemies():
            return "victoire"

        if not context.get_live_players():
            return "defaite"

    return "continuer"

#----------------------------------------- Combat ----------------------------------------------

def rest_after_combat(player_team):

    for character in player_team:

        if character.life > 0:
            character.life = min(
                character.life + character.base_stats["life_max"] * 0.2,
                character.base_stats["life_max"]
            )

            if character.mana is not None:
                character.mana = min(
                    character.mana + character.base_stats["mana_max"] * 0.3,
                    character.base_stats["mana_max"]
                )


def restore_team_after_combat(player_team):

    for character in player_team:

        character.life = character.base_stats["life_max"]
        
        if character.mana is not None:
            character.mana = character.base_stats["mana_max"]

        character.effects.clear()

    print("✨ Votre équipe récupère tous ses PV et son mana.")


def handle_defeated_enemies(context):

    loot = []

    for enemy in context.enemy_team:

        if is_dead(enemy):

            print(f"{enemy.name} disparaît !")

            loot.extend(
                generate_loot(enemy, context.zone)
            )

            enemy.defeated = True

    return loot


def is_dead(entity):
    return entity.life <= 0


def remove_dead_entities(context):
    for enemy in context.enemy_team:
        if is_dead(enemy):
            enemy.defeated = True


def prepare_combat(game):

    explore_result = explore(game.current_zone)

    if not explore_result or explore_result["type"] != "combat":
        return None

    enemy_team = generate_enemy_team(
        game.current_zone,
        explore_result["event"]
    )

    enemy_team = scale_enemy_team(
        game.player_team,
        enemy_team
    )

    return CombatContext(
        player_team=game.player_team,
        enemy_team=enemy_team,
        inventory=game.inventory,
        zone=game.current_zone,
        game=game
    )


def end_combat(game, context):

    if context.is_sub_boss_fight:
        game.current_zone.sub_boss_defeated = True

    if context.is_boss_fight:
        game.current_zone.boss_defeated = True

    loot = handle_defeated_enemies(context)
    
    add_loot(game.inventory, loot)
    
    display_loot(loot)

    gain_xp(context)

    restore_team_after_combat(game.player_team)

    SaveManager.save(game)
    
    print("Victoire totale !")
    

def combat(game):

    context = prepare_combat(game)

    if not context:
        return

    separator()
    
    for enemy in context.enemy_team:
        display_enemy(enemy)

    while context.get_live_enemies():

        turn_result = one_turn(context)

        if turn_result == "defaite":
            print("GAME OVER")
            return

        if turn_result == "victoire":
            end_combat(game, context)
            return


def gain_xp(context):

    for enemy in context.enemy_team:

        if is_dead(enemy):

            xp_reward = enemy.xp

            for character in context.player_team:
                character.xp += xp_reward

                print(
                    f"{character.name} gagne {xp_reward} XP !"
                )

                while character.xp >= xp_required(character.level):

                    character.xp -= xp_required(character.level)
                    character.level += 1

                    level_up(character)
                    unlock_skills(character)

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
            enemy for enemy in ENEMIES
            if enemy.id in event.enemies
        ]

    else:
        available = [
            enemy for enemy in ENEMIES
            if enemy.id in event.enemies
            and enemy.rarity in possible_rarity
        ]

    # On cherche d'abord les rares éventuels
    rare_enemies = [
        enemy for enemy in ENEMIES
        if enemy.id in event.enemies
        and enemy.rarity == "rare"
    ]

    # Chance d'apparition d'un rare
    if rare_enemies and random.random() < RARE_CHANCE:

        return [
            create_enemy(random.choice(rare_enemies).id)
        ]

    # Sinon équipe normale
    return [
        create_enemy(random.choice(available).id)
        for _ in range(enemy_count)
    ]