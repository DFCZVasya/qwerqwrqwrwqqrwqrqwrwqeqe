import pygame, sys
import random


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game  base')
screen = pygame.display.set_mode((500,500), 0 ,32)

font = pygame.font.SysFont(None,20)
#from button import Button
WINDOW_SIZE = (500,500)
 
screen = pygame.display.set_mode(WINDOW_SIZE, 0,32)
display = pygame.Surface((500,500))


player_image = pygame.image.load('/home/stdplus/game/test/player.png').convert()
player_image.set_colorkey((255,255,255))

grass_image = pygame.image.load("/home/stdplus/game/игра/игра/img/block.png")
TILE_SIZE = grass_image.get_width()
COLLISION_TLE_SIZE = 35
laminaaaat = pygame.image.load('/home/stdplus/game/игра/фон/laminaaaat.png')

dirt_image = pygame.image.load('/home/stdplus/game/test/dirt.png')
platform = pygame.image.load('/home/stdplus/game/игра/фон/platform.png')
blok = pygame.image.load('/home/stdplus/game/игра/фон/blok.png')


player_stand = pygame.image.load("/home/stdplus/game/игра/img/pygame_idle.png")
player_left = [pygame.image.load("/home/stdplus/game/игра/img/Right1.png"), pygame.image.load("/home/stdplus/game/игра/img/Right2.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right3.png"),pygame.image.load("/home/stdplus/game/игра/img/Right4.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right5.png")]#,pygame.image.load("/home/stdplus/game/игра/Right6.png")]  

player_right = [pygame.image.load("/home/stdplus/game/игра/img/Left0.png"), pygame.image.load("/home/stdplus/game/игра/img/Left1.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left2.png"),pygame.image.load("/home/stdplus/game/игра/img/Left3.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left4.png")]#,pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_6.png")]


naebLvl3 = pygame.image.load('/home/stdplus/game/игра/игра/img/фон/naeb.png')
lvl4 = pygame.image.load('/home/stdplus/game/игра/фон/lvl4.png')
lvl5 = pygame.image.load('/home/stdplus/game/игра/фон/lvl5.png')
lvl6 = pygame.image.load('/home/stdplus/game/игра/фон/lvl6.png')
lvl7 = pygame.image.load('/home/stdplus/game/игра/босс/доп/lvl8.png')
textt = pygame.image.load('/home/stdplus/game/игра/босс/доп/text.png')
textt2 = pygame.image.load('/home/stdplus/game/игра/босс/доп/text3.png')

lvlboss = pygame.image.load('/home/stdplus/game/игра/босс/финал/final.png')
lvlboss1 = pygame.image.load('/home/stdplus/game/игра/босс/финал/final1.png')
swim = pygame.image.load('/home/stdplus/game/игра/босс/swim.png')
viu = pygame.image.load('/home/stdplus/game/игра/босс/финал/viu.png')

axax = pygame.image.load('/home/stdplus/game/игра/игра/img/фон/axaxax.png')
kjump = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/jump.png')
wasd = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/управление_1.png')
press_e_to_respest = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/press_e.png')
home = pygame.image.load('/home/stdplus/game/игра/игра/фон/home.png')
room = pygame.image.load('/home/stdplus/game/игра/фон/pixil-layer-Layer 6(2).png')
shlepa = pygame.image.load('/home/stdplus/game/игра/игра/img/пельмени))/pixlr-bg-result(1).png')
bg = pygame.image.load("/home/stdplus/game/игра/игра/фон/first_screen7nW7X.jpg")

#паук
spider_down_hitbox = [ pygame.Rect(70,8,36,33),
pygame.Rect(70,44,36,33),
pygame.Rect(70,81,36,33),
pygame.Rect(70,120,36,33),
pygame.Rect(70,157,36,33),
pygame.Rect(70,195,36,33),
pygame.Rect(70,231,36,33),
pygame.Rect(70,271,36,33),
pygame.Rect(70,306,36,33),
pygame.Rect(70,339,36,33),
pygame.Rect(70,371,36,33) ]

spider_up_hitbox = spider_down_hitbox[::-1].copy()

spider_down= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png') ]

spider_up= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png') ]
#паук2

spider2_down_hitbox = [
pygame.Rect(260,8,36,33),
pygame.Rect(260,44,36,33),
pygame.Rect(260,81,36,33),
pygame.Rect(260,120,36,33),
pygame.Rect(260,157,36,33),
pygame.Rect(260,195,36,33),
pygame.Rect(260,231,36,33),
pygame.Rect(260,271,36,33),
pygame.Rect(260,306,36,33),
pygame.Rect(260,339,36,33),
pygame.Rect(260,371,36,33)]

spider2_up_hitbox = spider2_down_hitbox.reverse()

spider2_down= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png') ]

spider2_up= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png') ]
#паук3
spider3_down_hitbox =[ 
pygame.Rect(360,8,36,33),
pygame.Rect(360,44,36,33),
pygame.Rect(360,81,36,33),
pygame.Rect(360,120,36,33),
pygame.Rect(360,157,36,33),
pygame.Rect(360,195,36,33),
pygame.Rect(360,231,36,33),
pygame.Rect(360,271,36,33),
pygame.Rect(360,306,36,33),
pygame.Rect(360,339,36,33),
pygame.Rect(360,371,36,33)]

spider3_up_hitbox = spider3_down_hitbox.reverse()

spider3_down= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png') ]

spider3_up= [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider11.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider10.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider9.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider8.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider7.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider6.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/spider1.png') ]
#чудо
enemy_left_hitbox = [
pygame.Rect(403,364,70,22),
pygame.Rect(336,364,70,22),
pygame.Rect(282,364,70,22),
pygame.Rect(229,364,70,22),
pygame.Rect(169,364,70,22),
pygame.Rect(121,364,70,22)]

enemy_right_hitbox =enemy_left_hitbox.reverse()
enemy_right = [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r6.png')]

enemy_left = [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l6.png')]

enemy2_right = [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_r6.png')]

enemy2_left = [pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l1.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l2.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l3.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l4.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l5.png'),
pygame.image.load('/home/stdplus/game/игра/игра/img/паук/enemy_l6.png')]
#акула

shark_left = [pygame.image.load('/home/stdplus/game/игра/босс/shark0.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark1.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark2.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark3.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark4.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark5.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark6.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark7.png'),
pygame.image.load('/home/stdplus/game/игра/босс/shark8.png')]


shark_left = [pygame.image.load('/home/stdplus/game/игра/босс/sharkleft1.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft2.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft3.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft4.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft5.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft6.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft7.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft8.png'),
pygame.image.load('/home/stdplus/game/игра/босс/sharkleft9.png')]







game_map1 = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['2','2','2','2','2']]

game_map2 = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['3','3','3','3','3'],
            ['3','3','3','3','3']]

game_map3 = [['0','0','0','0','0'],
            ['0','0','0','4','4'],
            ['0','0','0','4','4'],
            ['4','0','0','4','4'],
            ['4','0','0','4','4'],
            ['4','0','0','4','4']]

game_map4 = [['4','0','0','0','0'],
            ['4','0','0','0','0'],
            ['4','0','0','0','0'],
            ['4','0','0','0','0'],
            ['4','4','4','4','4'],
            ['4','4','4','4','4']]

game_map5 = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['4','4','4','4','4'],
            ['4','4','4','4','4']]
game_map6 = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['4','4','4','4','4'],
            ['4','4','4','4','4']]

game_map7 = [['0','0','0','0','4'],
            ['0','0','0','5','4'],
            ['0','0','5','0','4'],
            ['0','5','0','0','0'],
            ['4','4','4','4','4'],
            ['4','4','4','4','4']]

game_map8 = [['0','0','0','0','4'],
            ['0','0','0','0','4'],
            ['0','0','0','0','4'],
            ['0','0','4','0','4'],
            ['4','0','0','0','4'],
            ['4','0','0','0','4']]
game_map9 = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0']]

game_maps = []
game_maps.append(game_map1)
game_maps.append(game_map2)
game_maps.append(game_map3)
game_maps.append(game_map4)
game_maps.append(game_map5)
game_maps.append(game_map6)
game_maps.append(game_map7)
game_maps.append(game_map8)
game_maps.append(game_map9)
collision_maps = []


collision_map1 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

collision_map2 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

collision_map3 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','1','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]
collision_map4 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]
collision_map5 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]

collision_map6 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]
collision_map7 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','1','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','1','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','1','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','1','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','1','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','1','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','1','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','1','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]

collision_map8 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['1','1','1','0','0','0','0','0','0','0','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','1','0','0','0','0']]

collision_map9 = [['0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

               
collision_maps.append(collision_map1)
collision_maps.append(collision_map2)
collision_maps.append(collision_map3)
collision_maps.append(collision_map4)
collision_maps.append(collision_map5)
collision_maps.append(collision_map6)
collision_maps.append(collision_map7)
collision_maps.append(collision_map8)
collision_maps.append(collision_map9)
width = 500
height = 500
animCount = 0


click = False
hp = 3
def spider_collision(player_rect):
    if is_spider_down:
        if player_rect.colliderect(spider_down_hitbox[spAnimCount//6]):
            pygame.draw.rect(display, (255,0,0), spider_down_hitbox[spAnimCount//6])
            print(spAnimCount)
    else:
       if player_rect.colliderect(spider_up_hitbox[spAnimCount//6]):
            pygame.draw.rect(display, (255,0,0), spider_up_hitbox[spAnimCount//6])
            print(spAnimCount)

menuu = pygame.image.load('/home/stdplus/game/игра/игра/фон/BG.png')
opt = pygame.image.load('/home/stdplus/game/игра/фон/pixil-layer-Layer 3.png')
startw = pygame.image.load('/home/stdplus/game/игра/фон/pixil-layer-Layer 1.png')

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

moving_right = False
moving_left = False

 
player_y_momentum=0
air_time = 0

is_spider_down = True
is_spider2_down = True
is_spider3_down = True

is_enemy_right = True
is_enemy2_right = True
is_shark_right = True

animCount = 0
spAnimCount = 0
sp2AnimCount = 0
sp3AnimCount = 0
enAnimCount = 0
en2AnimCount = 0
shAnimCount = 0
lvlCount = 0

isRight = False
isLeft = False
#здесь ниже по иксу должно быть -22
player_rect = pygame.Rect(-22,345, player_stand.get_width(), player_stand.get_height())

def drawWindow(x_1, y_1):
    global moving_left, moving_right, animCount, player_rect
    if lvlCount == 0:
        display.blit(bg,(0,-100))
        display.blit(home,(100,105))
        display.blit(wasd,(0,310))
        display.blit(press_e_to_respest,(100,320))

        display.blit(kjump,(50,320))
    if lvlCount == 1:
        display.blit(room,(0,-6))
        display.blit(shlepa,(250,190))
        display.blit(textt2,(10,70))

    if lvlCount == 2:
        display.blit(naebLvl3,(0,20))
    if lvlCount == 3:
        pygame.draw.rect(display, (105,63,85),(0,0,500,500))
        display.blit(lvl4,(20,0))
    if lvlCount == 4:
        display.blit(lvl5,(0,0))
        spider_collision(player_rect)
        
        if is_spider_down:
            display.blit(spider_down[spAnimCount//6],(50,0))
        else:
            display.blit(spider_up[spAnimCount//6],(50,0))

        
        if is_spider2_down:
            display.blit(spider2_down[sp2AnimCount//12],(250,0))
        else:
            display.blit(spider2_up[sp2AnimCount//12],(250,0))

       
        if is_spider3_down:
            display.blit(spider3_down[sp3AnimCount//6],(350,0))
        else:
            display.blit(spider3_up[sp3AnimCount//6],(350,0))

        


        #spider_rect = pygame.Rect(50, 300,spider_down.get_width(), spider_up.get_height())
    if lvlCount == 5:
        display.blit(lvl5,(0,0))

        if is_enemy_right:
           display.blit(enemy_right[enAnimCount//20], (100, 350))
        else:
            display.blit(enemy_left[enAnimCount//20], (100,350))
        #if is_enemy2_right:
        #   display.blit(enemy2_right[en2AnimCount//10], (200, 350))
        #else:
        #    display.blit(enemy2_left[en2AnimCount//10], (200,350))
    if lvlCount == 6:
        display.blit(lvl6,(0,0))
        display.blit(textt,(10,60))
    
    if lvlCount == 7:
       
        display.blit(lvl7,(0,0))
      
        
    if lvlCount == 8:
        display.blit(lvlboss,(0,0))
        display.blit(lvlboss1,(0,0))
    

    if moving_right:
        display.blit(player_right[animCount//5],(x_1,y_1 + 7))
    elif moving_left:
        display.blit(player_left[animCount//5],(x_1,y_1 + 7))
    else:
        display.blit(player_stand,(x_1,y_1 + 7))
    
    pygame.display.update()

def game():
    global player_rect, moving_left, moving_right, player_y_momentum, spAnimCount, air_time, animCount, lvlCount, is_spider_down,sp2AnimCount,sp3AnimCount,is_spider2_down,is_spider3_down,enAnimCount,is_enemy_right,is_enemy2_right,en2AnimCount
    
    
    
    
    while True:
        display.fill((79,181,225))
        drawWindow(player_rect.x,player_rect.y)
        #print(player_rect.x,player_rect.y)
        tile_rects = []
        y = 0
        for row in game_maps[lvlCount]:
            x =0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image,(x * TILE_SIZE, y * TILE_SIZE))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE - 55))
                if tile == '3':
                    display.blit(laminaaaat, (x * TILE_SIZE, y * TILE_SIZE-55))
                if tile == '4':
                    display.blit(axax, (x * TILE_SIZE  , y * TILE_SIZE ))
                if tile == '5':
                    display.blit(platform,(x * TILE_SIZE +10, y* TILE_SIZE))
                
                x += 1
            y +=1
        
        y = 0
        for row in collision_maps[lvlCount]:
            x =0
           
            for tile in row:
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * COLLISION_TLE_SIZE, y * COLLISION_TLE_SIZE-12, COLLISION_TLE_SIZE, COLLISION_TLE_SIZE))
                if tile == 'b':
                    display.blit(blok,((x * COLLISION_TLE_SIZE  , y * COLLISION_TLE_SIZE-20 )))
                x += 1
            y +=1
                    




        player_movement = [0,0]
        if moving_right:
            player_movement[0] += 2
        if moving_left:

            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3
        
        if lvlCount == 0:
            if 299 < player_rect.x < 329 and 299 < player_rect.y < 346:
                keys = pygame.key.get_pressed()
                if keys[K_e]:            
                    lvlCount = 1 
                    player_rect.x = 100
                    player_rect.y = 345
                
        if lvlCount == 1:
            if -7 < player_rect.x < 27 and 299 < player_rect.y < 346: 
                keys = pygame.key.get_pressed()
                if keys[K_e]: 
                    lvlCount = 0
                    player_rect.x = 280
                    player_rect.y = 345
        if lvlCount == 0:
            if 460 < player_rect.x:
                lvlCount = 2
                player_rect.x = 0
                player_rect.y = 100
        if lvlCount == 2:
            if 430< player_rect.y:
                lvlCount = 3
                player_rect.x = 150
                player_rect.y = 50
        if lvlCount == 3:
            if 440 < player_rect.x:
                lvlCount = 4
                player_rect.x = 30
                player_rect.y = 200
        if lvlCount == 4:
        
            if 440< player_rect.x:
                lvlCount = 5
                player_rect.x = 0
                player_rect.y = 300
        if lvlCount == 5:
            if 440< player_rect.x:
                lvlCount = 6
                player_rect.x = 0
                player_rect.y = 300
        if lvlCount == 6:
            if player_rect.y <10:
                lvlCount = 7
                player_rect.x = 10
                player_rect.y = 300
        if lvlCount == 7:
            if player_rect.y > 430 :
                lvlCount = 8
                player_rect.x = 100
                player_rect.y = 100
                 
        
        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['bottom']:
            player_y_momentum = 0
            air_time = 0
        else:
            air_time +=1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_time < 6:
                        player_y_momentum = -5
                if event.key == K_ESCAPE:
                   return
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        animCount += 1
        spAnimCount += 1
        sp2AnimCount += 1
        sp3AnimCount += 1
        enAnimCount += 1
        if spAnimCount > 60:
            spAnimCount = 0
            is_spider_down = not is_spider_down
        if sp2AnimCount > 120:
            sp2AnimCount = 0
            is_spider2_down = not is_spider2_down
        if sp3AnimCount > 60:
            sp3AnimCount = 0
            is_spider3_down = not is_spider3_down
        if enAnimCount >= 120:
            enAnimCount = 0
            is_enemy_right = not is_enemy_right



        if animCount > 24:
            animCount = 0
            
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.display.update() 
        mainClock.tick(60) 

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1 , color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)



def main_menu():
    global click
    while True:
        

        screen.blit(menuu,(-70,0))
        draw_text('main menu', font,(255,255,255), screen , 20,20)

        mx,my = pygame.mouse.get_pos()


        button_1 =pygame.Rect(200,150,100,25)
        button_2 = pygame.Rect(200,200,100,25)
        
        if button_1.collidepoint((mx,my)):
            if click:
                game()
        if button_2.collidepoint((mx,my)):
            if click:
                options()
        screen.blit(startw,(200,122))
        screen.blit(opt,(200,200))
        

        click  = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    pygame.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)



def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('options', font, (255,255,255), screen,20,20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
        pygame.display.update()
        mainClock.tick(60)


main_menu()
