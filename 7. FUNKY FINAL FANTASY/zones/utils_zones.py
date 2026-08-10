import random

from inventory.inventory import add_item, unlock_shop
from inventory.data import ITEMS

from events.class_gameevent import GameEvent    
from events.class_event import Event 

from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import get_enemy_by_id

from quests.quests import process_game_event, start_quest


def get_zone_by_id(zone_id, zones):

    return next(
        (zone for zone in zones if zone.id == zone_id),
        None
    )

 
#---------------------------------------------------- Exploration -----------------------------------------

def explore(zone, game):

    if not zone.discovered:
        print(f"\nVous entrez dans : {zone.name}")
        zone.discovered = True


    if zone.boss_unlocked and not zone.boss_defeated:
        return resolve_event(zone, choose_combat_event(zone), game)

    if zone.sub_boss_unlocked and not zone.sub_boss_defeated:
        return resolve_event(zone, choose_combat_event(zone), game)


    available_events = []

    for event in zone.events.values():

        if event.event_type == "combat":

            if event.repeatable:
                available_events.append(event)

        elif event.flag not in zone.flags:
            available_events.append(event)

        elif event.event_type == "collect":
            if event.repeatable:
                available_events.append(event)

        elif event.event_type == "discovery":
            if event.flag not in zone.flags:
                available_events.append(event)

        elif event.event_type == "shop":
            if event.shop_id not in game.unlocked_shops:
                available_events.append(event)
    
    if not available_events:
        return {"type": "nothing"}

    zone_event = random.choice(available_events)

    return resolve_event(zone, zone_event, game)

#--------------------------------- Résolution des évènements (combats + découvertes) ------------------------

def resolve_event(zone, event, game):

    print(f"\n{event.name}")

    if event.start_quests:
        for quest_id in event.start_quests:
            start_quest(game, quest_id)

    if event.event_type == "discovery": #------------ découverte

        if event.flag and event.flag not in zone.flags:
            zone.flags.append(event.flag)

        game_event = GameEvent("discovery", event.flag)
        process_game_event(game, game_event)

        return {"type": "discovery", "event": event}


    if event.event_type == "collect": #------------ récolte

        item_data = ITEMS[event.target]

        item = {
            "id": event.target,
            "name": item_data["name"],
            "description": item_data["description"],
            "type": item_data["type"],
            "rarity": item_data["rarity"],
            "quantity": event.amount
        }

        add_item(game.inventory, item)
        
        print(f"🌿 Vous récoltez {item['name']} x{event.amount} !")

        process_game_event(
            game,
            GameEvent(
                event_type=event.event_type,
                target=event.target,
                amount=event.amount
            )
        )

        return {"type": "collect", "event": event}


    elif event.event_type == "combat": #------------ combat

        return {"type": "combat", "event": event}


    elif event.event_type == "shop": #------------ boutique

        if event.flag and event.flag not in zone.flags:
            zone.flags.append(event.flag)

        unlock_shop(game, event.shop_id)

        return {"type": "shop", "shop_id": event.shop_id, "event": event}

    else:
        raise ValueError(f"Type d'événement inconnu : {event.event_type}")

#---------------------------------------------------- Event combat et boss -----------------------------------------

def create_boss_event(boss_id, boss_type):

    boss = get_enemy_by_id(boss_id, ENEMIES)

    return Event(
        id=f"{boss_id}_battle",
        name=f"⚔️ Combat contre {boss.name}",
        event_type="combat",
        event_category=boss_type,
        enemies=[boss_id],
        ignore_rarity=True
    )


def choose_combat_event(zone):

    if zone.boss_unlocked and not zone.boss_defeated:
        return create_boss_event(
            zone.boss,
            "boss"
        )
    
    if zone.sub_boss_unlocked and not zone.sub_boss_defeated:
        return create_boss_event(
            zone.sub_boss,
            "sub_boss"
        )

    combat_events = [event for event in zone.events.values() if event.event_type == "combat"]

    return random.choice(combat_events)
        