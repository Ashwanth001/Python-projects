import pygame

#Initializeing the pygame
pygame.init()
#creating the screen
screen = pygame.display.set_mode((800, 600))
#createing the screen
running = True
#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
#Game Loop
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
