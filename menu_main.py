import pygame, sys



#from button import Button

width = 500
height = 500
animCount = 0
isJump = False
isRight = False
isLeft = False
x_1 = 100
y_1 = 100
dy = 2
dx = 2

#размер окна
#screen = pygame.display.set_mode([width, height])
#задний фон 
bg = pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_bg.jpg")
#картинки для анимация персонажа
player_stand = pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_idle.png")
player_right = [pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_1.png"), pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_2.png"),
pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_3.png"),pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_4.png"),
pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_5.png"),pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_right_6.png")]  

player_left = [pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_1.png"), pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_2.png"),
pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_3.png"),pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_4.png"),
pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_5.png"),pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_6.png")]

def test():
    print("!")

jumpCount = 10
def drawWindow():
    global isLeft, isRight, animCount
    screen.blit(bg,(0,0))
    #кнопка
    #b = Button(screen, 100,100, 200, 200, pygame.font.SysFont('Arial', 40),"test", test)


    if isRight:
        screen.blit(player_right[animCount//6],(x_1,y_1))
    elif isLeft:
        screen.blit(player_left[animCount//6],(x_1,y_1))
    else:
        screen.blit(player_stand,(x_1,y_1))
    
    #b.process()
    pygame.display.update()


def main():
    global x_1,y_1,dx,dy,isRight, isLeft, animCount, jumpCount, isJump
    pygame.init()
    
    running = True

    pygame.display.update()
    # движение объекта при нажатии клавиш
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        animCount += 1
        if animCount > 30:
            animCount = 0
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x_1 > 0:
            x_1 -= dx
            isLeft = True
        else:
            isLeft = False
        if keys[pygame.K_d] and x_1< 440:
            x_1 += dx
            isRight = True
        else:
            isRight = False
        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
            if keys[pygame.K_w] and y_1 > 0:
                y_1 -= dy
            if keys[pygame.K_s] and y_1< 435:
                y_1 += dy
        else:
            if jumpCount > 0:
                y_1 -= (jumpCount**2)/2
            else:
                y_1 += (jumpCount**2)/2
            jumpCount -= 1
            if jumpCount == -11:
                isJump = False
                jumpCount = 10

        drawWindow()






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
        if button_1.collidepoint((my,my)):
            if click:
                main()
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



