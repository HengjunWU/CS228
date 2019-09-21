# import Del03b
import pickle
import os
from pygameWindow_Del03 import PYGAME_WINDOW_Del03
import pygame
from constants import *
import numpy as np
import time
from Deliverable import DELIVERABLE


class READER:
    def __init__(self):
        self.numGestures = 0
        self.gestureData = np.zeros((5, 4, 6), dtype = 'f')
        self.pygameWindow = PYGAME_WINDOW_Del03()
        self.screen = pygame.display.set_mode((pygameWindowWidth, pygameWindowDepth))
        self.x = 0
        self.y = 0
        self.xMin = -500
        self.xMax = 500
        self.yMin = -500
        self.yMax = 500
        self.debug = False

        # self.gestureData

    def NumberGestures(self):
        path, dirs, files = next(os.walk("userData"))
        self.numGestures = len(files)
        # print self.numGestures
    # def LoadData(self):
    #     for i in str(self.numGestures):
    #         file = open("userData/gesture"+str(self.numGestures)+".p", "rb")
    #         self.gestureData = pickle.load(file)
    #         # print gestureData

    # def Print_Gestures(self):
    #     for i in range(0, self.numGestures):
    #         file = open("userData/gesture{}.p".format(i), "rb")
    #         self.gestureData = pickle.load(file)
    #         print self.gestureData



    def Draw_Gesture(self,i):
        # for i in range(0, self.numGestures):
        file = open("userData/gesture{}.p".format(i), "rb")
        self.gestureData = pickle.load(file)
        print self.gestureData
        self.pygameWindow.Prepare()
        for i in range(0,5):
            for j in range(0, 4):
                # currentBone = self.gestureData[i, j, 3:6]
                xBaseNotYetScaled = self.gestureData[i,j,0]
                yBaseNotYetScaled = self.gestureData[i,j,1]
                xTipNotYetScaled  = self.gestureData[i,j,3]
                yTipNotYetScaled  = self.gestureData[i,j,4]

                xBase = self.pygameWindow.ScaleX(xBaseNotYetScaled, self.xMin, self.xMax, 0, pygameWindowWidth)
                yBase = self.pygameWindow.ScaleY(yBaseNotYetScaled, self.yMin, self.yMax, 0, pygameWindowWidth)
                xTip = self.pygameWindow.ScaleX(xTipNotYetScaled, self.xMin, self.xMax, 0, pygameWindowWidth)
                yTip = self.pygameWindow.ScaleY(yTipNotYetScaled, self.yMin, self.yMax, 0, pygameWindowWidth)

                if self.debug:
                    print xBaseNotYetScaled,yBaseNotYetScaled,xTipNotYetScaled,yTipNotYetScaled,xBase,yBase,xTip,yTip

                # color = 3
                pygame.draw.line(self.screen, [0,0,255], [xBase,yBase],[xTip,yTip], 1)
                # pygame.draw.line(self.screen, [0,255,0], [xBaseNotYetScaled,yBaseNotYetScaled],[xTipNotYetScaled,yTipNotYetScaled], 1)
        self.pygameWindow.Reveal()
        time.sleep(0.1)

                    # self.Draw_Line(self.xBaseNotYetScaled,self.yBaseNotYetScaled,self.xTipNotYetScaled,self.yTipNotYetScaled)
            # print self.gestureData
            # self.Draw_Gesture(i)


    def Draw_Each_Gesture_Once(self):
        self.NumberGestures()
        for i in range(0, self.numGestures):
            self.Draw_Gesture(i)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()