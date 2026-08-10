class GameState:

    def __init__(
        self,
        player_team,
        enemy_team,
        inventory,
        current_zone,
        active_quests=None,
        completed_quests=None,
        defeated_unique_enemies=None,
        met_npcs=None,
        npcs_with_new_dialogue=None,
        unlocked_shops=None,
        gold=0
    ):
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.inventory = inventory
        self.current_zone = current_zone
        self.active_quests = active_quests or []
        self.completed_quests = completed_quests or []
        self.defeated_unique_enemies = defeated_unique_enemies or []
        self.met_npcs = met_npcs or []
        self.npcs_with_new_dialogue = npcs_with_new_dialogue or []   # nouveaux dialogues disponibles
        self.unlocked_shops = unlocked_shops or []
        self.gold = gold
        