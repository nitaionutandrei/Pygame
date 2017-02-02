import pygame #First, import the pygame module
import time
import random

pygame.init() #We need to initialize pygame

crash_sound = pygame.mixer.Sound('crash.ogg')
pygame.mixer.music.load('soundtrack.ogg')

display_width=800 #set window display width
display_height=600 #set window display height
black = (0,0,0) #set black tuple
white = (255,255,255) #set white tuple
red = (200,0,0) #set red tuple
bright_red = (255,0,0)
green = (0,200,0) #set green tuple
bright_green = (0,255,0)
blue = (0,0,255) #set blue tuple
bright_blue = (0,0,200)
car_width = 63 #set the width of the car image
car_height = 128
score = 0
pause = False
keys = [False, False, False, False]

gameDisplay = pygame.display.set_mode((display_width,display_height)) #We setup the display with a custom resolution
pygame.display.set_caption('Race to Win') #We set the title of the game which will show on the window
clock = pygame.time.Clock() #We need to set up the game clock
carImg = pygame.image.load('racecar.png')#load the car image
backgroundImg = pygame.image.load('background.jpg')#load the background image
yellowCarImg = pygame.image.load('yellowCar.png')
greenCarImg = pygame.image.load('greenCar.png')
introImg = pygame.image.load('intro.jpg')
iconImg = pygame.image.load('icon.png')
playButton = pygame.image.load('playButton.png')
playAgainButton = pygame.image.load('playAgainButton.png')
exitButton = pygame.image.load('exitButton.png')
continueButton = pygame.image.load('continueButton.png')
pygame.display.set_icon(iconImg)
                          
def car(x,y): #car defining function
    gameDisplay.blit(carImg,(x,y)) #blit the image on the screen

def yellowCar(thingx, thingy):
    gameDisplay.blit(yellowCarImg,(thingx,thingy)) #blit the image on the screen

def greenCar(thingx, thingy):
    gameDisplay.blit(greenCarImg,(thingx,thingy))

def introImage(introx,introy):
    gameDisplay.blit(introImg,(introx,introy))
      
def message_display2(text):
    largeText = pygame.font.Font('freesansbold.ttf',35)
    TextSurf, TextRect = blue_text_objects(text, largeText)
    TextRect.center = (200,50)
    gameDisplay.blit(TextSurf, TextRect)

def black_text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
	
def red_text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
	
def blue_text_objects(text,font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def  button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    if 550+w > mouse[0] > 550 and y+h > mouse[1] > y:    
        pygame.draw.rect(gameDisplay,bright_red,(550,y,w,h))
    else:
        pygame.draw.rect(gameDisplay,red,(550,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = black_text_objects(msg,smallText)
    textRect.center = (x+(100/2),450+(50/2))
    gameDisplay.blit(textSurf, textRect)

    textSurf, textRect = black_text_objects("Quit",smallText)
    textRect.center = (550+(100/2),450+(50/2))
    gameDisplay.blit(textSurf, textRect)

def  button2(x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
    else:
        pass

    if 550+w > mouse[0] > 550 and y+h > mouse[1] > y:    
        if click[0] == 1 and action != None:
            quitgame()
    else:
        pass

##    smallText = pygame.font.Font("freesansbold.ttf",20)
##    textSurf, textRect = black_text_objects(msg,smallText)
##    textRect.center = (x+(100/2),450+(50/2))
##    gameDisplay.blit(textSurf, textRect)
##
##    textSurf, textRect = black_text_objects("Quit",smallText)
##    textRect.center = (550+(100/2),450+(50/2))
##    gameDisplay.blit(textSurf, textRect)

def game_intro():
    global smallText
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        introImage(0,0)       
        gameDisplay.blit(playButton,(150,450))
        gameDisplay.blit(exitButton,(550,450))
        
##        largeText = pygame.font.Font('freesansbold.ttf',115)
##        TextSurf, TextRect = black_text_objects("Race to Win!", largeText)
##        TextRect.center = ((display_width/2),(display_height/8))
##        gameDisplay.blit(TextSurf, TextRect)
##
        button2(150,450,150,50,game_loop)
        button2(550,450,150,50,quitgame)
        pygame.display.update()
        clock.tick(15)

def crash():
    score=0
    x_change=0;y_change=0
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = red_text_objects("You crashed!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(playAgainButton,(150,450))
        button2(150,450,100,50,game_loop)
        gameDisplay.blit(exitButton,(550,450))
        button2(550,450,100,50,quitgame)
        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    pygame.mixer.music.unpause()    

def paused():

    pygame.mixer.music.pause()
    
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = red_text_objects("Game Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.blit(continueButton,(150,450))
        button2(150,450,100,50,game_loop)
        gameDisplay.blit(exitButton,(550,450))
        button2(550,450,100,50,quitgame) 
##        button("Continue",150,450,100,50,green,bright_green,unpause)
##        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

def display_score():
    global score
    message_display2('Your score is %d' %score)

def game_loop():
    global score
    global pause
    keys = [False, False, False, False]
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45) #set car position on horizontal
    y = (display_height * 0.75) #set car position on vertical
    x_change = 0 #the delta for x
    y_change = 0 #the delta for y
    thing1_startx = random.choice((80,180,290,410,520,630)) #setup a random horizontal position for an obstacle
    thing2_startx = random.choice((80,180,290,410,520,630))
    thing1_starty = -600 #setup a vertical start position
    thing2_starty = -900
    thing_speed = 7 #set the obstacle speed
    thing_width = 62 #setup obstacle width
    thing_height = 128 #setup obstacle height
    gameExit = False #Set the crashed variable to False

    #The game loop which checks that the car is not crashed
    while not gameExit:
        #recover all the pygame default events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #check if user wants to quit, set crashed to True to break while loop
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keys[1] = True
                elif event.key == pygame.K_RIGHT:
                    keys[3] = True
                elif event.key == pygame.K_UP:
                    keys[0] = True
                elif event.key == pygame.K_DOWN:
                    keys[2] = True
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                elif event.key == pygame.K_w:
                    keys[0] = True
                elif event.key == pygame.K_a:
                    keys[1] = True
                elif event.key == pygame.K_s:
                    keys[2] = True
                elif event.key == pygame.K_d:
                    keys[3] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    keys[0] = False
                    y_change = 0
                elif event.key == pygame.K_a:
                    keys[1] = False
                    x_change = 0
                elif event.key == pygame.K_s:
                    keys[2] = False
                    y_change = 0
                elif event.key == pygame.K_d:
                    keys[3] = False
                    x_change = 0
                elif event.key == pygame.K_UP:
                    keys[0] = False
                    y_change = 0
                elif event.key == pygame.K_LEFT:
                    keys[1] = False
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    keys[2] = False
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    keys[3] = False
                    x_change = 0
                    
        if keys[1]:
            x_change = -7
        elif keys[3]:
            x_change = 7
        elif keys[0]:
            y_change = -7
        elif keys[2]:
            y_change = 7
##        if keys[1]:
##            playerpos[0] -= 5
##        elif keys[3]:
##            playerpos[0] += 5
                    
        x += x_change #update x
        y += y_change #update y
        gameDisplay.blit(backgroundImg,(0,0))
        #gameDisplay.fill(white) #add a white background
        yellowCar(thing1_startx, thing1_starty)
        greenCar(thing2_startx, thing2_starty)
        thing1_starty += thing_speed
        thing2_starty += thing_speed
        car(x,y) #draw the car
        
        if x > display_width - car_width-65 or x < 0+65:
            score = 0
            crash()
        if y > display_height - car_height or y < 0:
            score = 0
            crash()
            
        if thing1_starty > display_height:
            thing1_starty = 0 - thing_height
            thing1_startx = random.choice((80,180,290,410,520,630))
            score += 1
            thing_speed += 0.1
			
        if thing2_starty > display_height:
            thing2_starty = 0 - thing_height
            thing2_startx = random.choice((80,180,290,410,520,630))
            score += 1
            thing_speed += 0.05

        yellowCar(thing1_startx, thing1_starty)
        greenCar(thing2_startx, thing2_starty)
        
        if y < thing1_starty + thing_height:
            if x > thing1_startx and x < thing1_startx + thing_width \
            or x + car_width > thing1_startx and x + car_width < thing1_startx + thing_width:
                score = 0
                crash()
        
        if y < thing2_starty + thing_height:
            if x > thing2_startx and x < thing2_startx + thing_width \
            or x + car_width > thing2_startx and x + car_width < thing2_startx + thing_width:
                score = 0
                crash()
        display_score()		
        pygame.display.update() #update the display
        clock.tick(60) #set the number of fps

game_intro()
game_loop()
quitgame()
