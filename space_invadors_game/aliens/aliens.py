import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class alien which create one alien from aliens fleet"""

    def __init__(
            self,
            ai_game: any
    ) -> None:
        """Initialise alien and set his start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Alien Health
        self.health = 1

        # Load the alien image and set its rect attribute.
        self.image_road = "./images/alien-ship.png"
        self.image = pygame.image.load(self.image_road)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.height += 20
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move alien right"""
        self.x += (
                self.settings.alien_speed * self.settings.fleet_direction
        )
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if alien at the edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    #
    # def increase_health(self, amount: int) -> None:
    #     self.health += amount
    #
    # def image_change(self) -> None:
    #     if self.image_road == "./images/alien-ship.png":
    #         self.image_road = "./images/level_2.png"
    #     elif self.image_road == "./images/level_2.png":
    #         self.image_road = "./images/level_3.png"
    #     elif self.image_road == "./images/level_3.png":
    #         self.image_road = "./images/level_4.png"
    #     elif self.image_road == "./images/level_4.png":
    #         self.image_road = "./images/level_5.png"
    #
    #     self.image = pygame.image.load(self.image_road)
