import pygame


class HumanShip:
    """Class for caring of HumanShip"""
    def __init__(
            self,
            ai_game: any) -> None:
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the image of the ship
        self.image = pygame.image.load(
            "./images/ship.png"
        )
        self.rect = self.image.get_rect()

        # Create at the middle of the display
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update current position base on
        indicators of moving
        """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)
