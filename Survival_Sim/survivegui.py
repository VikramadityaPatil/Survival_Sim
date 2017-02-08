 # 1 - Import library
import pygame
from pygame.locals import *
import math
import random
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
pygame.mixer.init()

#3 - Loading Images
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
#4- Loading Audio

# Set the width and height of the window
width, height = int(pygame.display.Info().current_w), int(pygame.display.Info().current_h)
# Create the window
screen = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)
def main():
    hydrationval=100
    energyval=100
    staminaval=100
    heatval=100
    rescue=0
    running=1
    exitcode=0
    i=1
    

    while running:
        screen.fill(0)
        pygame.display.set_caption("Survive")
        screen.blit(healthbar, (5,5))
        for health1 in range(energyval):
            screen.blit(health, (health1+8,8))
        for health1 in range(staminaval):
            screen.blit(health, (health1+8,8))
        for health1 in range(hydrationval):
            screen.blit(health, (health1+8,8))
        for health1 in range(heatval):
            screen.blit(health, (health1+8,8))

main()
