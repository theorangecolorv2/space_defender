import pygame
import random
from bullet import Bullet


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, n):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.images = [pygame.image.load('graphics/asteroid 3.png'), pygame.image.load('graphics/asteroid 2.png'),
                       pygame.image.load(
                           'graphics/asteroid 1.png')]
        self.image = self.images[n]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)
        self.asteroids_group = pygame.sprite.Group()

    def update(self):  # скорость передвижения
        self.rect.y += self.speed


