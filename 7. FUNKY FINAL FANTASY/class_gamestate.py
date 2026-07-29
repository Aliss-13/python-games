class GameState:

    def __init__(
        self,
        player_team,
        enemy_team,
        inventory,
        current_zone,
        active_quests=None,
        completed_quests=None,
    ):
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.inventory = inventory
        self.current_zone = current_zone
        self.active_quests = active_quests or []
        self.completed_quests = completed_quests or []