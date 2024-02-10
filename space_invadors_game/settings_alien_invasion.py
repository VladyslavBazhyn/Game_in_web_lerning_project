class Settings:
    """Class for saving all needed settings"""

    def __init__(self) -> None:
        # Settings for screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 200, 100)

        # Settings for ship
        self.ship_speed = 1.0

        # Setting for a bullet
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
