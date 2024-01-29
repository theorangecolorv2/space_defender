import pygame
from spaceship import Spaceship
from asteroid import Asteroid
from enemy import Enemy
import menu
import random

class Game:
    def __init__(self, screen_width, screen_height, menu):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.asteroids_group = pygame.sprite.Group()
        self.asteroids_group.add(Asteroid(self.screen_width, self.screen_height, random.randint(0, 2)))
        self.enemy_group = pygame.sprite.GroupSingle()
        self.enemy_group.add(Enemy(self.screen_width, self.screen_height))
        self.lives = 3
        self.run = False
        self.score = 0
        self.load_records()
        self.menu = menu
        self.killed_music = pygame.mixer.Sound('music/killed_music.mp3')
        pygame.mixer.music.load('music/music (2).mp3')
        pygame.mixer.music.play(-1)

    def check_for_collisions(self):  # функция для проверки столкновений объектов и подссчет очков
        if self.spaceship_group:  # проверка на попадания лазера в объекты
            for bullet_sprite in self.spaceship_group.sprite.bullets_group:
                if pygame.sprite.spritecollide(bullet_sprite, self.asteroids_group, True):
                    self.score += 1
                    self.record()
                    self.killed_music.play()
                    bullet_sprite.kill()
                if pygame.sprite.spritecollide(bullet_sprite, self.enemy_group, True):
                    self.score += 5
                    self.record()
                    self.killed_music.play()
                    bullet_sprite.kill()
        if self.asteroids_group:  # проверка на попадания астероидов в корабль
            for asteroids_sprite in self.asteroids_group:
                if pygame.sprite.spritecollide(asteroids_sprite, self.spaceship_group, False):
                    asteroids_sprite.kill()
                    self.killed_music.play()
                    self.lives -= 1
                    if self.lives == 0:
                        self.record()
                        self.game_over()
                        self.score = 0
        if self.asteroids_group:
            for asteroid in self.asteroids_group:
                if pygame.sprite.spritecollide(asteroid, self.spaceship_group, False):
                    self.game_over()
                    self.score = 0

    def game_over(self):
        self.run = False
        self.lives = 3
        self.asteroids_group.empty()

    def n(self):
        pass

    def reset(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.asteroids_group.empty()

    def record(self):  # функция для сохранения рекорда в файл
        if self.score > self.records:
            self.records = self.score

            with open('record.txt', 'w') as file:
                file.write(str(self.records))

    def reset_record(self):
        self.score = 0
        with open('record.txt', 'w') as file:
            file.write("0")
        self.load_records()
        self.menu._option_surfaces.pop()
        self.menu._callbacks.pop()
        self.menu.append_option(f"Current record is {self.records}", self.n)


    def load_records(self):
        try:
            with open('record.txt', 'r') as file:
                self.records = int(file.read())
        except FileNotFoundError:
            self.records = 0

    def menus(self):
        self.run = True

    def pause(self):
        self.run = False

    def create_enemy(self):
        self.enemy_group.add(Enemy(self.screen_width, self.screen_height))
