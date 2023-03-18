import pygame
import random
from os import listdir
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()
screen = width, heigth = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
YELLOW = 255, 255, 0
BLUE = 0, 0, 255

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)

IMGS_PATH = 'goose'

player_imgs = [pygame.image.load(IMGS_PATH + '/' + five).convert_alpha() for five in listdir(IMGS_PATH)]
new_size = (int(player_imgs[0].get_width()/1.5), int(player_imgs[0].get_height()/1.5))
player_imgs = [pygame.transform.scale(ing, new_size) for ing in player_imgs]
player = player_imgs[0]

player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_speed = 6

def creat_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_size = (int(enemy.get_width() * 0.4), int(enemy.get_height() * 0.4))
    enemy = pygame.transform.scale(enemy, enemy_size)
    enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

def creat_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_size = (int(bonus.get_width() * 0.4), int(bonus.get_height() * 0.4))
    bonus = pygame.transform.scale(bonus, bonus_size)
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 6)
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgx = 0
bgx2 = bg.get_width()
bg_speed = 3

CREAT_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREAT_ENEMY, 1500)

CREAT_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREAT_BONUS, 1500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

img_index =0
scores = 0

enemies = []
bonuses = []

is_working = True

while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREAT_ENEMY:
            enemies.append(creat_enemy())

        if event.type == CREAT_BONUS:
            bonuses.append(creat_bonus())

        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(player_imgs):
                img_index = 0
            player = player_imgs[img_index]

    pressed_key = pygame.key.get_pressed()

    bgx -= bg_speed
    bgx2 -= bg_speed

    if bgx < -bg.get_width():
        bgx = bg.get_width()

    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()

    main_surface.blit(bg, (bgx, 0))
    main_surface.blit(bg, (bgx2, 0))

    main_surface.blit(player, player_rect)

    main_surface.blit(font.render(str(scores), True, BLUE), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom >= heigth:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1


    if pressed_key[K_DOWN] and player_rect.bottom < heigth:
        player_rect = player_rect.move(0, player_speed)

    if pressed_key[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move(0, -player_speed)

    if pressed_key[K_RIGHT] and player_rect.right < width:
        player_rect = player_rect.move(player_speed, 0)

    if pressed_key[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(-player_speed, 0)

    pygame.display.flip()