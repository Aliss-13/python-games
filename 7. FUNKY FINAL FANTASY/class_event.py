class Event:

    def __init__(
        self,
        id,
        name,
        event_type,
        progress=0,
        flag=None,
        enemies=None,
        ignore_rarity=False
    ):

        self.id = id
        self.name = name
        self.event_type = event_type
        self.progress = progress
        self.flag = flag
        self.enemies = enemies or []
        self.ignore_rarity = ignore_rarity



FOREST_EVENTS = {

    "strange_tree" : Event(
        id="strange_tree",
        name="Arbre étrange",
        event_type="discovery",
        progress=1,
        flag="strange_tree",
    ),

    "abandoned_hut" : Event(
        id="abandoned_hut",
        name="Cabane abandonnée",
        event_type="discovery",
        progress=2,
        flag="hut_found",
    ),

    "raven_attack" : Event(
        id="raven_attack",
        name="Attaque de corbeau",
        event_type="combat",
        enemies=["sick_raven", "sick_great_raven"],
    ),

    "spider_nest" : Event(
        id="spider_nest",
        name="Nid d'araignées",
        event_type="combat",
        enemies=["black_spider", "black_widow"],
    ),

    "rare_encounter" : Event(
        id="rare_encounter",
        name="Ennemi rare !",
        event_type="combat",
        enemies=["putrid_great_raven", "recluse", "werewolf", "doomed_baby_samuel"],
        ignore_rarity=True
        )
}


