import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.game_screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midbottom = ai_game.ship.image_rect.midtop

        self.y = float(self.bullet_rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.game_screen, self.color, self.bullet_rect)