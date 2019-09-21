from pygameWindow import PYGAME_WINDOW
import random
import pygame
from constants import *

x = 750
y = 750

def Perturb_Circle_Position():
    global x, y
    foursidedDieRoll = random.randint(1,4)
    if foursidedDieRoll == 1:
        x -= circleVelocity
    elif foursidedDieRoll == 2:
        x += circleVelocity
    elif foursidedDieRoll == 3:
        y -= circleVelocity
    else:
        y += circleVelocity

pygameWindow = PYGAME_WINDOW()

print(pygameWindow)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygameWindow.Prepare()
    pygameWindow.Draw_Black_Circle(x,y)
    Perturb_Circle_Position()
    print(x,y)
    pygameWindow.Reveal()