import pygame
from constants import *


class PYGAME_WINDOW:

    def __init__(self):
        pygame.init()
        self.width = pygameWindowWidth
        self.depth = pygameWindowDepth
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))

    def Prepare(self):
        # pygame.event.get()
        # pass
        self.screen.fill((255, 255, 255))
        # pygame.display.flip()

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 45, 0)
        print(x,y)
        print(self.screen)
        #print(pygame)
        # pygame.display.update()
