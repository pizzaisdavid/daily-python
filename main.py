import pygame
import random
from pygame import gfxdraw

def generate_random_color():
    color = []
    for i in range(3):
        color.append(random.randrange(0, 255))
    return color

def generate_colors(number):
    colors = []
    while len(colors) < number:
        random_color = generate_random_color()
        if random_color not in colors:
            colors.append(random_color)
    return colors

window = pygame.display.set_mode((640, 480))
number_of_colors = 30
colors = generate_colors(number_of_colors)
# pygame.Color(0, 255, 0)
print colors
