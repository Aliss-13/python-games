import random
from display import display_enemy, display_enemy_light, display_loot
from ui import separator, header, separator_bis
from class_enemy import create_enemy, ENEMIES
from skill_engine import execute_skill
from class_skillcontext import SkillContext
from class_combatcontext import CombatContext
from effects import start_of_turn
from level import scale_enemy_team, level_up, xp_required
from loot_tables import generate_loot, add_loot
from inventory import get_stats
from class_savemanager import SaveManager
from menu_combat import menu_tour
from class_zone import explore, add_zone_progress_combat
from class_effect import remove_effect_malus, remove_effect_bonus
from display import display_character, display_discovery
from class_gameevent import GameEvent
from class_quest import process_game_event

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
    header(f"Tour de {character.name}")

    display_character(character)

    if character.life <= 0:
        print(f"{character.name} est mort !")
        return

    menu_tour(context, character)


def play_entity_turn(context, entity):

    if entity.life <= 0:
        return

# if not manage

    if entity in context.player_team:
        character_turn(context, entity)

        if not manage_start_of_turn(entity):
            return

    else:
        enemy_turn(context, entity)

        if not manage_start_of_turn(entity):
            return


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

        stats = get_stats(character)

        if character.life > 0:

            character.life = min(
                character.life + stats["life_max"] * 0.2,
                stats["life_max"]
            )

            if character.mana is not None:

                character.mana = min(
                    character.mana + stats["mana_max"] * 0.3,
                    stats["mana_max"]
                )

        for effect in character.effects:
            remove_effect_bonus(character, effect)
            remove_effect_malus(character, effect)
                
        character.effects.clear()
                        
        print("✨ Votre équipe récupère !")
        

def restore_team_after_combat(player_team):

    for character in player_team:

        stats = get_stats(character)

        character.life = stats["life_max"]

        if character.mana is not None:
            character.mana = stats["mana_max"]

        for effect in character.effects:
            remove_effect_bonus(character, effect)
            remove_effect_malus(character, effect)

        character.effects.clear()
        
    print("✨ Votre équipe récupère tous ses PV et son mana.")


def register_defeated_enemies(game, context):

    for enemy in context.enemy_team:

        if enemy.life <= 0:

            context.zone.enemy_kills[enemy.id] = (context.zone.enemy_kills.get(enemy.id, 0) + 1)

            event = GameEvent("kill", enemy.id)
            process_game_event(game, event)

        add_zone_progress_combat(context.zone, enemy)


def handle_defeated_enemies(game, context):

    loot = []

    for enemy in context.enemy_team:

        if is_dead(enemy):
            separator_bis()
            print(f"{enemy.name} disparaît !")
            enemy.defeated = True

            register_defeated_enemies(game, context)
            separator_bis()
            gain_xp_combat(context)

            loot.extend(generate_loot(enemy, context.zone))

    add_loot(game.inventory, loot)
    separator_bis()
    display_loot(loot)

    return loot


def is_dead(entity):
    return entity.life <= 0


def remove_dead_entities(context):
    for enemy in context.enemy_team:
        if is_dead(enemy):
            enemy.defeated = True


def result_explore(game):

    result = explore(game.current_zone, game)

    if not result:
        return None

    if result["type"] == "discovery":
        display_discovery(result["event"])

    elif result["type"] == "nothing":
        print("Il ne se passe rien...")

    return result


def prepare_combat(game):

    explore_result = result_explore(game)

    if explore_result is None:
        return None

    if explore_result["type"] != "combat":
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
        game=game,
        event=explore_result["event"]
    )


def end_combat(game, context):

    if context.is_sub_boss_fight:
        game.current_zone.sub_boss_defeated = True

    if context.is_boss_fight:
        game.current_zone.boss_defeated = True

    handle_defeated_enemies(game, context)
    
    restore_team_after_combat(game.player_team)

    SaveManager.save(game)
    
    print("Victoire totale !")
    

def combat(game, context=None):

    if context is None:
        context = prepare_combat(game)

    if context is None:
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


def gain_xp_combat(context):

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

                    level_up(character)

#----------------------------------------- Génération de l'équipe ennemie ----------------------------------------------

def generate_enemy_team(zone, event):

# Boss et sous-boss : toujours seuls

    if event.event_category in ["boss", "sub_boss"]:
        return [
            create_enemy(event.enemies[0])
        ]

    # ensuite seulement la logique normale
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