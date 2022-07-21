import pygame
#from button import Button

width = 500
height = 500
animCount = 0
isJump = False
isRight = False
isLeft = False
x = 100
y = 100
dy = 2
dx = 2

#размер окна
screen = pygame.display.set_mode([width, height])
#задний фон 
bg = pygame.image.load("/home/stdplus/game/image/pygame_bg.jpg")
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
    screen.blit(bg,(0,0))
    #кнопка
    #b = Button(screen, 100,100, 200, 200, pygame.font.SysFont('Arial', 40),"test", test)


    if isRight:
        screen.blit(player_right[animCount//5],(x,y))
    elif isLeft:
        screen.blit(player_left[animCount//5],(x,y))
    else:
        screen.blit(player_stand,(x,y))
    
    #b.process()
    pygame.display.update()


def main():
    global x,y,dx,dy,isRight, isLeft, animCount, jumpCount, isJump
    pygame.init()
    
    running = True

    pygame.display.update()
    # движение объекта при нажатии клавиш
    while running:
        animCount += 1
        if animCount > 24:
            animCount = 0
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x > 0:
            x -= dx
            isLeft = True
        else:
            isLeft = False
        if keys[pygame.K_d] and x< 440:
            x += dx
            isRight = True
        else:
            isRight = False
        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
            if keys[pygame.K_w] and y > 0:
                y -= dy
            if keys[pygame.K_s] and y< 435:
                y += dy
        else:
            if jumpCount > 0:
                y -= (jumpCount**2)/2
            else:
                y += (jumpCount**2)/2
            jumpCount -= 1
            if jumpCount == -11:
                isJump = False
                jumpCount = 10

        
            
          
        drawWindow()
    pygame.quit()


if __name__ == '__main__':
    main()