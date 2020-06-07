import pygame
import random

pygame.init()

#GameBasicVariables
ScreenLength=800
ScreenHeight=600
FPS=30
window = pygame.display.set_mode((ScreenLength,ScreenHeight))
pygame.display.set_caption("Car Game")
bg1=pygame.image.load('images/background.png')
bg2=pygame.image.load('images/background.png')

bg1y=-600
bg2y=0
FPSclock=pygame.time.Clock()

#Background Music Settings
backgroundmusic=-1
pygame.mixer.music.load('driving.wav')
pygame.mixer.music.play(backgroundmusic)


#Carlist
Carlist=[
    'images/Car1.png',
    'images/Car2.png',
    'images/Car3.png',
    'images/Car4.png',
    'images/Car5.png',
    'images/Car6.png'
]

#Player Car Settings
CarPicture=pygame.image.load('images/CarProject.png')
CarHeight=135
CarWidth=75
CarX=180
CarY=450
speed=45

#Car1 Settings
Car1Picture=pygame.image.load('images/Car1.png')
Car1X=180
Car1Y=-random.randint(200,400)
Car1Speed=speed

#Car2 Settings
Car2Picture=pygame.image.load('images/Car2.png')
Car2X=300
Car2Y=-random.randint(300,500)
Car2Speed=speed

#Car3 Settings
Car3Picture=pygame.image.load('images/Car3.png')
Car3X=420
Car3Y=-random.randint(500,650)
Car3Speed=speed

#Car4 Settings
Car4Picture=pygame.image.load('images/Car4.png')
Car4X=540
Car4Y=-random.randint(900,1000)
Car4Speed=speed

#Score and Crash
Counter=0
isCrash=False
level=1
home=True
run=True
reset=1000
#CarGrid Generation Function Start
def cargenerator():
    global Car1Y
    global Car2Y
    global Car3Y
    global Car4Y
    global reset
    Car1Y = -random.randint(1, 5)
    Car2Y = -random.randint(1, 5)
    Car3Y = -random.randint(1, 5)
    Car4Y = -random.randint(1, 5)

    while Car1Y == Car2Y:
        Car2Y = -random.randint(1, 5)
    while Car2Y == Car3Y:
        Car3Y = -random.randint(1, 5)
    while Car3Y == Car4Y:
        Car4Y = -random.randint(1, 5)

    Car1Y = Car1Y * 300
    Car1Picture = pygame.image.load(Carlist[random.randint(0, 5)])
    Car2Y = Car2Y * 300
    Car2Picture = pygame.image.load(Carlist[random.randint(0, 5)])
    Car3Y = Car3Y * 300
    Car3Picture = pygame.image.load(Carlist[random.randint(0, 5)])
    Car4Y = Car4Y * 300
    Car4Picture = pygame.image.load(Carlist[random.randint(0, 5)])
    reset=min(Car1Y,Car2Y,Car3Y,Car4Y)
#CarGrid Generation Function End


def redrawGameWindow():
    window.blit(bg1, (0, bg1y))
    window.blit(bg2, (0, bg2y))
    window.blit(CarPicture, (CarX, CarY))
    window.blit(Car1Picture,(Car1X,Car1Y))
    window.blit(Car2Picture,(Car2X,Car2Y))
    window.blit(Car3Picture,(Car3X,Car3Y))
    window.blit(Car4Picture,(Car4X,Car4Y))

    myfont=pygame.font.SysFont('Comic Sans MS', 30)
    textsurface=myfont.render(str(Counter),False,(0,0,0))
    window.blit(textsurface,(10,10))
    pygame.display.update()

#Start Screen
while run and home:

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        if keys[pygame.K_SPACE]:
            home=False

    homescreen=pygame.image.load('images/homescreen.png')
    window.blit(homescreen,(0,0))
    pygame.display.update()

#Main Program for Operations
while run and not(isCrash):
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and CarX>=150:
        CarX-=speed
    if keys[pygame.K_RIGHT] and CarX<=580:
        CarX+=speed

    bg1y=bg1y+20
    bg2y=bg2y+20

    if bg1y>=600:
        bg1y=-600
    if bg2y>=600:
        bg2y=-600

    if reset<ScreenHeight:
        Car1Y+=speed+level*2
        if(Car1Y>ScreenHeight):
            Car1Y=-2000
            Counter+=1
        Car2Y+=speed+level*2
        if (Car2Y > ScreenHeight):
            Car2Y=-2000
            Counter += 1
        Car3Y+=speed+level*2
        if (Car3Y > ScreenHeight):
            Car3Y=-2000
            Counter += 1
        Car4Y+=speed+level*2
        if (Car4Y > ScreenHeight):
            Car4Y=-2000
            Counter += 1
        reset+=speed+level*2
        print(speed+level*2)
    else:
        cargenerator()

#Crash Test
    if (CarX>Car1X-75 and CarX<Car1X+75) and (Car1Y>315 and Car1Y<585):
            isCrash=True
    if (CarX>Car2X-75 and CarX<Car2X+75) and (Car2Y>315 and Car2Y<585):
            isCrash=True
    if (CarX>Car3X-75 and CarX<Car3X+75) and (Car3Y>315 and Car3Y<585):
            isCrash=True
    if (CarX>Car4X-75 and CarX<Car4X+75) and (Car4Y>315 and Car4Y<585):
            isCrash=True

    level=1+int(Counter/10)
    redrawGameWindow()
    FPSclock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.music.load('crash.wav')
pygame.mixer.music.play()

while run and isCrash:
    window.blit(bg1, (0, bg1y))
    window.blit(bg2, (0, bg2y))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textGameOver = myfont.render('GAME OVER', False, (255, 0, 0))
    window.blit(textGameOver, (300, 200))
    textsurface = myfont.render(str(Counter), False,(255,0,0))
    window.blit(textsurface, (400,300))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False

pygame.quit()


