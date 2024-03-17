import pygame.font


class Button:

    def __init__(self, ai_game, msg: str) -> None:
        """Initialise attributes of the game"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set size and properties of the button
        self.width, self.height = 100, 100
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create object 'rect' button and centering it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Message on the button need t obe shown only one time
        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        """Transform text in to image and set it to center of the button"""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_color,
            self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw empty button, and then '--' message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
