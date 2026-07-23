class Event:

    def __init__(
        self,
        id,
        name,
        event_type,
        progress=0,
        flag=None,
        enemies=None
    ):

        self.id = id
        self.name = name
        self.event_type = event_type
        self.progress = progress
        self.flag = flag
        self.enemies = enemies or []



FOREST_EVENTS = [

    Event(
        id="strange_tree",
        name="Arbre étrange",
        event_type="discovery",
        progress=1,
        flag="strange_tree"
    ),

    Event(
        id="abandoned_hut",
        name="Cabane abandonnée",
        event_type="discovery",
        progress=2,
        flag="hut_found"
    ),

    Event(
        id="raven_attack",
        name="Attaque de corbeau",
        event_type="combat",
        enemies=["sick_raven", "sick_great_raven"]
    ),

    Event(
        id="spider_nest",
        name="Nid d'araignées",
        event_type="combat",
        enemies=["black_spider", "black_widow"]
    )

]


