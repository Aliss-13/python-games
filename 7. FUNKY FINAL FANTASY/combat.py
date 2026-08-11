import random

from display import display_enemy, display_enemy_light, display_loot, display_character, header, separator

from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import create_enemy, get_enemy_by_id
from protagonists.get_stats import get_stats
from protagonists.level import scale_enemy_team, level_up, xp_required
from protagonists.status import is_dead

from quests.quests import process_game_event, add_loot
from quests.unlock_dialogues import unlock_dialogues_for_defeated_unique_enemies

from events.class_gameevent import GameEvent

from skills.skill_engine import execute_skill
from skills.class_skillcontext import SkillContext

from zones.utils_zones import explore
from zones.end_zone import is_zone_complete, display_zone_end

from effects.effects import start_of_turn, remove_effect_malus, remove_effect_bonus

from class_combatcontext import CombatContext

from class_savemanager import SaveManager

from inventory.loot_tables import generate_loot, generate_enemy_specific_loots
from inventory. inventory import menu_shop

from menu_combat import menu_tour


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
        
    print("")
    print("✨ Votre équipe récupère tous ses PV et son mana.")


def register_defeated_enemies(game, context):

    for enemy in context.enemy_team:

        if not is_dead(enemy):
            continue

        enemy.defeated = True

        if enemy.is_unique:
            if enemy.id not in game.defeated_unique_enemies:
                game.defeated_unique_enemies.append(enemy.id)

            unlock_dialogues_for_defeated_unique_enemies(
                game,
                enemy.id
            )

        context.zone.enemy_kills[enemy.id] = (
            context.zone.enemy_kills.get(enemy.id, 0) + 1
        )

        process_game_event(
            game,
            GameEvent("kill", enemy.id)
        )
    
    
def handle_defeated_enemies(game, context):

    loot = []

    for enemy in context.enemy_team:

        if is_dead(enemy):
            enemy.defeated = True

            gain_xp_combat(context)

            loot.extend(generate_loot(enemy, context.zone))
            loot.extend(generate_enemy_specific_loots(enemy))

    register_defeated_enemies(game, context)

    add_loot(game, loot)

    if loot:
        print("")
        display_loot(loot)

    if is_zone_complete(game):
        display_zone_end(game)

    return loot


def remove_dead_entities(context):
    for enemy in context.enemy_team:
        if is_dead(enemy):
            enemy.defeated = True


def handle_explore(game):

    result = explore(game.current_zone, game)

    if not result:
        return

    if result["type"] == "combat":

        context = prepare_combat(
            game,
            result["event"]
        )

        if context:
            combat(context)

    elif result["type"] == "shop":
        menu_shop(game)
        return

    elif result["type"] == "discovery":
        pass

    elif result["type"] == "collect":
        pass

    elif result["type"] == "nothing":
        print("Il ne se passe rien...")
        

def prepare_combat(game, event):

    DEBUG_ENEMY = None

    if DEBUG_ENEMY:
        enemy_team = [
            create_enemy(DEBUG_ENEMY)
        ]

    else:
        enemy_team = generate_enemy_team(
        game,
        game.current_zone,
        event
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
        event=event
    )


def end_combat(game, context):

    if context.is_sub_boss_fight:
        game.current_zone.sub_boss_defeated = True

    if context.is_boss_fight:
        game.current_zone.boss_defeated = True

    handle_defeated_enemies(game, context)
    
    restore_team_after_combat(game.player_team)

    SaveManager.save(game)
    

def combat(context):

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
            end_combat(context.game, context)
            return


def gain_xp_combat(context):

    for enemy in context.enemy_team:

        if is_dead(enemy):

            xp_reward = enemy.xp

            for character in context.player_team:
                character.xp += xp_reward
                print(f"{character.name} gagne {xp_reward} XP !")

            for character in context.player_team:
                while character.xp >= xp_required(character.level):
                    character.xp -= xp_required(character.level)
                    level_up(character)

#----------------------------------------- Génération de l'équipe ennemie ----------------------------------------------

def can_spawn_enemy(game, enemy):
    if enemy.is_unique and enemy.id in game.defeated_unique_enemies:
        return False
    
    return True


def generate_enemy_team(game, zone, event):

    # --------------------------------------------------
    # BOSS / SOUS-BOSS
    # --------------------------------------------------

    if event.event_category in ["boss", "sub_boss"]:

        enemy = get_enemy_by_id(event.enemies[0], ENEMIES)

        if enemy.is_unique and enemy.id in game.defeated_unique_enemies:
            return []

        return [create_enemy(enemy.id)]
    
    # --------------------------------------------------
    # ENNEMIS DISPONIBLES
    # --------------------------------------------------
    
    available_enemies = [
        enemy
        for enemy in ENEMIES
        if enemy.id in event.enemies
        and not (
            enemy.is_unique
            and enemy.id in game.defeated_unique_enemies
        )
    ]

    # --------------------------------------------------
    # ENNEMI RARE
    # --------------------------------------------------

    if event.event_category == "rare_combat":

        rare_available = [
            enemy
            for enemy in available_enemies
            if enemy.rarity == "rare"
        ]

        if not rare_available:
            return []
        
        team = [create_enemy(random.choice(rare_available).id)]

        return team
       
    # --------------------------------------------------
    # PARAMÈTRES DU COMBAT NORMAL
    # --------------------------------------------------

    if zone.difficulty == 1:
        enemy_count = 1
        possible_rarity = ["common"]

    elif zone.difficulty == 2:
        enemy_count = random.choice([2, 3])
        possible_rarity = ["common", "uncommon"]

    else:
        enemy_count = random.choice([2, 3])
        possible_rarity = ["common", "uncommon"]

    # --------------------------------------------------
    # ENNEMIS NORMAUX
    # --------------------------------------------------

    if event.ignore_rarity:

        available = [enemy for enemy in available_enemies if not enemy.is_unique]

    else:

        available = [
            enemy
            for enemy in available_enemies
            if enemy.rarity in possible_rarity
            and not enemy.is_unique
        ]

    # --------------------------------------------------
    # UNIQUE
    # --------------------------------------------------

    unique_available = [
        enemy
        for enemy in available_enemies
        if enemy.is_unique
        and enemy.rarity in possible_rarity
    ]

    if unique_available:
        enemy = random.choice(unique_available)
        return [create_enemy(enemy.id)]

    # --------------------------------------------------
    # ÉQUIPE NORMALE
    # --------------------------------------------------

    if not available:
        return []
    
    return [create_enemy(random.choice(available).id) for _ in range(enemy_count)]
    