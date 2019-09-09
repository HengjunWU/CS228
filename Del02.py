import sys
import Leap

from pygameWindow import PYGAME_WINDOW
import pygame
sys.path.insert(0, '..')

x = 0
y = 343

xMin = -300
xMax = 300
yMin = -300
yMax = 300

def Handle_Frame(frame):
    global xMin
    global xMax
    global yMin
    global yMax

    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)

def Handle_Finger(finger):
    for b in range(0,4):
        Handle_Bone(b,finger)


def Handle_Bone(b,finger):
    bone = finger.bone(b)
    base = bone.prev_joint
    tip = bone.next_joint

    [xBase,yBase] = Handle_Vector_From_Leap(base)
    [xTip,yTip] = Handle_Vector_From_Leap(tip)

    pygameWindow.Draw_Black_Line(xBase,yBase,xTip,yTip,b)

def Handle_Vector_From_Leap(v):
    global xMin
    global xMax
    global yMin
    global yMax

    x = int(v[0])
    y = int(v[2])
    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y
    return x, y


pygameWindow = PYGAME_WINDOW()



run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygameWindow.Prepare()

    controller = Leap.Controller()
    frame = controller.frame()

    handlist = frame.hands
    if not handlist:
        print "nothing"
    else:
        Handle_Frame(frame)

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

