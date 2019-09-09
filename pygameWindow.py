import pygame
from constants import *


class PYGAME_WINDOW:

    def __init__(self):
        pygame.init()
        self.width = pygameWindowWidth
        self.depth = pygameWindowDepth
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))
        self.debug = True

    def Prepare(self):
        # pygame.event.get()
        # pass
        self.screen.fill((255, 255, 255))
        # pygame.display.flip()

    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Line(self,xBase,yBase,xTip,yTip,b):
        xBase = self.ScaleX(xBase, -300, 300, 0, pygameWindowWidth)
        xTip = self.ScaleX(xTip, -300, 300, 0, pygameWindowWidth)
        yBase = self.ScaleY(yBase, -300, 300, 0, pygameWindowDepth)
        yTip = self.ScaleY(yTip, -300, 300, 0, pygameWindowDepth)
        # width = 4-b
        pygame.draw.line(self.screen, (0,0,0), [xBase,yBase], [xTip,yTip], 4-b)

    def Draw_Black_Circle(self, x, y):
        x = self.ScaleX(x, -1000, 1000, 0, pygameWindowWidth)
        y = self.ScaleZ(y, 0, 1200, 0, pygameWindowDepth)
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 45, 0)
        #print(x,y)
        #print(self.screen)
        #print(pygame)
        # pygame.display.update()

    # def Draw_Black_Dot(self, value, leapMin, leapMax, windowStart, windowEnd):
    #     return int((leapMax-(value + (leapMax-leapMin)/2)) / float(leapMax - leapMin)) * (windowEnd - windowStart)

    def ScaleX(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device is > 2000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            return (int(((value + (leapMax-leapMin)/2) / float(leapMax - leapMin)) * (windowEnd - windowStart)))

    def ScaleY(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device along the z-axis is > 1000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            return int(((value + (leapMax-leapMin)/2) / float(leapMax - leapMin)) * (windowEnd - windowStart))

    def ScaleZ(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device along the z-axis is > 1000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            return int((1-1.75*(value / float(leapMax - leapMin))) * (windowEnd - windowStart))

    # def getDebugStatus(self):
    #     return self.debug