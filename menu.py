
import pygame, sys

from requests import options

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game  base')
screen = pygame.display.set_mode((500,500), 0 ,32)


font = pygame.font.SysFont(None,20)

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1 , color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    global click
    while True:

        screen.fill((0,0,0))
        draw_text('main menu', font,(255,255,255), screen , 20,20)

        my,my = pygame.mouse.get_pos()

        button_1  =pygame.Rect(50,100,200,50)
        button_2 = pygame.Rect(50,200,200,50)
        if button_1.collidepoint((my,my)):# если кнопка 1 нажата то запускается функция game
            if click:
                game()
        if button_2.collidepoint((my,my)):
            if click:
                options()
        pygame.draw.rect(screen, (255,0,0), button_1)
        pygame.draw.rect(screen, (255,0,0), button_2)

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
        mainClock.tick(60)# 60 кадров в секунду это лучше не изменять
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
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