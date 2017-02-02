import pygame

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(BLUE)

Pix = pygame.PixelArray(gameDisplay,) 

Pix[10][10] = GREEN

pygame.draw.line(gameDisplay, RED, (200,300),(500,500),5)
pygame.draw.circle(gameDisplay, RED, (200,200), 100)

pygame.draw.rect(gameDisplay, GREEN, (150,150,200,100))
pygame.draw.polygon(gameDisplay, WHITE,((140,5),(200,16),(88,333),(600,222),(555,222)))

def quitgame():
    pygame.quit()
    quit()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame()


    pygame.display.update()
