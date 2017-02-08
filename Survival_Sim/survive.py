# 1 - Import library
import pygame
from pygame.locals import *
import random
import time

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
#3 - Loading Images
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
y=random.randint(0,2)
if y==0:
    grass = pygame.image.load("resources/images/grass.png")
if y==1:
    grass = pygame.image.load("resources/images/grass1.png")
if y==2:
    grass = pygame.image.load("resources/images/grass2.png")
a=random.randint(0,2)
if a==0:
    rescue = pygame.image.load("resources/images/rescue1.png")
if a==1:
    rescue = pygame.image.load("resources/images/rescue2.png")
if a==2:
    rescue = pygame.image.load("resources/images/rescue3.png")
sleep = pygame.image.load("resources/images/sleep.png")
survive = pygame.image.load("resources/images/survive.png")
food = pygame.image.load("resources/images/food.png")
greenoverlay = pygame.image.load("resources/images/dead.png")
pygame.mixer.music.load('resources/audio/CreepyWind.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.30)
#1
energyval=194
hydrationval=194
bodyheatval=194
inventoryl=['wood','berries','meat','water']
amount=[1,3,2,5]
running=1
foragecount=0
woodcount=0
watercount=0
huntcount=0
todol=['Sleep','Forage','Cut Wood','Eat','Hunt','collectwater','drink','Fire']
#2
def start():
    pygame.display.set_caption("Survive")
    for x in range(width/survive.get_width()+1):
        for y in range(height/survive.get_height()+1):
            screen.blit(survive,(x*100-99,y*200-90))
    pygame.display.flip()
    time.sleep(4)
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def Sleep():
    screen.fill(255)
    for x in range(width/sleep.get_width()+1):
        for y in range(height/sleep.get_height()+1):
            screen.blit(sleep,(x*100,y*100))
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('Sleep', True, (238,130,238))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-190
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('1- Rest - A quick nap for required relaxation', True, (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-100
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('2- Sleep - A good sleep, replenshises senses', True, (255,255,255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-25
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('3- Deep Slumber- Too tired?This way to go.', True, (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery+50
    screen.blit(text, textrect)
    pygame.display.flip()
    time.sleep(2)

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_q:
                todo(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
            if event.key==K_1:
                rest(energyval,bodyheatval,hydrationval)
            if event.key==K_2:
                sleepr(energyval,bodyheatval,hydrationval)
            if event.key==K_3:
                slumber(energyval,bodyheatval,hydrationval)

def rest(energyval,bodyheatval,hydrationval):
    if energyval>=194:
       pass
    else:
        enregyval+=10
    bodyheatval-=10
    hydrationval-=20
    if energyval>194:
        energyval=194
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def sleepr(energyval,bodyheatval,hydrationval):
    if energyval>=194:
        pass
    else:
        enregyval+=25
    bodyheatval-=15
    hydrationval-=25
    if energyval>194:
        energyval=194
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def slumber(energyval,bodyheatval,hydrationval):
    if energyval>=194:
        pass
    else:
        enregyval+=60
    if energyval>194:
        energyval=194
    bodyheatval-=30
    hydrationval-=50
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def Forage(energyval,bodyheatval,hydrationval,foragecount,amount):

    if foragecount<5:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Foraging', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)
        foragecount +=1
        energyval=energyval-10
        hydrationval=hydrationval-10
        bodyheatval=bodyheatval+5
        berriesc=random.randint(0,3)
        amount[1]+=berriesc
        main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def cutwood(energyval,bodyheatval,hydrationval,woodcount,amount):

    if woodcount<5:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Cutting', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)
        woodcount +=1
        energyval=energyval-15
        hydrationval=hydrationval-15
        bodyheatval=bodyheatval+5
        woodc=random.randint(0,3)
        amount[0]+=woodc
        main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def hunt(energyval,bodyheatval,hydrationval,huntcount,amount):

    if huntcount<5:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Hunting', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(0.5)
        huntcount +=1
        energyval=energyval-40
        hydrationval=hydrationval-20
        bodyheatval=bodyheatval+10
        woodc=random.randint(0,3)
        amount[0]+=woodc

    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def collect(energyval,bodyheatval,hydrationval,watercount,amount):

    if watercount<5:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Collecting Water', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(0.5)
        watercount +=1
        energyval=energyval-5
        hydrationval=hydrationval-5
        bodyheatval=bodyheatval+5
        woodc=random.randint(0,3)
        amount[3]+=woodc
    else:
        pass
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def drink(energyval,bodyheatval,hydrationval,amount):

    if amount[3]>0:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Drinking', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)
        hydrationval=hydrationval+70
        if hydrationval>194:
            hydrationval=194
        bodyheatval=bodyheatval-5
        amount[3]-=1
        main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def fire(energyval,bodyheatval,hydrationval,amount):

    if amount[0]>0:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Heating', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)

        energyval=energyval-10
        hydrationval=hydrationval-20
        bodyheatval=180
        if bodyheatval>194:
            bodyheatval=194
        amount[0]-=1
    else:
       pass
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def eat(energyval,bodyheatval,hydrationval,amount):
    screen.fill(255)
    for x in range(width/food.get_width()+1):
        for y in range(height/food.get_height()+1):
            screen.blit(food,(x*100,y*100))
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('Eat', True, (105, 90, 87))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-190
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('1- Eat Meat', True, (105, 90, 87))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-100
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('2- Eat Berries', True, (105, 90, 87))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-30
    textrect.centery = screen.get_rect().centery-25
    screen.blit(text, textrect)
    basicfont = pygame.font.SysFont(None, 36)
    pygame.display.flip()
    time.sleep(2)

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_q:
                todo()
            if event.key==K_1:
                eatmeat(energyval,bodyheatval,hydrationval,amount)
            if event.key==K_2:
                eatberries(energyval,bodyheatval,hydrationval,amount)

def eatmeat(energyval,bodyheatval,hydrationval,amount):
    if amount[2]>0:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Eating Meat', True, (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)
        energyval=energyval+40
        hydrationval=hydrationval-10
        bodyheatval=bodyheatval+10
        amount[2]-=1
        if hydrationval>194:
            hydrationval=194
        if bodyheatval>194:
            bodyheatval=194
        if energyval>194:
            energyval=194
    else:
        pass
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def eatberries(energyval,bodyheatval,hydrationval,amount):
    if amount[1]>0:
        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render('Eating Berries', True, (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-30
        textrect.centery = screen.get_rect().centery+50
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(1)
        energyval=energyval+20
        hydrationval=hydrationval+20
        bodyheatval=bodyheatval+5
        amount[1]-=1
        if hydrationval>194:
            hydrationval=194
        if bodyheatval>194:
            bodyheatval=194
        if energyval>194:
            energyval=194
    else:
        pass
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
def todo(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount):
    screen.fill(0)
    screen.blit(healthbar, (5,5))
    for health1 in range(int(energyval)):
        screen.blit(health, (health1+8,8))
    screen.blit(healthbar, (5,40))
    for health2 in range(int(hydrationval)):
        screen.blit(health, (health2+8,43))
    screen.blit(healthbar, (5,75))
    for health2 in range(int(bodyheatval)):
        screen.blit(health, (health2+8,78))
    energyval-=20
    bodyheatval-=20
    hydrationval-=20

    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('To Do?', True, (255,127,80))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-60
    textrect.centery = screen.get_rect().centery-190
    screen.blit(text, textrect)
    for i in range(len(todol)):

        text = basicfont.render(str(i+1), True, (105, 190, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-80
        textrect.centery = screen.get_rect().centery-90+30*i
        screen.blit(text, textrect)

        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render(str(todol[i]), True, (105, 190, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx+20
        textrect.centery = screen.get_rect().centery-90+30*i
        screen.blit(text, textrect)

    pygame.display.flip()
    time.sleep(3)

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_q:
                main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
            if event.key==K_1:
                Sleep()
            if event.key==K_2:
                Forage(energyval,bodyheatval,hydrationval,foragecount,amount)
            if event.key==K_3:
                cutwood(energyval,bodyheatval,hydrationval,woodcount,amount)
            if event.key==K_4:
                eat(energyval,bodyheatval,hydrationval,amount)
            if event.key==K_5:
                hunt(energyval,bodyheatval,hydrationval,huntcount,amount)
            if event.key==K_6:
                collect(energyval,bodyheatval,hydrationval,watercount,amount)
            if event.key==K_7:
                drink(energyval,bodyheatval,hydrationval,amount)
            if event.key==K_8:
                fire(energyval,bodyheatval,hydrationval,amount)

    p=random.randint(50,100)
    a=random.randint(0,4)
    b=random.randint(0,4)
    c=random.randint(0,4)

    for j in range(180):
     if 5000*j<pygame.time.get_ticks()<5000*j+p:
        energyval-=(a)
        bodyheatval-=b
        hydrationval-=c


def inventory(energyval,bodyheatval,hydrationval):
    energyval-=2
    bodyheatval-=4
    hydrationval-=5
    screen.fill(0)
    basicfont = pygame.font.SysFont(None, 36)
    text = basicfont.render('Inventory', True, (105, 190, 0))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-60
    textrect.centery = screen.get_rect().centery-190
    screen.blit(text, textrect)
    for i in range(len(inventoryl)):

        text = basicfont.render(str(inventoryl[i]), True, (105, 190, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx-60
        textrect.centery = screen.get_rect().centery-90+40*i
        screen.blit(text, textrect)

        basicfont = pygame.font.SysFont(None, 36)
        text = basicfont.render(str(amount[i]), True, (105, 190, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery-90+40*i
        screen.blit(text, textrect)

    pygame.display.flip()
    time.sleep(5)
    main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_q:
                pass

        if event.type == pygame.KEYUP:
            if event.key==pygame.K_q:
                keys[3]=False


def main(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount):
 while 1:
    init=time.time()
    screen.fill(0)
    pygame.display.set_caption("Survive")
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(healthbar, (5,5))
    for health1 in range(int(energyval)):
        screen.blit(health, (health1+8,8))
    screen.blit(healthbar, (5,40))
    for health2 in range(int(hydrationval)):
        screen.blit(health, (health2+8,43))
    screen.blit(healthbar, (5,75))
    for health2 in range(int(bodyheatval)):
        screen.blit(health, (health2+8,78))
    basicfont = pygame.font.SysFont(None, 26)
    text = basicfont.render('Energy', True, (0, 255, 0))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-60
    textrect.centery = screen.get_rect().centery-225
    screen.blit(text, textrect)

    basicfont = pygame.font.SysFont(None, 26)
    text = basicfont.render('Hydration', True, (0, 0, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-60
    textrect.centery = screen.get_rect().centery-190
    screen.blit(text, textrect)

    basicfont = pygame.font.SysFont(None, 26)
    text = basicfont.render('Heat', True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx-60
    textrect.centery = screen.get_rect().centery-155
    screen.blit(text, textrect)

    font = pygame.font.Font("freesansbold.ttf", 24)
    bigfont = pygame.font.Font("freesansbold.ttf", 36)
        # Render text

    gameover = bigfont.render('Press i to open inventory.', True, (0,0,0))
    gameoverRect = gameover.get_rect()
    gameoverRect.centerx = screen.get_rect().centerx
    gameoverRect.centery = screen.get_rect().centery+24
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, gameoverRect)

    gameover = bigfont.render(' Press t to open to do list.', True, (0,0,0))
    gameoverRect = gameover.get_rect()
    gameoverRect.centerx = screen.get_rect().centerx
    gameoverRect.centery = screen.get_rect().centery-50
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24

    # Draw text
    screen.blit(gameover, gameoverRect)

    gameover = font.render(' Press button multiple times for better results', True, (0,0,0))
    gameoverRect = gameover.get_rect()
    gameoverRect.centerx = screen.get_rect().centerx
    gameoverRect.centery = screen.get_rect().centery+100
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24

    # Draw text
    screen.blit(gameover, gameoverRect)
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_i:
                inventory(energyval,bodyheatval,hydrationval)
            elif event.key==K_t:
                todo(energyval,hydrationval,bodyheatval,woodcount,foragecount,huntcount,watercount,amount)
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_t:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    #if keys[0]:
     # inventory()
    if keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5
    final=time.time()
    p=random.randint(50,100)
    a=random.randint(0,4)
    b=random.randint(0,4)
    c=random.randint(0,4)

    for j in range(180):
     if 5000*j<pygame.time.get_ticks()<5000*j+p:
        energyval-=(a)
        bodyheatval-=b
        hydrationval-=c
    if energyval < 0:
        y=pygame.time.get_ticks()

        # Initialize the font
        pygame.font.init()
        # Set font
        font = pygame.font.Font("freesansbold.ttf", 18)
        bigfont = pygame.font.Font("freesansbold.ttf", 24)
        # Render text
        for x in range(width/greenoverlay.get_width()+1):
            for z in range(height/greenoverlay.get_height()+1):
                screen.blit(greenoverlay,(x*500,z*500))
        gameover = bigfont.render('''You died due to lack of energy''', True, (0,255,0))
        gameoverRect = gameover.get_rect()
        gameoverRect.centerx = screen.get_rect().centerx
        gameoverRect.centery = screen.get_rect().centery-24
        text = font.render("Time: "+str(y/1000.0)+'seconds', True, (0,255,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24

        # Draw text
        screen.blit(gameover, gameoverRect)
        screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(100000)
    if bodyheatval < 0:
        y=pygame.time.get_ticks()

        # Initialize the font
        pygame.font.init()
        # Set font
        font = pygame.font.Font("freesansbold.ttf", 18)
        bigfont = pygame.font.Font("freesansbold.ttf", 24)
        # Render text
        for x in range(width/greenoverlay.get_width()+1):
            for z in range(height/greenoverlay.get_height()+1):
                screen.blit(greenoverlay,(x*500,z*500))
        gameover = bigfont.render('''You died due to hypothermia''', True, (255,0,0))
        gameoverRect = gameover.get_rect()
        gameoverRect.centerx = screen.get_rect().centerx
        gameoverRect.centery = screen.get_rect().centery-24
        text = font.render("Time: "+str(y/1000.0)+'seconds', True, (255,0,0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24

        # Draw text
        screen.blit(gameover, gameoverRect)
        screen.blit(text, textRect)
        pygame.display.flip()
        pygame.time.wait(100000)
    if hydrationval < 0:
        y=pygame.time.get_ticks()

        # Initialize the font
        pygame.font.init()
        # Set font
        font = pygame.font.Font("freesansbold.ttf", 18)
        bigfont = pygame.font.Font("freesansbold.ttf", 24)
        # Render text
        for x in range(width/greenoverlay.get_width()+1):
            for z in range(height/greenoverlay.get_height()+1):
                screen.blit(greenoverlay,(x*500,z*500))
        gameover = bigfont.render('''You died due to Thirst''', True, (0,0,255))
        gameoverRect = gameover.get_rect()
        gameoverRect.centerx = screen.get_rect().centerx
        gameoverRect.centery = screen.get_rect().centery-24
        text = font.render("Time: "+str(y/1000.0)+"seconds", True, (0,0,255))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24

        # Draw text
        screen.blit(gameover, gameoverRect)
        screen.blit(text, textRect)

        pygame.display.flip()
        pygame.time.wait(100000)
    if pygame.time.get_ticks()>=300000:
        pygame.font.init()
        # Set font
        font = pygame.font.Font("freesansbold.ttf", 18)
        bigfont = pygame.font.Font("freesansbold.ttf",24)
        # Render text
        for x in range(width/rescue.get_width()+1):
            for z in range(height/rescue.get_height()+1):
                screen.blit(rescue,(x*500,z*500))
        gameover = bigfont.render('''You were rescued''', True, (0,0,255))
        gameoverRect = gameover.get_rect()
        gameoverRect.centerx = screen.get_rect().centerx
        gameoverRect.centery = screen.get_rect().centery-24
        text = font.render("Time: "+str(y/1000.0)+"seconds", True, (0,0,255))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery+24

        # Draw text
        screen.blit(gameover, gameoverRect)
        screen.blit(text, textRect)

        pygame.display.flip()
        pygame.time.wait(100000)

start()
