import pygame


class Ship:

    def __init__(self, ai_game):
        self.game_screen = ai_game.screen
        self.game_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.game_rect.midbottom

        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.game_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.game_screen.blit(self.image, self.rect)