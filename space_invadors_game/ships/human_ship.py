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

    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)
