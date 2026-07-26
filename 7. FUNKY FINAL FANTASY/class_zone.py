import random
from class_event import FOREST_EVENTS, Event
from loot_tables import LOOT_ZONES_PROFILES


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
        self.sub_boss_defeated = False

        self.boss_unlocked = False
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
            "sub_boss_defeated": self.sub_boss_defeated,
            "boss_unlocked": self.boss_unlocked,
            "boss_defeated": self.boss_defeated   
        }

    def load_state(self, data):

        self.progress = data["progress"]
        self.flags = data["flags"]
        self.discovered = data["discovered"]
        self.sub_boss_defeated = data["sub_boss_defeated"]
        self.boss_defeated = data["boss_defeated"]


    @property
    def difficulty(self):

        if self.progress < self.sub_boss_progress:
            return 1

        elif self.progress < self.boss_progress:
            return 2

        else:
            return 3


    def add_progress(self, amount):

        self.progress += amount

        print(f"+{amount} progression de zone")

        self.check_unlocks()



    def check_unlocks(self):

        if (
            self.progress >= self.sub_boss_progress
            and not self.sub_boss_unlocked
        ):
            self.sub_boss_unlocked = True
            print(f"⚔️ {self.sub_boss} est accessible !")


        if (
            self.progress >= self.boss_progress
            and self.sub_boss_defeated
            and not self.boss_unlocked
        ):
            self.boss_unlocked = True
            print(f"👑 {self.boss} est accessible !")


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

        sub_boss_progress=10,
        boss_progress=20
    )

]


def get_zone_by_id(zone_id, zones):

    for zone in zones:

        if zone.id == zone_id:
            return zone

    return None


current_zone = get_zone_by_id("dark_forest", ZONES)


def create_boss_event(boss_id):

    return Event(
        id=f"{boss_id}_battle",
        name=f"⚔️ Combat contre {boss_id}",
        event_type="combat",
        enemies=[boss_id],
        ignore_rarity=True,
        is_boss=True
    )


def choose_combat_event(zone):

    if (zone.boss_unlocked and not zone.boss_defeated):
        return create_boss_event(zone.boss)

    if (zone.sub_boss_unlocked and not zone.sub_boss_defeated):
        return create_boss_event(zone.sub_boss)

    return random.choice(list(zone.events.values()))


def explore(zone):

    if not zone.discovered:
        print(f"\n🌲 Vous entrez dans : {zone.name}")
        zone.discovered = True


    if zone.sub_boss_unlocked or zone.boss_unlocked:
        zone_event = choose_combat_event(zone)

    else:
        zone_event = random.choice(
            list(zone.events.values())
        )


    return resolve_event(zone, zone_event)


def resolve_event(zone, event):

    print(f"\n🌲 {event.name}")


    if event.event_type == "discovery":

        zone.add_progress(event.progress)

        print(f"+{event.progress} progression de zone")

        if (zone.progress >= zone.sub_boss_progress and not zone.sub_boss_unlocked):
            zone.sub_boss_unlocked = True
            print(f"\n⚔️ {zone.sub_boss} est désormais accessible !")


        if (
            zone.progress >= zone.boss_progress
            and zone.sub_boss_defeated
            and not zone.boss_unlocked
        ):

            zone.boss_unlocked = True

            print(f"\n👑 {zone.boss} est désormais accessible !")


        if event.flag and event.flag not in zone.flags:
            zone.flags.append(event.flag)

        return {"type": "discovery"}


    elif event.event_type == "combat":

        return {
            "type": "combat",
            "event": event
        }
        