class GameStats:
    """Collecting statistic data"""

    def __init__(self, ai_game) -> None:
        """Initializing of statistic"""
        self.game_active = True
        self.ships_left = 2
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state
        self.game_active = False

        # Don't reset scores
        self.high_score = 0

    def reset_stats(self):
        """Initializing statistic, which can be changed along the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
