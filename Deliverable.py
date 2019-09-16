import sys
sys.path.insert(0, '..')
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import numpy as np
import pickle


class DELIVERABLE:

    def __init__(self):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW()
        self.x = 0
        self.y = 0
        self.xMin = -300
        self.xMax = 300
        self.yMin = -300
        self.yMax = 300
        # self.numberOfHands = 0
        self.currentNumberOfHands = 0
        self.previousNumberOfHands = 0
        self.gestureData = np.zeros((5, 4, 6), dtype=float)
        self.numberOfFile = 0


    def Handle_Frame(self,frame):
        hand = frame.hands[0]
        # print hand
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)

        if self.Recording_Is_Ending():
            print self.gestureData
            self.Save_Gesture()

    def Handle_Finger(self,finger):
        for i in range(0, 5):
            for b in range(0, 4):
                self.Handle_Bone(b, finger, i)
        # self.numberOfFile += 1

    def Handle_Bone(self, b, finger, i):
        bone = finger.bone(b)
        base = bone.prev_joint
        tip = bone.next_joint

        [xBase, yBase] = self.Handle_Vector_From_Leap(base)
        [xTip, yTip] = self.Handle_Vector_From_Leap(tip)
        # self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b)

        green = 1
        red = 2
        if self.currentNumberOfHands == 1:
            self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, green)
        if self.currentNumberOfHands == 2:
            self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, b, red)
        if self.Recording_Is_Ending():
            self.gestureData[i, b, 0] = bone.prev_joint.x
            self.gestureData[i, b, 1] = bone.prev_joint.y
            self.gestureData[i, b, 2] = bone.prev_joint.z
            self.gestureData[i, b, 3] = bone.next_joint.x
            self.gestureData[i, b, 4] = bone.next_joint.y
            self.gestureData[i, b, 5] = bone.next_joint.z
            # print tip

    def Handle_Vector_From_Leap(self, v):
        self.x = int(v[0])
        self.y = int(v[2])

        if (self.x < self.xMin):
            self.xMin = self.x
        if (self.x > self.xMax):
            self.xMax = self.x
        if (self.y < self.yMin):
            self.yMin = self.y
        if (self.y > self.yMax):
            self.yMax = self.y
        return self.x, self.y

    def Recording_Is_Ending(self):
        if self.previousNumberOfHands > self.currentNumberOfHands:
            return True

    def Save_Gesture(self):
        # for i in self.numberOfFile:
            # file_list.append(FileData(path))
        self.numberOfFile += 1
        save_gesture = open("userData/gesture"+str(self.numberOfFile)+".p", "wb")
        pickle.dump(self.gestureData, save_gesture)
        save_gesture.close()
        # pass

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
            print "nothing"
        else:
            self.currentNumberOfHands = len(handlist)
            print "current is ", self.currentNumberOfHands
            self.Handle_Frame(frame)
            self.previousNumberOfHands = len(handlist)
            print "previous is ", self.previousNumberOfHands

        self.pygameWindow.Reveal()
    def Run_Forever(self):
        while True:
            self.Run_Once()
