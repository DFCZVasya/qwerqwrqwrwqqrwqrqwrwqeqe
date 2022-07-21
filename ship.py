import pygame, sys



mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game  base')
screen = pygame.display.set_mode((500,500), 0 ,32)

font = pygame.font.SysFont(None,20)
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
click = False
wasd = pygame.image.load('/home/stdplus/game/игра/игра/img/управление/Background64x64.png')
home = pygame.image.load('/home/stdplus/game/игра/игра/фон/home.png')
menuu = pygame.image.load('/home/stdplus/game/игра/игра/фон/BG.png')
opt = pygame.image.load('/home/stdplus/game/игра/фон/pixil-layer-Layer 3.png')
startw = pygame.image.load('/home/stdplus/game/игра/фон/pixil-layer-Layer 1.png')
#размер окна
screen = pygame.display.set_mode([width, height])
#задний фон 
bg = pygame.image.load("/home/stdplus/game/игра/игра/фон/first_screen7nW7X.jpg")
#картинки для анимация персонажа
player_stand = pygame.image.load("/home/stdplus/game/игра/img/pygame_idle.png")
player_left = [pygame.image.load("/home/stdplus/game/игра/img/Right1.png"), pygame.image.load("/home/stdplus/game/игра/img/Right2.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right3.png"),pygame.image.load("/home/stdplus/game/игра/img/Right4.png"),
pygame.image.load("/home/stdplus/game/игра/img/Right5.png")]#,pygame.image.load("/home/stdplus/game/игра/Right6.png")]  

player_right = [pygame.image.load("/home/stdplus/game/игра/img/Left0.png"), pygame.image.load("/home/stdplus/game/игра/img/Left1.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left2.png"),pygame.image.load("/home/stdplus/game/игра/img/Left3.png"),
pygame.image.load("/home/stdplus/game/игра/img/Left4.png")]#,pygame.image.load("/home/stdplus/sum104/7 ul/8  ul/11 ul/14  ul/image/pygame_left_6.png")]

def test():
    print("!")

jumpCount = 10
def drawWindow():
    global isLeft, isRight, animCount
    screen.blit(bg,(0,-100))
    screen.blit(home,(100,105))
    
    #кнопка
    #b = Button(screen, 100,100, 200, 200, pygame.font.SysFont('Arial', 40),"test", test)


    if isRight:
        screen.blit(player_right[animCount//5],(x_1,y_1))
    elif isLeft:
        screen.blit(player_left[animCount//5],(x_1,y_1))
    else:
        screen.blit(player_stand,(x_1,y_1))
    #door()
    #b.process()
    pygame.display.update()



def main():
    global x_1,y_1,dx,dy,isRight, isLeft, animCount, jumpCount, isJump#,click
    pygame.init()

    running = True
    while running:
                        
        pygame.display.update()
            # движение объекта при нажатии клавиш
        for event in pygame.event.get():
            #print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        animCount += 1
        if animCount > 24:
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
                main()
        if button_2.collidepoint((mx,my)):
            if click:
                options()
        #pygame.draw.rect(screen, (255,0,0), button_1)<-это не нужно
        screen.blit(startw,(200,122))
        #pygame.draw.rect(screen, (0,0,0), button_2)<-это не нужно
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

def secondPlase(): 
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

def door():
    
    
    door = pygame.Rect(300,345,25,75)
    while True:
        m_x,m_y = pygame.mouse.get_pos()
        if door.collidepoint((m_x,m_y)):
            if click: 
                secondPlase()
                    
        pygame.display.update()


main_menu()


