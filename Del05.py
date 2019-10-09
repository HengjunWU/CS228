# import sys
# sys.path.insert(0, '..')
#
# import Leap
# import pygame
# from pygameWindow import PYGAME_WINDOW
# import Deliverable
# deliverable = Deliverable.DELIVERABLE()


from Recorder import RECORDER


deliverable = RECORDER()
deliverable.delete()
deliverable.Run_Forever()


#
# def Run_Forever():
#     pygameWindow = PYGAME_WINDOW()
#     run = True
#     while run:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#         pygameWindow.Prepare()
#
#         controller = Leap.Controller()
#         frame = controller.frame()
#
#         handlist = frame.hands
#         if not handlist:
#             print "nothing"
#         else:
#             deliverable.Handle_Frame(frame)
#
#         pygameWindow.Reveal()
#
# Run_Forever()







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

