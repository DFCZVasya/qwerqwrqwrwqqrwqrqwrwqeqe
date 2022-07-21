import pygame,sys
#движение акулы
shark_1 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark1_8.png")
]
shark_2 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark2_8.png")]

shark_3 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark3_8.png")
]
shark_4 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark4_8.png")
]
shark_5 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark5_8.png")]

shark_6 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark6_8.png")]

shark_7 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark7_8.png")]

shark_8 = [pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_1.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_2.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_3.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_4.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_5.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_6.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_7.png"),
pygame.image.load("/home/stdplus/game/игра/босс/финал/shark8_8.png")]


swim = pygame.image.load('/home/stdplus/game/игра/босс/swim.png')
viu = pygame.image.load('/home/stdplus/game/игра/босс/финал/viu.png')

sh1AnimCount = 0
sh2AnimCount = 0
sh3AnimCount = 0
sh4AnimCount = 0
sh5AnimCount = 0
sh6AnimCount = 0
sh7AnimCount = 0
sh8AnimCount = 0

is_shark1_right = True
is_shark2_right = True
is_shark3_right = True
is_shark4_right = True
is_shark5_right = True
is_shark6_right = True
is_shark7_right = True
is_shark8_right = True

'''
if is_shark1_right:
    display.blit(shark_1[sh1AnimCount//6],(0,0))
if is_shark2_right:
    display.blit(shark_2[sh2AnimCount//6],(0,0))
if is_shark3_right:
    display.blit(shark_3[sh3AnimCount//6],(0,0))
if is_shark4_right:
    display.blit(shark_4[sh4AnimCount//6],(0,0))
if is_shark5_right:
    display.blit(shark_5[sh5AnimCount//6],(0,0))
if is_shark6_right:
    display.blit(shark_6[sh6AnimCount//6],(0,0))
if is_shark7_right:
    display.blit(shark_7[sh7AnimCount//6],(0,0))
if is_shark8_right:
    display.blit(shark_8[sh8AnimCount//6],(0,0))

sh1AnimCount += 1
sh2AnimCount += 1
sh3AnimCount += 1
sh4AnimCount += 1
sh5AnimCount += 1
sh6AnimCount += 1
sh7AnimCount += 1
sh8AnimCount += 1

if sh1AnimCount > 60:
        sh1AnimCount = 0
        is_shark1_right = not is_shark1_right
if sh2AnimCount > 60:
        sh2AnimCount = 0
        is_shark2_right = not is_shark2_right
if sh3AnimCount > 60:
        sh3AnimCount = 0
        is_shark3_right = not is_shark3_right
if sh4AnimCount > 60:
        sh4AnimCount = 0
        is_shark4_right = not is_shark4_right
if sh5AnimCount > 60:
        sh5AnimCount = 0
        is_shark5_right = not is_shark5_right
if sh6AnimCount > 60:
        sh6AnimCount = 0
        is_shark6_right = not is_shark6_right
if sh7AnimCount > 60:
        sh7AnimCount = 0
        is_shark7_right = not is_shark7_right
if sh8AnimCount > 60:
        sh8AnimCount = 0
        is_shark8_right = not is_shark8_right

def boss():
    # появление водоворота
    xv =30
    yv = 30
    
    
    xr = str(random.randint(0,8))
    print(xr)
    yr = str(random.randint(0,8))
    print(yr)
    if xr == '1':
        xv +=0
       
        display.blit(viu,(xv,yv))
    if xr == '2':
        xv +=60
        display.blit(viu,(xv,yv))
    if xr == '3':
        xv +=120
        display.blit(viu,(xv,yv))
    if xr == '4':
        xv +=180
        display.blit(viu,(xv,yv))
    if xr == '5':
        xv +=240
        display.blit(viu,(xv,yv))
    if xr == '6':
        xv +=300
        display.blit(viu,(xv,yv))
    if xr == '7':
        xv +=360
        display.blit(viu,(xv,yv))
    if xr == '8':
        xv +=420
        display.blit(viu,(xv,yv))
    
    
    if yr == '1':
        yv +=0
        display.blit(viu,(xv,yv))
    if xr == '2':
        yv +=60
        display.blit(viu,(xv,yv))
    if yr == '3':
        yv +=120
        display.blit(viu,(xv,yv))
    if yr == '4':
        yv +=180
        display.blit(viu,(xv,yv))
    if yr == '5':
        yv +=240
        display.blit(viu,(xv,yv))
    if yr == '6':
        yv +=300
        display.blit(viu,(xv,yv))
    if yr == '7':
        yv +=360
        display.blit(viu,(xv,yv))
    if yr == '8':
        yv +=420
        display.blit(viu,(xv,yv))
    

#появление акулы
    xs = str(random.randint(0,8))
    print(xr)

    if xs == '1':
        display.blit(shark_1,(0,0))
    if xs == '2':
        
        display.blit(shark_2,(0,0))
    if xs == '3':
        
        display.blit(shark_3,(0,0))
    if xs == '4':
        
        display.blit(shark_4,(0,0))
    if xs == '5':
       
        display.blit(shark_5,(0,0))
    if xs == '6':
        
        display.blit(shark_6,(0,0))
    if xs == '7':
        
        display.blit(shark_7,(0,0))
    if xs == '8':
        
        display.blit(shark_8,(0,0))

#движение персонажа
xp = 30
yp =30
for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    xp += 60 
                    display.blit(swim,(xp,yp))

                if event.key == K_LEFT:
                    xp -= 60
                    display.blit(swim,(xp,yp))
                    
                if event.key == K_UP:
                    yp -= 60
                    display.blit(swim,(xp,yp))
                if event.key == K_ESCAPE:
                    return
                if event.key == K_DOWN:
                    yp += 60
                    display.blit(swim,(xp,yp))

sh1AnimCount += 1
sh2AnimCount += 1
sh3AnimCount += 1
sh4AnimCount += 1
sh5AnimCount += 1
sh6AnimCount += 1
sh7AnimCount += 1
sh8AnimCount += 1
if sh1AnimCount > 60:
        sh1AnimCount = 0
        is_shark1_right = not is_shark1_right
if sh2AnimCount > 60:
        sh2AnimCount = 0
        is_shark2_right = not is_shark2_right
if sh3AnimCount > 60:
        sh3AnimCount = 0
        is_shark3_right = not is_shark3_right
if sh4AnimCount > 60:
        sh4AnimCount = 0
        is_shark4_right = not is_shark4_right
if sh5AnimCount > 60:
        sh5AnimCount = 0
        is_shark5_right = not is_shark5_right
if sh6AnimCount > 60:
        sh6AnimCount = 0
        is_shark6_right = not is_shark6_right
if sh7AnimCount > 60:
        sh7AnimCount = 0
        is_shark7_right = not is_shark7_right
if sh8AnimCount > 60:
        sh8AnimCount = 0
        is_shark8_right = not is_shark8_right
'''