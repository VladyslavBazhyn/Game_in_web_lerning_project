import pygame.font
from pygame.sprite import Group

from space_invadors_game.ships.human_ship import HumanShip


class Scoreboard:
    """Class which display score"""
    def __init__(self, ai_game) -> None:
        """Initializing attributes, binding with score """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings of font for display score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare imagine with start scores
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self) -> None:
        """Show how many sips left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = HumanShip(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self) -> None:
        """Torn level to imagine"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Place level near count
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self) -> None:
        """Convert score to imagine"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score}"
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Show score in right upper angle
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self) -> None:
        """Generate high score to imagine"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score}"
        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Place high score to center of horizon
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self) -> None:
        """Show score on display"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self) -> None:
        """Check whether new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
