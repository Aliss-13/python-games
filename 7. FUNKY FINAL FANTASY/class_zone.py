import random

from inventory.inventory import add_item
from inventory.data import ITEMS
from inventory.loot_tables import LOOT_ZONES_PROFILES

from events.class_gameevent import GameEvent    
from events.class_event import FOREST_EVENTS, Event 

from protagonists.data_enemies import ENEMIES
from protagonists.utils_enemies import get_enemy_by_id

from quests.quests import start_quest, process_game_event

from display import display_boss_name



class Zone:

    def __init__(
        self,
        id,
        name,
        description,
        events,
        loot_profile,
        enemies=None,
        rare_enemies=None,
        rare_chance=0.05,
        sub_boss=None,
        boss=None,
        flags=None,
        progress=0,
        recommended_level=1,
        sub_boss_progress=10,
        boss_progress=20,
    ):

        self.id = id
        self.name = name
        self.description = description

        # événements
        self.events = events

        # loot et scaling objets
        self.loot_profile = loot_profile
        self.min_item_level = loot_profile["item_level"][0]
        self.max_item_level = loot_profile["item_level"][1]

        # ennemis
        self.enemies = enemies or []
        self.enemy_kills = {}
        self.rare_enemies = rare_enemies or []
        self.rare_chance = rare_chance

        # boss
        self.sub_boss = sub_boss
        self.boss = boss

        self.sub_boss_progress = sub_boss_progress
        self.boss_progress = boss_progress

        self.sub_boss_unlocked = False
        self.boss_unlocked = False

        self.sub_boss_defeated = False
        self.boss_defeated = False

        # progression zone
        self.flags = flags or []
        self.progress = progress
        
        # découverte
        self.discovered = False

        # niveau conseillé
        self.recommended_level = recommended_level

        # état final
        self.completed = False


    def to_dict(self):

        return {
            "id": self.id,
            "progress": self.progress,
            "flags": self.flags,
            "discovered": self.discovered,
            "sub_boss_unlocked": self.sub_boss_unlocked,
            "boss_unlocked": self.boss_unlocked,
            "sub_boss_defeated": self.sub_boss_defeated,
            "boss_defeated": self.boss_defeated,
            "enemy_kills": self.enemy_kills,   
        }

    def load_state(self, data):

        self.progress = data.get("progress", 0)
        self.flags = data.get("flags", [])
        self.discovered = data.get("discovered", False)
        self.sub_boss_unlocked = data.get("sub_boss_unlocked", False)
        self.boss_unlocked = data.get("boss_unlocked", False)
        self.sub_boss_defeated = data.get("sub_boss_defeated", False)
        self.boss_defeated = data.get("boss_defeated", False)
        self.enemy_kills = data.get("enemy_kills", {})


    @property
    def difficulty(self):

        if self.progress < self.sub_boss_progress:
            return 1

        elif self.progress < self.boss_progress:
            return 2

        else:
            return 3


    def add_progress(self, amount):

        if amount <= 0:
            return

        self.progress += amount

        print(f"Vous gagnez +{amount} progression de zone !")

        self.check_unlocks()


    def check_unlocks(self):

        if (
            self.progress >= self.sub_boss_progress
            and not self.sub_boss_unlocked
        ):
            self.sub_boss_unlocked = True
            sub_boss = display_boss_name(self.sub_boss)
            print(f"⚔️ {sub_boss} est accessible !")


        if (
            self.progress >= self.boss_progress
            and self.sub_boss_defeated
            and not self.boss_unlocked
        ):
            self.boss_unlocked = True
            boss = display_boss_name(self.boss)
            print(f"👑 {boss} est accessible !")


ZONES = [

    Zone(
        id="dark_forest",
        name="Forêt obscure",
        description="Une forêt sombre, très sombre...",

        events = FOREST_EVENTS,

        loot_profile=LOOT_ZONES_PROFILES["dark_forest"],

        enemies=[
            "sick_raven",
            "sick_great_raven",
            "black_spider",
            "black_widow"
        ],

        rare_enemies=[
            "putrid_great_raven",
            "recluse",
            "werewolf",
            "doomed_baby_samuel"
        ],

        rare_chance=0.10,

        sub_boss="black_phillip",
        boss="the_vvitch",

        recommended_level=1,

        sub_boss_progress=20,
        boss_progress=35
    )

]


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

        # événements répétables (combats)
        if event.repeatable:
            available_events.append(event)


        # découvertes uniques
        elif event.event_type == "discovery":

            if event.flag not in zone.flags:
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
        