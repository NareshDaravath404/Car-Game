import pygame
import random
import time
from pygame import mixer


pygame.init()
display_width=800
display_height=600


screen=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CAR GAME")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pause= False

green=(0,255,0)
gray=(119,118,110)
white=(255,255,255)
red=(255,0,0)
bright_green=(127,255,0)
bright_red=(255,69,0)
bright_blue=(39,64,139)
blue=(0,0,250)

clock=pygame.time.Clock()
intro_background=pygame.image.load("introimage.jpg")
intro_background2=pygame.image.load("background2.jpg")
intro_background3=pygame.image.load("background3.jpg")
car_image=pygame.image.load("car.png")
green_image=pygame.image.load("green1.png")
line_image=pygame.image.load("line1.jpg")

white_image=pygame.image.load("white.jpg")

def enter_loop():
    enter=True
    while  enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(intro_background,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",110)
        textsurf,textrect=text_objects("CAR GAME",largetext)
        textrect.center=(400,100)
        screen.blit(textsurf,textrect)
        button("START" ,150,520,100,50,green,bright_green,"play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)

def button(msg, x, y, w, h, ic, ac, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                enter_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)

def introduction():
    introduction= True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(intro_background2,(0,0))
        largetext=pygame.font.Font("freesansbold.ttf",80)
        smalltext=pygame.font.Font("freesansbold.ttf",20)
        mediumtext=pygame.font.Font("freesansbold.ttf",40)
        textsurf,textrect=text_objects("This is an Car Game in which you need to dodge the coming cars",smalltext)
        textrect.center=((350),(200))
        Textsurf,Textrect=text_objects("INSTRUCTIONS",largetext)
        Textrect.center=(400,100)
        screen.blit(Textsurf,Textrect)
        screen.blit(textsurf,textrect)
        stextsurf, stextrect = text_objects("ARROW LEFT : LEFT TURN", smalltext)
        stextrect.center=(300,400)
        htextsurf, htextrect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        htextrect.center=(300,450)
        atextsurf, atextrect = text_objects("A : ACCELERATOR", smalltext)
        atextrect.center=(300,500)
        rtextsurf, rtextrect = text_objects("B : BRAKE", smalltext)
        rtextrect.center=(300,550)
        ptextsurf, ptextrect = text_objects("P : PAUSE ", smalltext)
        ptextrect.center=(300,350)
        sTextsurf, sTextrect = text_objects("CONTROLS:",mediumtext)
        sTextrect.center=(150,300)
        screen.blit(sTextsurf, sTextrect)
        screen.blit(stextsurf, stextrect)
        screen.blit(htextsurf, htextrect)
        screen.blit(atextsurf, atextrect)
        screen.blit(rtextsurf, rtextrect)
        screen.blit(ptextsurf, ptextrect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)
def paused():
    global pause
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(intro_background3,(0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 110)
        textsurf, textrect = text_objects("PAUSED", largetext)
        textrect.center = ((display_width/2),(display_height/2))
        screen.blit(textsurf, textrect)
        button("CONTINUE", 150, 450, 150, 50, green, bright_green,"unpause")
        button("RESTART", 350, 450, 150, 50, blue,  bright_blue, "play")
        button("MAIN MENU", 550, 450, 200, 50, red,bright_red, "menu")
        pygame.display.update()
        clock.tick(30)
def unpaused():
    global pause
    pause = False
def gameover():
    game_over=True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(intro_background3,(0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 90)
        textsurf, textrect = text_objects("GAME OVER", largetext)
        textrect.center = ((display_width/2),(display_height/2))
        screen.blit(textsurf, textrect)
        button("RESTART", 150, 450, 150, 50, blue,  bright_blue, "play")
        button("MAIN MENU", 450, 450, 200, 50, red,bright_red, "menu")
        pygame.display.update()
        clock.tick(30)
def score_system(passed,score):
    font=pygame.font.SysFont(None,40)
    text=font.render("PASSED:" + str(passed),True,(0,0,0))
    score = font.render("SCORE:" + str(score), True, red)
    screen.blit(text,(0,50))
    screen.blit(score,(0,20))

def text_objects(text,font):
    text_surface=font.render(text,True,(0,0,0))
    return text_surface,text_surface.get_rect()
def message(text):
    largetext=pygame.font.Font("freesansbold.ttf",60)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    screen.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
def crashed():
    message("YOU CRASHED!!")
def car(car_x,car_y):
    screen.blit(car_image,(car_x,car_y))
def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("carx1.png")
    elif obs==1:
        obs_pic = pygame.image.load("carx2.png")
    elif obs==2:
        obs_pic = pygame.image.load("carx3.png")
    elif obs==3:
        obs_pic = pygame.image.load("carx4.png")
    elif obs==4:
        obs_pic = pygame.image.load("carx5.png")
    elif obs==5:
        obs_pic = pygame.image.load("carx6.png")
    elif obs==6:
        obs_pic = pygame.image.load("carx7.png")
    elif obs==7:
        obs_pic = pygame.image.load("car.png")
    screen.blit(obs_pic,(obs_startx,obs_starty))


def game_loop():
    global pause

    running = True
    obstacle_speed = 14
    obs = 0
    y_change = 0
    car_x = 300
    car_y = 480
    car_x_change = 0
    car_width = 60
    car_height = 120
    obs_startx = random.randrange(180, (display_width - 240))
    obs_starty = -750
    obs_width = 60
    obs_height = 120
    passed = 0
    level = 0
    score = 0
    y2=7
    fps=120
    while running:
        screen.fill(gray)
        screen.blit(white_image, (390, 10))
        screen.blit(white_image, (390, 100))
        screen.blit(white_image, (390, 190))
        screen.blit(white_image, (390, 280))
        screen.blit(white_image, (390, 370))
        screen.blit(white_image, (390, 460))
        screen.blit(white_image, (390, 550))
        screen.blit(green_image, (0, 0))
        screen.blit(green_image, (622, 0))
        screen.blit(line_image, (180, 0))
        screen.blit(line_image, (610, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change -= 10
                if event.key == pygame.K_RIGHT:
                    car_x_change += 10
                if event.key == pygame.K_a:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        if car_x <= 170:
            explosion_sound = mixer.Sound("crash.wav")
            explosion_sound.play()
            crashed()
            gameover()
        if car_x >= 560:
            explosion_sound = mixer.Sound("crash.wav")
            explosion_sound.play()
            crashed()
            gameover()

        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(180, (display_width - 240))
            obs = random.randrange(0, 7)
            passed += 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                largetext = pygame.font.Font("freesansbold.ttf", 50)
                textsurf, textrect = text_objects("LEVEL " + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                screen.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(2)

        if car_y < obs_starty + obs_height:
            if car_x > obs_startx and car_x < obs_startx + obs_width or car_x + car_width > obs_startx and car_x + car_width < obs_startx + obs_width:
                explosion_sound = mixer.Sound("crash.wav")
                explosion_sound.play()
                crashed()
                gameover()


        obs_starty -= (obstacle_speed / 4)

        obs_starty += obstacle_speed
        car_x += car_x_change
        score_system(passed, score)
        obstacle(obs_startx, obs_starty, obs)


        car(car_x, car_y)
        button("PAUSE",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)
enter_loop()
introduction()
game_loop()





