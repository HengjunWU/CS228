import sys
import Leap
import pickle
import numpy as np
from pygameWindow import PYGAME_WINDOW
import pygame

sys.path.insert(0, '../..')
clf = pickle.load( open('userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')

pygameWindow = PYGAME_WINDOW()

# x = 0
# y = 343

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
    k = 0
    for finger in fingers:
        for b in range(0,4):
            bone = finger.bone(b)
            base = bone.prev_joint
            tip = bone.next_joint

            [xBase,zBase,yBase] = Handle_Vector_From_Leap(base)
            [xTip,zTip,yTip] = Handle_Vector_From_Leap(tip)
            pygameWindow.Draw_Black_Line(xBase,yBase,xTip,yTip,b)
            if ((b == 0) or (b == 3)):
                testData[0, k] = xTip
                testData[0, k + 1] = yTip
                testData[0, k + 2] = zTip
                k = k +3
    # print(testData)
    testData_1 = CenterData(testData)
    predictedClass = clf.Predict(testData_1)
    print(predictedClass)

def CenterData(testData):
    mean_x = sum(testData[0, ::3])/10
    mean_y = sum(testData[0, 1::3])/10
    mean_z = sum(testData[0, 2::3])/10
    testData[0, ::3] = [x - mean_x for x in testData[0, ::3]]
    testData[0, 1::3] = [y - mean_y for y in testData[0, 1::3]]
    testData[0, 2::3] = [z - mean_z for z in testData[0, 2::3]]
    return testData


def Handle_Vector_From_Leap(v):
    global xMin
    global xMax
    global yMin
    global yMax

    x = int(v[0])
    y = int(v[1])
    z = int(v[2])
    if (x < xMin):
        x = xMin
    if (x > xMax):
        x = xMax
    if (y < yMin):
        y = yMin
    if (y > yMax):
        y = yMax
    return x, y, z





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
