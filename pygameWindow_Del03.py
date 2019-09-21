import pygame
from constants import *


class PYGAME_WINDOW_Del03:

    def __init__(self):
        pygame.init()
        pygame.display.init()
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

    def Draw_Line(self,xBase,yBase,xTip,yTip,b,color):
        xBase = self.ScaleX(xBase, -300, 300, 0, pygameWindowWidth)
        xTip = self.ScaleX(xTip, -300, 300, 0, pygameWindowWidth)
        yBase = self.ScaleY(yBase, -300, 300, 0, pygameWindowDepth)
        yTip = self.ScaleY(yTip, -300, 300, 0, pygameWindowDepth)
        # width = 4-b
        if color == 1:
            pygame.draw.line(self.screen, (0,128,0), [xBase,yBase], [xTip,yTip], 4-b)
        elif color == 2:
            pygame.draw.line(self.screen, (255,0,0), [xBase,yBase], [xTip,yTip], 4-b)
        else:
            pygame.draw.line(self.screen, (255,0,0), [xBase,yBase], [xTip,yTip], 4-b)


        # pygame.draw.line(self.screen, (0,0,0), [xBase,yBase], [xTip,yTip], 4-b)

        # print xBase,xTip,yBase,yTip

    def Draw_Black_Circle(self, x, y):
        x = self.ScaleX(x, -1000, 1000, 0, pygameWindowWidth)
        y = self.ScaleY(y, -1000, 1000, 0, pygameWindowDepth)
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
            return int(1/float(2)*(windowEnd - windowStart)-(value/float(leapMax - leapMin)*(windowEnd - windowStart)))
            # return int(((value + (leapMax-leapMin)/2) / float(leapMax - leapMin)) * (windowEnd - windowStart)-1/float(2)*(windowEnd - windowStart))

    def ScaleZ(self, value, leapMin, leapMax, windowStart, windowEnd):
        if(leapMax == leapMin):
            print "The maximum data collection range for the Leap Motion device along the z-axis is > 1000. You have chosen a range of 0. Division by 0 is not possible."
        else:
            return int((1-1.75*(value / float(leapMax - leapMin))) * (windowEnd - windowStart))
