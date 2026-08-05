from combat import combat, generate_enemy_team, scale_enemy_team
from events.class_event import Event
from class_combatcontext import CombatContext
from protagonists.get_stats import get_stats
from protagonists.level import level_up

def debug_level(game, target_level):

    for character in game.player_team:

        while character.level < target_level:
            level_up(character)
            

def debug_enemy(game, enemy_id):

    print("\n========== DEBUG ==========")
    print(f"Combat contre : {enemy_id}")

    event = Event(
        id="debug",
        name="Combat test",
        event_type="combat",
        enemies=[enemy_id],
        ignore_rarity=True
    )

    enemy_team = generate_enemy_team(
        game.current_zone,
        event
    )

    enemy_team = scale_enemy_team(
        game.player_team,
        enemy_team
    )

    context = CombatContext(
        player_team=game.player_team,
        enemy_team=enemy_team,
        inventory=game.inventory,
        zone=game.current_zone,
        game=game,
        event=event
    )
    
    for character in game.player_team:
        print(
            f"{character.name} - "
            f"Niveau : {character.level} - "
            f"{get_stats(character)}"
        )

    for enemy in enemy_team:
        print(
            f"{enemy.name} - "
            f"Niveau {enemy.level} - "
            f"{get_stats(enemy)}"
        )

    print("===========================\n")

    combat(game, context)