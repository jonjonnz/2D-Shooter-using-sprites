import pygame #import pygame module
import random # import random module

#Predefined Values
width = 360
height = 480
FPS = 30
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Initialize pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size=(height, width))
pygame.display.set_caption("Shoot Em Up")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


#Main game loop
running = True
while running:
    #inputs/events
    for event in pygame.event.get():
        #checking for closing the game
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    
    #draw/render
    screen.fill(black)
    all_sprites.draw(screen)
    
    # after drawing everyting flip the display
    pygame.display.flip()
    
pygame.quit()
