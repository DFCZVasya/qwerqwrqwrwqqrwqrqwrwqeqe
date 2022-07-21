import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Pygame Window')

WINDOW_SIZE = (500,500)
 
screen = pygame.display.set_mode(WINDOW_SIZE, 0,32)
display = pygame.Surface((500,500))


player_image = pygame.image.load('/home/stdplus/game/test/player.png').convert()
player_image.set_colorkey((255,255,255))

grass_image = pygame.image.load("/home/stdplus/game/игра/игра/img/block.png")
TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('/home/stdplus/game/test/dirt.png')


player_stand = pygame.image.load("/home/stdplus/game/игра/img/pygame_idle.png")
player_left = [pygame.image.load("/home/stdplus/game/игра/img/Right1.png"), pygame.image.load("/home/stdplus/game/игра/img/Right2.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right3.png"),pygame.image.load("/home/stdplus/game/игра/img/Right4.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right5.png")]#,pygame.image.load("/home/stdplus/game/игра/Right6.png")]  

player_right = [pygame.image.load("/home/stdplus/game/игра/img/Left0.png"), pygame.image.load("/home/stdplus/game/игра/img/Left1.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left2.png"),pygame.image.load("/home/stdplus/game/игра/img/Left3.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left4.png")]#,pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_6.png")]

kjump = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/jump.png')
wasd = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/управление_1.png')
home = pygame.image.load('/home/stdplus/game/игра/игра/фон/home.png')
bg = pygame.image.load("/home/stdplus/game/игра/игра/фон/first_screen7nW7X.jpg")
game_map = [['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['0','0','0','0','0'],
            ['2','2','2','2','2']]


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

animCount = 0

isRight = False
isLeft = False

player_rect = pygame.Rect(-22,345, player_stand.get_width(), player_stand.get_height())
def drawWindow(x_1, y_1):
    global moving_left, moving_right, animCount
    display.blit(bg,(0,-100))
    display.blit(home,(100,105))
    display.blit(wasd,(0,310))

    display.blit(kjump,(50,320))

    
    

    if moving_right:
        display.blit(player_right[animCount//5],(x_1,y_1 + 7))
    elif moving_left:
        display.blit(player_left[animCount//5],(x_1,y_1 + 7))
    else:
        display.blit(player_stand,(x_1,y_1 + 7))
    
    pygame.display.update()

def game():
    while True:
        display.fill((146,244,255))
        drawWindow(player_rect.x,player_rect.y)
        #print(player_rect.x,player_rect.y)
        tile_rects = []
        y = 0
        for row in game_map:
            x =0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image,(x * TILE_SIZE, y * TILE_SIZE))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE - 55))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE - 55, TILE_SIZE, TILE_SIZE))
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

        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['bottom']:
            player_y_momentum = 0
            air_time = 0
        else:
            air_time +=1

        #display.blit(player_image, (player_rect.x,player_rect.y))
        
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
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        animCount += 1
        if animCount > 24:
            animCount = 0
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.display.update() 
        clock.tick(60) 
                



