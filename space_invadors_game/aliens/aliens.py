import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class alien which create one alien from aliens fleet"""
    def __init(
        self,
        ai_game: any
    ) -> None:
        """Initialise alien and set his start position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        # image = pygame.image.load("./images/alien-ship.png")
        # self.image = pygame.transform.scale(image, (100, 100))
        self.image = pygame.image.load("./images/alien-ship.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
