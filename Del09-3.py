import sys
import Leap
import pickle
import numpy as np
from pygameWindow import PYGAME_WINDOW
import pygame
import time
import os
import random
import datetime
import Dict

sys.path.insert(0, '../..')
clf = pickle.load( open('Del6/userData/classifier.p','rb') )
testData = np.zeros((1,30),dtype='f')

pygameWindow = PYGAME_WINDOW()
clock = pygame.time.Clock()

# x = 0
# y = 343

xMin = -200
xMax = 200
yMin = -200
yMax = 200
programState = 0
xBase = 0
yBase = 0
xTip = 0
yTip = 0

t = 0
q = 0
m = 0
k = 0
e = 0

w = 0.15
# num = random.randint(0, 9)
num = 0
corrected = 0
h = 27
improved = 0
switch = True
switch2 = False
switch3 = False
opened = True

start = datetime.datetime.now()
display1 = None
display2 = None


def Handle_Frame(frame):
    global xMin
    global xMax
    global yMin
    global yMax
    global xBase
    global yBase
    global xTip
    global yTip

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
                testData[0, k + 1] = zTip
                testData[0, k + 2] = yTip
                k = k +3
    # print(testData)
    # testData_1 = CenterData(testData)
    # predictedClass = clf.Predict(testData_1)
    # print(predictedClass)

def CenterData(testData):
    mean_x = sum(testData[0, ::3])/10
    mean_z = sum(testData[0, 1::3])/10
    mean_y = sum(testData[0, 2::3])/10
    testData[0, ::3] = [x - mean_x for x in testData[0, ::3]]
    testData[0, 1::3] = [z - mean_z for z in testData[0, 1::3]]
    testData[0, 2::3] = [y - mean_y for y in testData[0, 2::3]]
    return testData


def Handle_Vector_From_Leap(v):
    global xMin
    global xMax
    global yMin
    global yMax

    x = int(v[0])
    z = int(v[1])
    y = int(v[2])
    if (x < xMin):
        x = xMin
    if (x > xMax):
        x = xMax
    if (y < yMin):
        y = yMin
    if (y > yMax):
        y = yMax
    return x, z, y
def DrawImageToHelpUserPutTheirHandOverTheDevice():
    graph = pygame.image.load('images/hands.jpeg')
    graph = pygame.transform.scale(graph,(400,400))
    pygameWindow.screen.blit(graph, (400, 0))

def HandleState0(handlist):
    global programState

    DrawImageToHelpUserPutTheirHandOverTheDevice()
    if handlist:
        programState=1

def HandleState1(handlist):
    global programState
    global xBase
    global yBase
    global xTip
    global yTip
    global t
    global start
    global display1
    global m
    global k
    global corrected

    # m = 0
    # t = 0
    k = 0
    corrected = 0

    xBase_1 = pygameWindow.ScaleX(xBase, -200, 200, 0, 800)
    yBase_1 = pygameWindow.ScaleY(yBase, -200, 200, 0, 800)
    xTip_1 = pygameWindow.ScaleX(xTip, -200, 200, 0, 800)
    yTip_1 = pygameWindow.ScaleY(yTip, -200, 200, 0, 800)

    # print(xBase_1, yBase_1, xTip_1, yTip_1)

    if switch:
        Handle_Frame(frame)

    if yTip_1<150 and yBase_1<150:
        # print("high is ",xBase_1,yBase_1,xTip_1,yTip_1)
        graph = pygame.image.load('images/down.jpeg')
        graph = pygame.transform.scale(graph, (400, 400))
        pygameWindow.screen.blit(graph, (400, 0))
        t = 0
        m = 0
    elif xTip_1<150 and xBase_1<150:
        # print("left is ",xBase_1,yBase_1,xTip_1,yTip_1)
        graph = pygame.image.load('images/right.png')
        graph = pygame.transform.scale(graph, (400, 400))
        pygameWindow.screen.blit(graph, (400, 0))
        t = 0
        m = 0
    clock.tick()
    if (150<=xBase_1 and 150<=yBase_1) and (150<=xTip_1 and 150<=yTip_1):
        # print("center is ",xBase_1,yBase_1,xTip_1,yTip_1)
        graph = pygame.image.load('images/check.png')
        graph = pygame.transform.scale(graph, (400, 400))
        pygameWindow.screen.blit(graph, (400, 0))
        clock.tick()
        t+=clock.get_time()/1000.0
        print("t :", t)
        if t > 0.02:
            display1 = True
            # print("start is ", start)

            if display1:
                clock.tick()
                graph = pygame.image.load('images/Thumb.jpeg')
                graph = pygame.transform.scale(graph, (400, 400))
                pygameWindow.screen.blit(graph, (400, 0))
                clock.tick()
                m += clock.get_time() / 1000.0
                print("m :", m)
                # print("123")
                # print(datetime.datetime.now()-start).total_seconds()
                if m > 0.02:
                    # print("end is ",datetime.datetime.now())
                    display1 = False
                    programState = 2

    if not handlist:
        programState=0

def HandleState2(handlist):
    global programState
    global xBase
    global yBase
    global xTip
    global yTip
    global num
    global corrected
    global t
    global switch
    global switch2
    global switch3
    global opened
    global h
    global q
    global w
    global m
    global k
    global e

    m = 0
    t = 0
    k = 0
    xBase_1 = pygameWindow.ScaleX(xBase, -200, 200, 0, 800)
    yBase_1 = pygameWindow.ScaleY(yBase, -200, 200, 0, 800)
    xTip_1 = pygameWindow.ScaleX(xTip, -200, 200, 0, 800)
    yTip_1 = pygameWindow.ScaleY(yTip, -200, 200, 0, 800)

    if switch:
        Handle_Frame(frame)
    if (200<=xBase_1 and 0<=yBase_1) and (200<=xTip_1 and 0<=yTip_1):
        clock.tick()
        graph = pygame.image.load('images/number{}.jpg'.format(num))
        graph = pygame.transform.scale(graph, (400, 400))
        pygameWindow.screen.blit(graph, (400, 0))
        graph = pygame.image.load('images/gesture{}.jpg'.format(num))
        graph = pygame.transform.scale(graph, (400, 400))
        pygameWindow.screen.blit(graph, (400, 400))
        clock.tick()
        q += clock.get_time() / 1000.0
        print("q :", q)

        testData_1 = CenterData(testData)
        predictedClass = clf.Predict(testData_1)
        print(predictedClass)
        if predictedClass == num:
            corrected+=1
            if q > w:
                print("corrected:", corrected)
                # w -= 0.03
                if corrected>=20:
                    programState = 3
                    w -= 0.01
                    switch2 = True
                else:
                    programState = 3
                    switch3 = True

    elif not handlist:
        programState = 0
    elif not (200<=xBase_1 and 0<=yBase_1 and 200<=xTip_1 and 0<=yTip_1):
        programState = 1
        # HandleState1(handlist)

def HandleState3(handlist):
    global programState
    global num
    global corrected
    global start
    global t
    global display2
    global k
    global improved
    global opened
    global q
    global switch2
    global switch3
    global e

    q = 0
    e = 0
    # corrected = 0
    if switch:
        Handle_Frame(frame)

    display2 = True
    # print("start is ", start)

    if display2:

        clock.tick()

        if switch2:
            graph = pygame.image.load('images/good.jpeg'.format(num))
            graph = pygame.transform.scale(graph, (400, 400))
            pygameWindow.screen.blit(graph, (400, 0))
            text1 = ""
            text2 = ""
            text1 += ('Digit {}').format(num) + " attempted " + str(corrected) + ' times'
            text2 += 'It\'s more than or equal to 20 times. '
            # # myfont = pygame.font.SysFont('Comic Sans MS', 20)
            myfont = pygame.font.SysFont('comicsansms', 40)
            t1 = myfont.render(text1, False, (0, 0, 0))
            t2 = myfont.render(text2, False, (0, 0, 0))
            pygameWindow.screen.blit(t1, (0, 400))
            pygameWindow.screen.blit(t2, (0, 500))

        if switch3:
            graph = pygame.image.load('images/almost.jpeg'.format(num))
            graph = pygame.transform.scale(graph, (400, 400))
            pygameWindow.screen.blit(graph, (400, 0))
            text1 = ""
            text2 = ""
            text1 += ('Digit {}').format(num) + " attempted " + str(corrected) + ' times'
            text2 += 'It\'s less than 20 times. '
        # # myfont = pygame.font.SysFont('Comic Sans MS', 20)
            myfont = pygame.font.SysFont('comicsansms', 40)
            t1 = myfont.render(text1, False, (0, 0, 0))
            t2 = myfont.render(text2, False, (0, 0, 0))
            pygameWindow.screen.blit(t1, (0, 400))
            pygameWindow.screen.blit(t2, (0, 500))

        clock.tick()

        k += clock.get_time() / 1000.0
        print("k :",k)
        if k > 0.05:
            # num = random.randint(0, 9)
            # print("number is ",num)
            display2 = False
            switch2 = False
            switch3 = False
            corrected = 0
            if handlist:
                programState = 2
            elif not handlist:
                t = 0
                programState = 0


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygameWindow.Prepare()

    controller = Leap.Controller()
    frame = controller.frame()

    handlist = frame.hands

    if programState == 0:
        HandleState0(handlist)
        # print(programState)
    elif programState == 1:
        HandleState1(handlist)
        # print(programState)
    elif programState == 2:
        HandleState2(handlist)
        # print(programState)
    elif programState == 3:
        HandleState3(handlist)
        # print(programState)
    pygameWindow.Reveal()
