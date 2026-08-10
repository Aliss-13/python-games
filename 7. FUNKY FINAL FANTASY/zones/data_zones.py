from inventory.loot_tables import LOOT_ZONES_PROFILES
from events.class_event import FOREST_EVENTS
from zones.class_zone import Zone

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

        sub_boss_progress=30,
        boss_progress=60,
        total_progress=70
    )

]