import pygame.font


class Scoreboard:
    """Class which display score"""
    def __init__(self, ai_game) -> None:
        """Initializing attributes, binding with score """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Settings of font for display score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare imagine with start scores
        self.prep_score()

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

    def show_score(self) -> None:
        """Show score on display"""
        self.screen.blit(self.score_image, self.score_rect)
