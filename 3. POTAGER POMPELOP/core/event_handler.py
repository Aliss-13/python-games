def handle_events(events):

    if not events:
        return

    for event in events:
        if not isinstance(event, dict):
            print(f"⚠️ Event invalide ignoré : {event}")
            continue

        if "type" not in event:
            print(f"⚠️ Event sans type ignoré : {event}")
            continue

        handler = EVENT_HANDLERS.get(event["type"])

        if handler:
            handler(event)
        else:
            print(f"⚠️ Event inconnu : {event['type']}")

def handle_level_up(event):
    print(f"LEVEL UP ! Niveau {event['niveau']}")

def handle_money_gain(event):
    print(f"+{event['amount']} pièces")

def handle_command_expired(event):
    print(f"Commande {event['id']} expirée")

def handle_loot_received(event):
    print(f"🧺 Tu as obtenu : {event['item']}")

def handle_plant_removed(event):
    print(f"Plante supprimée ({event['reason']})")

def handle_plant_seed(event):
    print(
        f"🌱 Plantation : "
        f"{event['quantite']} x {event['graine_nom']}"
    )

def handle_unlock_seed(event):
    print(f"🌱 Nouvelle graine débloquée : niveau {event['seed']}")

def handle_potager_upgraded(event):
    print(f"Potager amélioré : {event['new_size']} places !")
    print(f"Tu as dépensé {event['cost']} pièces.")

def handle_command_completed(event):
    print(
        f"Commande {event['id']} validée ✔ "
        f"(+{event['xp']} XP, +{event['pieces']} pièces)"
    )

def handle_item_bought(event):
    print(
        f"Achat : {event['item']} "
        f"({event['price']} pièces)"
    )


EVENT_HANDLERS = {
    "level_up": handle_level_up,
    "money_gain": handle_money_gain,
    "command_expired": handle_command_expired,
    "command_completed" : handle_command_completed,
    "loot_received": handle_loot_received,
    "plant_removed": handle_plant_removed,
    "potager_upgraded": handle_potager_upgraded,
    "plant_seed" : handle_plant_seed,
    "unlock_seed" : handle_unlock_seed,
    "item_bought" : handle_item_bought
}


