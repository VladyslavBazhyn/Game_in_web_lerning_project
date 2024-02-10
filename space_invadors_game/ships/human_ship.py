import pygame


class HumanShip:
    """Class for caring of HumanShip"""
    def __init__(
            self,
            ai_game: any
    ) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the image of the ship
        image = pygame.image.load(
            "./images/ship.png"
        )
        self.image = pygame.transform.scale(image, (60, 60))  # Set desired width and height

        self.rect = self.image.get_rect()

        # Create ship at the middle of the display
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.settings = ai_game.settings

    def update(self):
        """
        Update current position base on
        indicators of moving
        """
        if self.moving_right and (self.rect.right - 165) < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)
