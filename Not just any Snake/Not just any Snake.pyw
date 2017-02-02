import pygame
import time
import random

pygame.init()
#CONSTANTS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,150,0)
FPS = 10
AppleThickness = 20
#variables
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
block_size = 20
iconImg = pygame.image.load('icon.png')
pygame.display.set_icon(iconImg)
img = pygame.image.load('snakehead.png')
body = pygame.image.load('snakebody.png')
apple = pygame.image.load('apple.png')
background = pygame.image.load('background.png')
introImg = pygame.image.load('intro.png')

direction = "right"
smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 75)

pygame.display.set_caption('Not just any Snake')

def quit_game():
    pygame.quit()
    quit()

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False   
    
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
                     
    for XnY in snakelist[:-1]:
        gameDisplay.blit(body, (XnY[0],XnY[1]))

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX,randAppleY

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
        
    return textSurface, textSurface.get_rect()

def message(msg,color,x_displace = 0, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2 + x_displace, display_height/2 + y_displace)
    gameDisplay.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        quit_game()
                    if event.key == pygame.K_c:
                        game_loop()
                        
        gameDisplay.blit(introImg,(0, 0))
        message('Welcome to Not just any Snake', GREEN, y_displace = -150, size = 'large')
        message('The objective of the game is to eat the red apples.', BLACK, y_displace = -30)
        message('The more apples you eat the longer you get.', BLACK, y_displace = 10)
        message('If you run into yourself or the edges you die.', BLACK, y_displace = 50)
        message('Press C to play or Q to quit.', BLACK, y_displace = 180)
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    global direction
    direction = 'right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0, display_width - block_size))
    randAppleY = round(random.randrange (0, display_height - block_size))

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(WHITE)
            message('Game Over!',RED,y_displace = -50, size = "large")
            message('Press C to continue playing or Q to quit.', BLACK,y_displace = 50, size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        quit_game()
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            
            print randAppleX, randAppleY, AppleThickness
            print lead_x, lead_y, block_size
            
            if event.type == pygame.QUIT:
                gameExit = True
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.blit(background,(0, 0))
        
        gameDisplay.blit(apple,(randAppleX, randAppleY))
          
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
    
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                time.sleep(1)
                gameOver = True
        
        snake(block_size,snakeList)
        message('Score: %d' %snakeLength,BLACK, -350, -275)
        pygame.display.update() 

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
            
        clock.tick(FPS)

game_intro()
game_loop()
