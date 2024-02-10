import sys

import pygame

from settings_alien_invasion import Settings
from space_invadors_game.ships.human_ship import HumanShip
from bullet.bullet import Bullet


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
        self.bullets = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def _check_events(self):
        # """Checking for the mous and keys actions"""

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """Create new bullet and add it to group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self) -> None:
        """Update bullet position and remove old bullets"""
        self.bullets.update()
        # Update bullets position
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Show last printed display
        pygame.display.flip()

    def run_game(self) -> None:
        """Start main cycle of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.update_bullets()
            self._update_screen()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
