import sys

import pygame

from settings_alien_invasion import Settings
from space_invadors_game.ships.human_ship import HumanShip


class AlienInvasion:
    """Global class which is role of game behavior"""

    def __init__(self) -> None:
        """Initialisation of this game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien invasion")

        self.ship = HumanShip(self)

    def run_game(self) -> None:
        """Start main cycle of the game"""

        while True:
            # """Checking for the mous and keys actions"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()

            # Show last printed display
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
