import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(
        self,
        ai_game: any
    ) -> None:
        # Create bullet object in current directory
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create rect of bullet in (0, 0) and set right position
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save position of bullet as float number
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Push bullet up"""

        # Update float position of bullet
        self.y -= self.settings.bullet_speed

        # Update position rect
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw bullet on screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)

