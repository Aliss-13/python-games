class Quest:

    def __init__(
        self,
        id,
        name,
        description,
        quest_type,
        objectives=None,
        reward_xp=0,
        reward_items=None, 
        zone_progress=0
    ):

        self.id = id
        self.name = name
        self.description = description

        self.quest_type = quest_type
        self.objectives = objectives or {}

        if self.quest_type in ["kill_each", "collect_each", "discover_each"]:
            self.objectives_progress = {
                objective: 0 
                for objective in self.objectives
            }

        else:
            self.objectives_progress = {}

        self.progress = 0
        self.completed = False

        self.reward_xp = reward_xp
        self.reward_items = reward_items or []

        self.zone_progress = zone_progress


    def to_dict(self):

        return {
            "id": self.id,
            "progress": self.progress,
            "objectives_progress": self.objectives_progress,
            "completed": self.completed,
            "zone_progress": self.zone_progress,
            "reward_items": self.reward_items,
            
        }


    @classmethod
    def from_dict(cls, data, quest_database):

        quest_template = quest_database[data["id"]]

        quest = cls(
            id=quest_template.id,
            name=quest_template.name,
            description=quest_template.description,
            quest_type=quest_template.quest_type,
            objectives=quest_template.objectives,
            reward_xp=quest_template.reward_xp,
            reward_items=quest_template.reward_items, 
            zone_progress=quest_template.zone_progress
        )

        quest.progress = data.get("progress", 0)

        quest.objectives_progress = data.get(
            "objectives_progress", 
            {objective: 0 for objective in quest.objectives})
        
        quest.completed = data.get("completed", False)

        return quest


QUESTS_BY_TARGET = {
    "werewolf": "kill_the_werewolf",
    "baby_samuel": "free_baby_samuel",
    }

FOREST_QUESTS = {

    "help_build_the_community_hall": Quest(
        id="help_build_the_community_hall",
        name="Aidez à construire la salle du village",
        description=
        "Récoltez du bois pour aider le charpentier du village.",
        quest_type="collect_each",
        objectives= {"log": 10},
        reward_xp=50, 
        zone_progress=2
    ),

    "the_apple_pie": Quest(
        id="the_apple_pie",
        name="La tarte aux pommes",
        description=
        "Récoltez des pommes pour que Dame Lisse prépare sa fameuse tarte.",
        quest_type="collect_each",
        objectives= {"red_apple": 10},
        reward_xp=50, 
        zone_progress=2
    ),

    "spider_hunt": Quest(
        id="spider_hunt",
        name="Des nids un peu trop collants",
        description=
        "Tuer trois araignées géantes.",
        quest_type="kill_group",
        objectives= {
                        "targets": ["black_spider", "black_widow", "recluse"],
                        "required": 3
        },
        reward_xp=80, 
        zone_progress=5
    ),


    "raven_hunt": Quest(
        id="raven_hunt",
        name="Des corbeaux malades agressifs.",
        description=
        "Tuer trois corbeaux malades.",
        quest_type="kill_group",
        objectives={
                    "targets": ["sick_raven", "sick_great_raven", "putrid_great_raven"],
                    "required": 3
        },
        reward_xp=80,
        zone_progress=5
    ),


    "rare_enemies": Quest(
        id="rare_enemies",
        name="Monstres rares",
        description=
        "Tuer les quatre monstres rares : Bébé Samuel, Loup-garou, Recluse et Grand Corbeau Putride.",
        quest_type="kill_each",
        objectives={"baby_samuel": 1, "werewolf": 1, "putrid_great_raven": 1, "recluse": 1},
        reward_xp=150,
        zone_progress=15,
        reward_items=["nothingness"]
    ),


    "free_baby_samuel": Quest(
        id="free_baby_samuel",
        name="Libérer Bébé Samuel",
        description=
        "Samuel est possédé... Sauvez son âme de l'Enfer !",
        quest_type="kill_each",
        objectives={"baby_samuel": 1},
        reward_xp=80,
        zone_progress=5,
        reward_items=["cosmic_mittens"]
    ),


    "kill_the_werewolf": Quest(
        id="kill_the_werewolf",
        name="Eliminer le loup-garou",
        description=
        "Un loup-garou tue les villageois à chaque pleine lune...",
        quest_type="kill_each",
        objectives={"werewolf": 1},
        reward_xp=80,
        zone_progress=5,
        reward_items=["star_patterned_hose"]
    ),


    "forest_mysteries": Quest(
        id="forest_mysteries",
        name="Les mystères de la forêt",
        description=
        "Découvrir quatre lieux mystérieux de la forêt.",
        quest_type= "discover_each",
        objectives={"hut_found": 1, "strange_tree_found": 1, "stone_circle_found": 1, "dark_clearing_found": 1},
        reward_xp=50,
        zone_progress=15
    ),

    "the_seamstress": Quest(
        id="the_seamstress",
        name="La couturière",
        description=
        "Récupérer 5 champignons sombres, 3 soies d'araignée et 5 plumes noires pour aider l'apprentie couturière.",
        quest_type= "collect_each",
        objectives={"dark_mushroom": 5, "spider_silk": 3, "black_feather": 5},
        reward_xp=100,
        zone_progress=15,
        reward_items=["raven_dress"]
    )

}