def handle_events(events, state):

    if not events:
        return

    for event in events:

        if not isinstance(event, dict):
            print(f"⚠️ Event invalide ignoré : {event}")
            continue

        event_type = event.get("type")

        if not event_type:
            print(f"⚠️ Event sans type ignoré : {event}")
            continue

        handler = EVENT_HANDLERS.get(event_type)

        if handler is None:
            print(f"⚠️ Event inconnu : {event_type}")
            continue

        if "data" in event:
            payload = event["data"]
        else:
            payload = {
                k: v
                for k, v in event.items()
                if k != "type"
            }

        handler(payload, state)

def handle_level_up(event, state):
    print(f"LEVEL UP ! Niveau {event['niveau']}")

def handle_money_gain(event, state):
    print(f"+{event['amount']} pièces")

def handle_loot_received(event, state):
    print(f"🧺 Tu as obtenu : {event['item']}")

def handle_plant_removed(event, state):
    print(f"Plante supprimée ({event['reason']})")

def handle_plant_seed(event, state):
    print(
        f"🌱 Plantation : "
        f"{event['quantite']} x {event['graine_nom']}"
    )

def handle_unlock_seed(event, state):
    print(f"🌱 Nouvelle graine débloquée : niveau {event['seed']}")

def handle_potager_upgraded(event, state):
    print(f"Potager amélioré : {event['new_size']} places !")
    print(f"Tu as dépensé {event['cost']} pièces.")
    
def handle_item_bought(event, state):
    print(
        f"Achat : {event['item']} "
        f"({event['price']} pièces)"
    )

def handle_command_expired(event, state):
    print(f"⌛️ Commande {event['id']} expirée !")

def handle_priority_command(event, state):
    print(f"🪧 Commande prioritaire !")

def handle_command_completed(event, state):
    
    value = event['xp'] + event['pieces'] * 0.5

    if event.get("prioritaire", True):
        value *= 1.5

    print(
        f"Commande {event['id']} :"
        f"+{event['xp']} XP, +{event['pieces']} pièces, +{int(value)} prestige pour ton potager ! You got to Pompélop 🎵"
    )
    
    




EVENT_HANDLERS = {
    "level_up": handle_level_up,
    "money_gain": handle_money_gain,
    "loot_received": handle_loot_received,
    "plant_removed": handle_plant_removed,
    "potager_upgraded": handle_potager_upgraded,
    "plant_seed" : handle_plant_seed,
    "unlock_seed" : handle_unlock_seed,
    "item_bought" : handle_item_bought,
    "command_completed" : handle_command_completed,  
    "command_expired": handle_command_expired,
    "priority_command" : handle_priority_command
}


