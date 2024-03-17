import sys
from time import sleep

import pygame

from settings_alien_invasion import Settings
from game_stats import GameStats
from space_invadors_game.ships.human_ship import HumanShip
from space_invadors_game.bullet.bullet import Bullet
from space_invadors_game.aliens.aliens import Alien
from button import Button


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

        # Create instance for saving game statistic
        self.stats = GameStats(self)

        # Create Play button
        self.play_button = Button(self, "Play")

    def _ship_hit(self):
        """React on collision of alien ship with human ship"""
        if self.stats.ships_left > 0:
            # Decrease ships_left
            self.stats.ships_left -= 1

            # Delete surplus of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and set ship on center
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self) -> None:
        """Check whether one of the aliens reach the screen bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # React like ship was hit
                self._ship_hit()
                break


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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos: tuple) -> None:
        """Start new game when user pres Play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Annul game statistic
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True

            # Delete existing aliens and bullet
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and centering human_ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide mouse cursor
            pygame.mouse.set_visible(False)

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

    def _update_bullets(self) -> None:
        """Update bullet position and remove old bullets"""
        self.bullets.update()
        # Update bullets position
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self) -> None:
        """Reaction on shooting aliens by bullets"""
        # Delete all bullets and aliens which collided
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if not self.aliens:
            print("All aliens destroyed! Creating a new fleet...")
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Draw Play button, if game inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Show last printed display
        pygame.display.flip()

    def _update_aliens(self) -> None:
        """Check whether fleet situated on edge,
        then renovate position of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Seek whether some of the aliens reached screen bottom
        self._check_aliens_bottom()

    def _check_fleet_edges(self) -> None:
        """Acting according to whether some of the aliens achieve screen edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Move down all fleet and change his direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= (-1)

    def run_game(self) -> None:
        """Start main cycle of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
