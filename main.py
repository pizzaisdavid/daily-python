import pygame
from pygame import gfxdraw

window = pygame.display.set_mode((640, 480))
color = pygame.Color(0, 255, 0)
for i in range(600):
    gfxdraw.pixel(window, i, i, color)
    pygame.display.update()

