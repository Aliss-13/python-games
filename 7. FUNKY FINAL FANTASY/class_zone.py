class Zone:

    def __init__(
        self,
        id,
        name,
        description,
        enemies,
        boss=None,
        recommended_level=1
    ):

        self.id = id
        self.name = name
        self.description = description
        self.enemies = enemies
        self.boss = boss
        self.recommended_level = recommended_level
        self.completed = False



ZONES = [

    Zone(
        id="dark_forest",
        name="Forêt obscure",
        description="Une forêt sombre, très sombre...",
        enemies=["sick_raven", "sick_great_raven", "putrid_great_raven", "black_spider", "black_widow", "recluse", "werewolf"],
        boss="the_vvitch",
        recommended_level=1,
    )
]


def get_zone_by_id(zone_id, zones):

    for zone in zones:
        if zone.id == zone_id:
            return zone

    return None


current_zone = get_zone_by_id("dark_forest", ZONES)