class CombatContext:

    def __init__(
        self,
        player_team,
        enemy_team,
        inventory=None,
        zone=None,
        game=None
    ):
        self.player_team = player_team
        self.enemy_team = enemy_team
        self.inventory = inventory
        self.zone = zone
        self.game = game


    def get_live_entities(self):

        return [
            entity 
            for entity in self.player_team + self.enemy_team
            if entity.life > 0
        ]

    def get_live_players(self):
        return [
            character
            for character in self.player_team
            if character.life > 0
        ]

    def get_live_enemies(self):
        return [
            enemy
            for enemy in self.enemy_team
            if enemy.life > 0
        ]