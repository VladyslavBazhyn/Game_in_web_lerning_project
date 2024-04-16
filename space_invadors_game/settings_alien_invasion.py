class Settings:
    """Class for saving all needed settings"""

    def __init__(self) -> None:
        """Initialize constant game settings"""
        # Settings for screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 200, 100)

        # Settings for ship
        self.ship_limit = 1

        # Setting for a bullet
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Settings for an aliens
        self.fleet_drop_speed = 12

        # Parameter for speed increasing
        self.alien_speedup_scale = 1.05
        self.ship_speedup_scale = 1.05
        self.bullet_speedup_scale = 1.05

        # How fast increase alien price
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initializing of changeable parameters"""
        self.ship_speed = 1.25
        self.bullet_speed = 1.5
        self.alien_speed = 0.15

        # fleet_direction 1 mean way of moving right; -1 left
        self.fleet_direction = 1

        # Taking score
        self.alien_points = 50

    def increase_speed(self) -> None:
        """Increasing of speed parameters and alin price"""
        self.ship_speed *= self.ship_speedup_scale
        self.bullet_speed *= self.bullet_speedup_scale
        self.alien_speed *= self.alien_speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
