class GameState:

    def __init__(
        self,
        player_team,
        enemy_team,
        inventory,
        current_zone
    ):
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.inventory = inventory
        self.current_zone = current_zone