class Event:

    def __init__(
        self,
        id,
        name,
        event_type,
        event_category="normal",
        progress=0,
        flag=None,
        enemies=None,
        repeatable=False,
        ignore_rarity=False,
        
    ):

        self.id = id
        self.name = name
        self.event_type = event_type
        self.progress = progress
        self.flag = flag
        self.enemies = enemies or []
        self.repeatable = repeatable
        self.ignore_rarity = ignore_rarity
        self.event_category = event_category
        



FOREST_EVENTS = {

    "strange_tree" : Event(
        id="strange_tree",
        name="Arbre étrange",
        event_type="discovery",
        event_category="normal",
        progress=1,
        flag="strange_tree",
    ),

    "abandoned_hut" : Event(
        id="abandoned_hut",
        name="Cabane abandonnée",
        event_type="discovery",
        event_category= "normal",
        progress=2,
        flag="abandoned_hut",
    ),

    "raven_attack" : Event(
        id="raven_attack",
        name="Attaque de corbeau",
        event_type="combat",
        event_category= "normal",
        enemies=["sick_raven", "sick_great_raven"],
        repeatable=True
    ),

    "spider_nest" : Event(
        id="spider_nest",
        name="Nid d'araignées",
        event_type="combat",
        event_category= "normal",
        enemies=["black_spider", "black_widow"],
        repeatable=True
    ),

    "rare_encounter" : Event(
        id="rare_encounter",
        name="Ennemi rare !",
        event_type="combat",
        event_category= "normal",
        enemies=["putrid_great_raven", "recluse", "werewolf", "doomed_baby_samuel"],
        repeatable=True,
        ignore_rarity=True
        ),

    "black_phillip_battle" : Event(
        id="black_phillip_battle",
        name="Combat contre Black Phillip",
        event_type="combat",
        event_category="sub_boss",
        enemies=["black_phillip"],
        ignore_rarity=True
    ),

    "the_vvitch_battle" : Event(
        id="the_vvitch_battle",
        name="Combat contre The VVitch",
        event_type="combat",
        event_category="boss",
        enemies=["the_vvitch"],
        ignore_rarity=True
        )
}


