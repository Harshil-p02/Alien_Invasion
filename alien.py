import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.game_screen = ai_game.screen
        self.game_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        if self.rect.right >= self.game_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x = float(self.rect.x)
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x