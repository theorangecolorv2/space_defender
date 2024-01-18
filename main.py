import sys
import pygame
import random
from game import Game
from asteroid import Asteroid
from menu import *

def nothing():
    pass

pygame.init()
screen_width = 800
screen_height = 800
image_fons = pygame.image.load('graphics/ffon.jpg')
heart_image = pygame.image.load('graphics/heart1.png')
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Defender')
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('game', 35)

scores = my_font.render('SCORE', False, (0, 227, 160))
record = my_font.render('RECORD', False, (0, 227, 160))

menu = Menu()

game = Game(screen_width, screen_height, menu)


menu.append_option("Play", game.menus)
menu.append_option('Quit', quit)
menu.append_option("Reset current record", game.reset_record)
menu.append_option("", nothing)
menu.append_option(f"Current record is {game.records}", nothing)

enemy = pygame.USEREVENT + 1
pygame.time.set_timer(enemy, random.randint(4000, 8000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == enemy:
            game.create_enemy()
            pygame.time.set_timer(enemy, random.randint(4000, 8000))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                menu.switch(-1)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                menu.switch(1)
            elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                menu.select()
            elif event.key == pygame.K_ESCAPE:
                game.pause()

    if game.run == False:
        menu.draw(screen, 100, 100, 75)
        pygame.display.flip()
    if game.run:  # создание астероидов
        if random.randint(1, 20) == 1 and game.run:
            new_asteroid = Asteroid(screen_width, screen_height, random.randint(0, 2))
            game.asteroids_group.add(new_asteroid)
        if game.run:
            game.spaceship_group.update()
            game.asteroids_group.update()
            game.check_for_collisions()
            game.enemy_group.update()
        keys = pygame.key.get_pressed()
        screen.blit(image_fons, (0, 0))
        if game.lives == 3:  # проверка на количесвто жизней
            screen.blit(heart_image, (691, 0))
            screen.blit(heart_image, (725, 0))
            screen.blit(heart_image, (760, 0))
        elif game.lives == 2:
            screen.blit(heart_image, (691, 0))
            screen.blit(heart_image, (725, 0))
        elif game.lives == 1:
            screen.blit(heart_image, (691, 0))
        screen.blit(scores, (25, 25))
        score_point = my_font.render(str(game.score), False, (0, 227, 160))  # запись очков
        record_points = my_font.render(str(game.records), False, (0, 227, 160))  # запись рекорда
        screen.blit(score_point, (50, 55, 50, 50))
        screen.blit(record, (687, 55, 50, 50))
        screen.blit(record_points, (745, 91, 0, 0))
        game.spaceship_group.draw(screen)  # рисование корабля
        game.spaceship_group.sprite.bullets_group.draw(screen)  # рисование пули
        game.asteroids_group.draw(screen)
        game.enemy_group.draw(screen)
        pygame.display.update()
        clock.tick(60)


