class Event:

    def __init__(
        self,
        id,
        name,
        event_type,
        event_category="normal",
        target=None,
        amount=0,
        rewards=None,
        flag=None,
        enemies=None,
        repeatable=False,
        ignore_rarity=False,
        start_quests=None
    ):

        self.id = id
        self.name = name
        self.event_type = event_type
        self.event_category = event_category
        self.target=target
        self.amount=amount
        self.rewards = rewards
        self.flag = flag
        self.enemies = enemies or []
        self.repeatable = repeatable
        self.ignore_rarity = ignore_rarity
        self.start_quests = start_quests or []


def get_event_by_flag(flag, events):

    return next(
        (event for event in events.values() if event.flag == flag),
        None
    )

FOREST_EVENTS = {

    "village_shop_found" : Event(
        id="village_shop_found",
        name="Une petite boutique cachée",
        event_type="shop",
        target="village_shop",
        repeatable=False
    ),

    "strange_tree" : Event(
        id="strange_tree",
        name="Arbre étrange",
        event_type="discovery",
        event_category="normal",
        flag="strange_tree_found",
        start_quests=["forest_mysteries"]
    ),

    "abandoned_hut" : Event(
        id="abandoned_hut",
        name="Cabane abandonnée",
        event_type="discovery",
        event_category= "normal",
        flag="hut_found",
        start_quests=["forest_mysteries"]
    ),

    "stone_circle" : Event(
        id="stone_circle",
        name="Cercle de pierres",
        event_type="discovery",
        event_category="normal",
        flag="stone_circle_found",
        start_quests=["forest_mysteries"]
    ),
    
    "dark_clearing" : Event(
        id="dark_clearing",
        name="Clairière sombre",
        event_type="discovery",
        event_category= "normal",
        flag="dark_clearing_found",
        start_quests=["forest_mysteries"]
    ),

    "dark_mushroom_patch_1": Event(
        id="dark_mushroom_patch_1",
        name="Des champignons sombres poussent à côté d'une flaque.",
        event_type="collect",
        event_category="resource",
        target="dark_mushroom",
        amount=2,
        repeatable=True
    ),
    
    "dark_mushroom_patch_2": Event(
        id="dark_mushroom_patch_2",
        name="Des champignons sombres poussent près d'un arbre mort.",
        event_type="collect",
        event_category="resource",
        target="dark_mushroom",
        amount=2,
        repeatable=True
    ),

    "log_patch_1": Event(
        id="log_patch_1",
        name="Vous coupez du bois et vous faites des belles bûches.",
        event_type="collect",
        event_category="resource",
        target="log",
        amount=3,
        repeatable=True
    ),
        
    "log_patch_2": Event(
        id="log_patch_2",
        name="Vous sortez votre grosse hache et votre chemise à carreaux.",
        event_type="collect",
        event_category="resource",
        target="log",
        amount=2,
        repeatable=True
    ),

    "red_apples_patch_1": Event(
        id="red_apples_patch_1",
        name="Vous trouvez un beau panier en osier avec des belles pommes rouges dedans. Pas louche du tout, ça.",
        event_type="collect",
        event_category="resource",
        target="red_apple",
        amount=4,
        repeatable=True
    ),
            
    "red_apples_patch_1": Event(
        id="log_patch_2",
        name="Vous tombez sur un pommier rempli de pommes bien rouges. On est en plein hiver mais bon, vous les cueillez quand même...",
        event_type="collect",
        event_category="resource",
        target="red_apple",
        amount=4,
        repeatable=True
    ),

    "raven_attack" : Event(
        id="raven_attack",
        name="Attaque de corbeau",
        event_type="combat",
        event_category= "normal",
        enemies=["sick_raven", "sick_great_raven", "putrid_great_raven"],
        start_quests=["raven_hunt"],
        repeatable=True
    ),

    "spider_nest" : Event(
        id="spider_nest",
        name="Nid d'araignées",
        event_type="combat",
        event_category= "normal",
        enemies=["black_spider", "black_widow", "recluse"],
        start_quests=["spider_hunt"],
        repeatable=True
    ),

    "rare_encounter" : Event(
        id="rare_encounter",
        name="Ennemi rare !",
        event_type="combat",
        event_category= "normal",
        enemies=["putrid_great_raven", "recluse", "werewolf", "baby_samuel"],
        start_quests=["rare_enemies"],
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
        ignore_rarity=True,
        )
}


