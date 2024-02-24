import sys

import pygame

from settings_alien_invasion import Settings
from space_invadors_game.ships.human_ship import HumanShip
from space_invadors_game.bullet.bullet import Bullet
from space_invadors_game.aliens.aliens import Alien


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
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def _create_alien(
            self,
            alien_number: int,
            numbers_row: int
    ) -> None:
        """Create an oen alien and place him in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 4 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (alien.rect.height * numbers_row)
        self.aliens.add(alien)

    def _create_fleet(self) -> None:
        """Creating a fleet of aliens"""
        # Create one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (4 * alien_width)
        number_of_aliens_x = available_space_x // (3 * alien_width)

        # Calculate which amount of alien's rows can be placed on a screen
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height -
            (4 * alien_height) - ship_height
        )
        number_rows = available_space_y // (3 * alien_height)

        for row in range(number_rows):
            for alien_number in range(number_of_aliens_x):
                # Create alien and place it in row
                self._create_alien(alien_number, row)

    def _check_events(self):
        # """Checking for the mouse and keys actions"""

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

        self.aliens.draw(self.screen)

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
