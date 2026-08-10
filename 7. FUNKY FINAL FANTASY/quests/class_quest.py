from protagonists.utils_enemies import get_enemy_by_id
from protagonists.data_enemies import ENEMIES


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


    def get_inventory_progress(self, game):

        progress = {}

        for item_id, required in self.objectives.items():

            quantity = 0

            for item in game.inventory:
                if item["id"] == item_id:
                    quantity += item.get("quantity", 1)

            progress[item_id] = quantity

        return progress



    def get_progress(self, game):

        if self.quest_type == "collect_items":
            return self.get_inventory_progress(game)

        if self.quest_type == "kill_each":

            progress = {}

            for enemy_id in self.objectives:

                enemy = get_enemy_by_id(enemy_id, ENEMIES)

                if enemy and enemy.is_unique:
                    progress[enemy_id] = (1 if enemy_id in game.defeated_unique_enemies else 0)

                else:
                    progress[enemy_id] = self.objectives_progress.get(enemy_id, 0)

            return progress

        if self.quest_type in ["kill_group", "discover_each"]:
            return self.objectives_progress

        return self.objectives_progress