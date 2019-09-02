import constants
import sys
import Leap
from Leap import Finger
from Leap import Bone
from pygameWindow import PYGAME_WINDOW
import random
import pygame
sys.path.insert(0, '..')

x = 0
y = 343

xMin = -800
xMax = 800
yMin = 0
yMax = 1200




def Perturb_Circle_Position(x, y):
    foursidedDieRoll = random.randint(1,4)
    if foursidedDieRoll == 1:
        x -= constants.circleVelocity
    elif foursidedDieRoll == 2:
        x += constants.circleVelocity
    elif foursidedDieRoll == 3:
        y -= constants.circleVelocity
    else:
        y += constants.circleVelocity
    return [x, y]

def Handle_Frame(frame):
    global xMin
    global xMax
    global yMin
    global yMax
    # xMin = 1000.0
    # xMax = -1000.0
    # yMin = 1000.0
    # yMax = -1000.0

    #print(frame)
    hand = frame.hands[0]
    #print(hand)
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(Finger.TYPE_INDEX)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(Bone.TYPE_DISTAL)
    #print(distalPhalanx)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y
    return [x, y]


pygameWindow = PYGAME_WINDOW()
print(pygameWindow)
#debug = True

    # global debug
    # if not(frame.is_valid):
    #     debug = True
    # if(debug):
    #     print(frame)


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygameWindow.Prepare()
    controller = Leap.Controller()
    frame = controller.frame()
    handlist = frame.hands
    for hand in handlist:
        # print str(hand)
        [x, y] = Handle_Frame(frame)

    pygameWindow.Draw_Black_Circle(x, y)
    [x, y] = Perturb_Circle_Position(x, y)
        # print(x,y)
    pygameWindow.Reveal()

    # if(handlist.is_empty):
    #     debug = True
    #     if(debug):
    #         print("handList is empty. You can not modify the handList object.")
    # else:






    # hand = frame.hands[0]
    # fingers = hand.fingers
    # indexFingerList = fingers.finger_type(Finger.TYPE_INDEX)
    # indexFinger = indexFingerList[0]
    #






        # indexFingerList = list[0]
        # for hand in handlist:
        #     #if(debug):
        #         #print(hand)
        #         #print(len(handlist))
        #     fingers = hand.fingers
        #     for f in fingers:
        #         if(f.type == Finger.TYPE_INDEX):
        #             indexFingerList.append(f)
        #             #if(debug):
        #                 #print(f)
        #     distalPhalanx = indexFingerList.bone(Bone.TYPE_DISTAL)
        #     print(distalPhalanx)
        # # if (debug):
        # #     for f in indexFingerList:
        # #         print(f.type)
        # return indexFingerList



#

