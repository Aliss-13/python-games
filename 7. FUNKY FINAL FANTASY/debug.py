from events.class_event import FOREST_EVENTS
from combat import prepare_combat, combat

def debug_combat(game):

    events = {
        "1": "raven_ambush",
        "2": "spider_nest",
        "3": "spider_tree",
        "4": "raven_attack",
        "5": "rare_encounter"
    }

    print("\n🧪 DEBUG COMBAT")
    
    for key, event_id in events.items():
        event = FOREST_EVENTS[event_id]
        print(f"[{key}] {event.name}")

    choice = input("\nCombat à tester : ")

    event_id = events.get(choice)

    if not event_id:
        print("❌ Choix invalide.")
        return

    event = FOREST_EVENTS[event_id]

    context = prepare_combat(game, event)

    print(
        "👹 Équipe générée :",
        [enemy.id for enemy in context.enemy_team]
    )

    if not context.enemy_team:
        print("❌ Aucun ennemi disponible.")
        return

    combat(context)