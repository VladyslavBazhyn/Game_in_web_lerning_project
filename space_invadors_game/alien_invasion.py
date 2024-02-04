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

    def _check_events(self):
        # """Checking for the mous and keys actions"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move ship right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Show last printed display
        pygame.display.flip()

    def run_game(self) -> None:
        """Start main cycle of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
