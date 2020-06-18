import pygame


class Ship:

    def __init__(self, ai_game):
        self.game_screen = ai_game.screen
        self.settings = ai_game.settings
        self.game_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.midbottom = self.game_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.image_rect.x)

    def update(self):
        if self.moving_right and self.image_rect.right < self.game_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.image_rect.left > 0:
            self.x -= self.settings.ship_speed

        self.image_rect.x = self.x

    def blitme(self):
        self.game_screen.blit(self.image, self.image_rect)