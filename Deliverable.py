import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW_Del03
import numpy as np
import pickle
import os
import shutil
# import time



class DELIVERABLE:

    def __init__(self):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW_Del03()
        self.x = 0
        self.y = 0
        self.xMin = -300
        self.xMax = 300
        self.yMin = -300
        self.yMax = 300
        self.debug = False
        # self.numberOfHands = 0
        self.currentNumberOfHands = 0
        self.previousNumberOfHands = 0
        self.gestureData = np.zeros((5, 4, 6), dtype='f')
        self.numberOfFile = 0


    def Handle_Frame(self,frame):
        hand = frame.hands[0]
        # print hand
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)

        if self.Recording_Is_Ending():
            # print self.gestureData
            self.Save_Gesture()

    def Handle_Finger(self,finger):
        for b in range(0, 4):
            self.Handle_Bone(finger.type, b, finger)
        # self.numberOfFile += 1

    def Handle_Bone(self, i, b, finger):
        # time.sleep(1)
        bone = finger.bone(b)
        base = bone.prev_joint
        tip = bone.next_joint
        print base, tip

        [xBase, yBase] = self.Handle_Vector_From_Leap(base)
        [xTip, yTip] = self.Handle_Vector_From_Leap(tip)
        # self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b)
        # print base,tip
        green = 1
        red = 2
        if self.currentNumberOfHands == 1:
            self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, green)
        elif self.currentNumberOfHands == 2:
            self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, red)
        # print base[0], base[1], base[2],tip[0],tip[1],tip[2]
        if self.Recording_Is_Ending():
            self.gestureData[i, b, 0] = base[0]
            self.gestureData[i, b, 1] = base[1]
            self.gestureData[i, b, 2] = base[2]
            self.gestureData[i, b, 3] = tip[0]
            self.gestureData[i, b, 4] = tip[1]
            self.gestureData[i, b, 5] = tip[2]
            # print "i is ",i
            # print "b is ",b
            if self.debug:
                print "handle Bone is processing nested for loop to collect 120 hand coordinates"
                print self.gestureData[i, b, 0]
                print self.gestureData[i, b, 1]
                print self.gestureData[i, b, 2]
                print self.gestureData[i, b, 3]
                print self.gestureData[i, b, 4]
                print self.gestureData[i, b, 5]
            # print tip

    def Handle_Vector_From_Leap(self, v):
        self.x = int(v[0])
        self.y = int(v[1])

        if (self.x < self.xMin):
            self.x = self.xMin
        if (self.x > self.xMax):
            self.x = self.xMax
        if (self.y < self.yMin):
            self.y = self.yMin
        if (self.y > self.yMax):
            self.y = self.yMax
        return self.x, self.y

    def Recording_Is_Ending(self):
        if self.previousNumberOfHands > self.currentNumberOfHands:
            return True

    def Save_Gesture(self):
        # print self.gestureData
        if self.debug:
            print self.gestureData
        self.numberOfFile += 1
        save_gesture = open("userData/gesture"+str(self.numberOfFile-1)+".p", "wb")
        pickle.dump(self.gestureData, save_gesture)
        save_gesture.close()
        # pass

    def delete(self):
        shutil.rmtree("userData")
        os.mkdir("userData")

    def Run_Once(self):
        # run = True
        # while run:
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False
        self.pygameWindow.Prepare()

        # self.controller = Leap.Controller()
        frame = self.controller.frame()
        handlist = frame.hands

        if not handlist:
            if self.debug:
                print "nothing"
        else:
            self.currentNumberOfHands = len(handlist)
            if self.debug:
                print "current is ", self.currentNumberOfHands
            self.Handle_Frame(frame)
            self.previousNumberOfHands = len(handlist)
            if self.debug:
                print "previous is ", self.previousNumberOfHands

        self.pygameWindow.Reveal()
    def Run_Forever(self):
        while True:
            self.Run_Once()
