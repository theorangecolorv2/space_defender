import pygame
from bullet import Bullet


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load('graphics/spaceships.png')
        self.rect = self.image.get_rect(midbottom=(screen_width / 2, self.screen_height))
        self.speed = 6
        self.bullets_group = pygame.sprite.Group()
        self.bullets_ready = True
        self.bullets_time = 0
        self.bullet_recharge = 250  # Перезарядка
        self.bullet_music = pygame.mixer.Sound('music/bullet_music.mp3')

    def user_input(self):  # функция для отслеживания нажатий кнопок
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= 6

        if keys[pygame.K_SPACE] and self.bullets_ready:
            self.bullets_ready = False
            bullet = Bullet(self.rect.center, 10, self.screen_height)
            self.bullets_group.add(bullet)
            self.bullets_time = pygame.time.get_ticks()
            self.bullet_music.play()

    def update(self):
        self.user_input()
        self.limit()
        self.bullets_group.update()
        self.recharge_bullet()

    def limit(self):  # функция для проверки чтобы корабль не выходил за границы поля
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0

    def recharge_bullet(self):  # скорость пуль
        if not self.bullets_ready:
            time = pygame.time.get_ticks()
            if time - self.bullets_time >= self.bullet_recharge:
                self.bullets_ready = True

    def reset(self):
        self.rect = self.image.get_rect(midbottom=(self.screen_width / 2, self.screen_height))
        self.bullets_group.empty()
