import pygame
import GIFImage
import time
import random
from pygame.locals import *

pygame.init()

width = 640
height = 640

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("ENDLESS UNDYNE?!!!!!!")


black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (38, 38, 38)
#:)
blood = (191, 0, 0)
yellow = (255, 255, 0)

song = pygame.mixer.music.load("res/spearofjustice.ogg")
pygame.mixer.music.play()
cage = pygame.image.load("res/cage.png")
blocker = pygame.image.load("res/blocker2.png")
undyne = GIFImage.GIFImage("res/undyne0.gif")
mute = pygame.image.load("res/mute.png")
cross = pygame.image.load("res/cross.png")
arrow = pygame.image.load("res/arrow.png")
#                   x    y    w   h
button_location = (260, 250, 100, 40)
button_border = (255, 245, 110, 50)
undyne_pos = (200, 0)

right_arrow = pygame.transform.rotate(arrow, 180)
arrowRight = right_arrow

top_arrow = pygame.transform.rotate(arrow, 270)
arrowTop = top_arrow

bottom_arrow = pygame.transform.rotate(arrow, 90)
arrowBottom = bottom_arrow

left_arrow = pygame.transform.rotate(arrow, 0)
arrowLeft = left_arrow



#right
arrows1 = [[640, 360]]
#top
arrows2 = [[303, 0]]
#bottom
arrows3 = [[303, 640]]
#left
arrows4 = [[0, 360]]
hp = 40

mute_button = (280, 50, 50, 50)
mute_border = (275, 45, 60, 60)

options_loc = (245, 310, 130, 40)
options_border = (240, 305, 140, 50)

back_pos = (5, 5, 100, 40)
back_border = (0, 0, 110, 50)

volume_button = mute
angle = 0

def make_title(x, y):
    
    font = pygame.font.Font("res/font.ttf", 45)
    
    title = font.render("Endless Undyne!", True, blood)
    titleRect = title.get_rect()
    titleRect.centerx = x
    titleRect.centery = y
    screen.blit(title, titleRect)



def game():
    exited = False
    x = 0
    while not exited:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                exited = True
        alive = True
        while alive:

            global timer
            global angle
            screen.fill(black)
            undyne.render(screen, undyne_pos)
            cageRect = cage.get_rect()
            cageRect.centerx = screen.get_rect().width/2 - 10
            cageRect.centery = screen.get_rect().height/2 + 50
            screen.blit(cage, cageRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        angle = 270
                    elif event.key==pygame.K_a:
                        angle = 0
                    elif event.key==pygame.K_s:
                        angle = 90
                    elif event.key==pygame.K_d:
                        angle = 180

            font = pygame.font.Font("res/font.ttf", 10)

            for health1 in range(hp):
                pygame.draw.rect(screen, gray, (278, 403, 45, 15))
                pygame.draw.rect(screen, blood, (280, 405, 40, 10))
                pygame.draw.rect(screen, yellow, (280, 405, hp, 10))
                text = font.render(str(hp) + "/40", True, white)
                screen.blit(text, (280, 415))

            if alive == True:
                arrow_left()
                arrow_right()
                arrow_top()
                arrow_bottom()

            if hp <= -1:
                alive = False

            playerRot = pygame.transform.rotate(blocker, angle)
            screen.blit(playerRot, cageRect)
            pygame.display.flip()


def randNum():
    return random.randint(1, random.randint(2500, 3000))


def hit():
    global hp
    hp -= 2


def arrow_right():
    global angle
    global hp
    speed = 0.2
    index = 0
    if randNum() == 1:
        arrows1.append([640, 360])

    # removing arrows
    for arrow1 in arrows1:
        if arrow1[0] <= 335 and angle == 180 and arrow1[0] >= 330:
            arrows1.pop(index)

        if arrow1[0] <= 310:
            hit()
            arrows1.pop(index)


        arrow1[0] -= speed
        index += 1
    for arrow1 in arrows1:
        screen.blit(arrowRight, arrow1)


def arrow_left():
    global angle
    global hp
    speed = 0.2
    index = 0

    if randNum() == 4:
        arrows4.append([0, 360])

    # removing arrows
    for arrow1 in arrows4:
        if arrow1[0] >= 265 and angle == 0 and arrow1[0] <= 270:
            arrows4.pop(index)

        if arrow1[0] >= 300:
            hit()
            arrows4.pop(index)


        arrow1[0] += speed
        index += 1

    for arrow1 in arrows4:
        screen.blit(arrowLeft, arrow1)


def arrow_top():
    global angle
    speed = 0.2
    index = 0

    if randNum() == 2:
        arrows2.append([303, 0])

    # removing arrows
    for arrow1 in arrows2:
        if arrow1[1] >= 330 and angle == 270 and arrow1[1] <=335:
            arrows2.pop(index)

        if arrow1[1] >= 360:
            hit()
            arrows2.pop(index)

        arrow1[1] += speed
        index += 1
    for arrow1 in arrows2:
        screen.blit(arrowTop, arrow1)

def arrow_bottom():
    global angle
    speed = 0.2
    index = 0

    if randNum() == 3:
        arrows3.append([303, 640])

    # removing arrows
    for arrow1 in arrows3:
        if arrow1[1] <= 390 and angle == 90 and arrow1[1] >= 385:
            arrows3.pop(index)

        if arrow1[1] <= 370:
            hit()
            arrows3.pop(index)

        arrow1[1] -= 0.2
        index += 1
    for arrow1 in arrows3:
        screen.blit(arrowBottom, arrow1)


        
def intro():
    running = True
    
    while running:
        #mouse position
        mouse = pygame.mouse.get_pos()
        #click?
        click = pygame.mouse.get_pressed()
        #filling the screen xanadu here
        screen.fill(black)
        
        
        undyne.render(screen, undyne_pos)
        
        #adding zee title
        make_title(screen.get_rect().width/2, 100)
        
        #button hover
        #        mouse x            mouse y
        if 255 < mouse[0] < 355 and 250 < mouse[1] < 300:
            pygame.draw.rect(screen, blood, button_border)
            pygame.draw.rect(screen, red, button_location)
            if click[0] == 1:
                game()
            
        else:
            pygame.draw.rect(screen, white, button_border)
            pygame.draw.rect(screen, gray, button_location)

        #a font
        text_font = pygame.font.Font("res/font.ttf", 25)
        button_text = text_font.render("START", True, white)
        textRect = button_text.get_rect()
        textRect.centerx = 310
        textRect.centery = 270
        screen.blit(button_text, textRect)
        
        
        #cuz
        pygame.display.flip()
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
           
intro()
        
        
        
