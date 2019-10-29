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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        self.screen.fill((255, 255, 255))
        # pygame.display.flip()

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Line(self,xBase,yBase,xTip,yTip,b):
        xBase = self.ScaleX(xBase, -200, 200, 0, pygameWindowWidth)
        xTip = self.ScaleX(xTip, -200, 200, 0, pygameWindowWidth)
        yBase = self.ScaleY(yBase, -200, 200, 0, pygameWindowDepth)
        yTip = self.ScaleY(yTip, -200, 200, 0, pygameWindowDepth)
        # yBase = self.ScaleY(yBase, -200, 200, 0, pygameWindowDepth)
        # yTip = self.ScaleY(yTip, -200, 200, 0, pygameWindowDepth)
        pygame.draw.line(self.screen, (0,0,0), [xBase,yBase], [xTip,yTip], 4-b)
        # print(xBase,xTip,yBase,yTip)
        # print xBase,xTip,yBase,yTip

    def Draw_Black_Circle(self, x, y):
        x = self.ScaleX(x, -600, 600, 0, pygameWindowWidth)
        y = self.ScaleZ(y, 0, 1200, 0, pygameWindowDepth)
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 45, 0)

    def ScaleX(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device is > 2000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            # return (int(((value + (leapMax-leapMin)/4) / float(leapMax - leapMin)) * (windowEnd - windowStart)))
            return int(value + (windowEnd - windowStart)/4)


    def ScaleY(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device along the z-axis is > 1000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            # return int(1/float(2)*(windowEnd - windowStart)-(value/float(leapMax - leapMin)*(windowEnd - windowStart)))
            return int(value+(windowEnd - windowStart)/4)


    def ScaleZ(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device along the z-axis is > 1000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            return int(value+200)