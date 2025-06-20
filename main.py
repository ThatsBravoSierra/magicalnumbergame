# Robert's Magical Number Game 2

import pygame
from pygame.locals import *
import random

pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600	
DISPLAYSURF = pygame.display.set_mode((400,600))

FramePerSec = pygame.time.Clock()

#Game Loop
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    
    
    pygame.display.update()
