import numpy as np
import pickle
import os
from knn import KNN
import sys
sys.path.insert(0, '../..')



knn = KNN()
knn.Use_K_Of(15)

path, dirs, files = next(os.walk("userData"))
# numGestures = len(files)

# for i in range(numGestures):
# file = open("userData/gesture{}.p".format(i), "rb")
test0_1 = open("userData/Clark_test0.p", "rb")
test0_2 = open("userData/Soccorsi_test0.p", "rb")
test0_3 = open("userData/Childs_test0.p", "rb")
test1 = open("userData/Clark_test1.p", "rb")
test2_1 = open("userData/Newton_test2.p", "rb")
test2_2 = open("userData/Gordon_test2.p", "rb")
test2_3 = open("userData/Thissell_test2.p", "rb")
test3 = open("userData/Ward_test3.p", "rb")
test4 = open("userData/Ward_test4.p", "rb")
test5 = open("userData/test5.p", "rb")
test6 = open("userData/test6.p", "rb")
test7_1 = open("userData/Mardis_test7.p", "rb")
test7_2 = open("userData/Zhang_test7.p", "rb")
test7_3 = open("userData/Rubin_test7.p", "rb")
test8_1 = open("userData/Zonay_test8.p", "rb")
test8_2 = open("userData/Zhang_test8.p", "rb")
test8_3 = open("userData/Mardis_test8.p", "rb")
test9_1 = open("userData/Zonay_test9.p", "rb")
test9_2 = open("userData/Childs_test9.p", "rb")
test9_3 = open("userData/Soccorsi_test9.p", "rb")


train0_1 = open("userData/Clark_train0.p", "rb")
train0_2 = open("userData/Soccorsi_test0.p", "rb")
train0_3 = open("userData/Childs_test0.p", "rb")
train1 = open("userData/Clark_train1.p", "rb")
train2_1 = open("userData/Newton_train2.p", "rb")
train2_2 = open("userData/Gordon_train2.p", "rb")
train2_3 = open("userData/Thissell_train2.p", "rb")
train3 = open("userData/Ward_train3.p", "rb")
train4 = open("userData/Ward_train4.p", "rb")
train5 = open("userData/train5.dat", "rb")
train6 = open("userData/train6.dat", "rb")
train7_1 = open("userData/Mardis_train7.p", "rb")
train7_2 = open("userData/Zhang_train7.p", "rb")
train7_3 = open("userData/Rubin_train7.p", "rb")
train8_1 = open("userData/Zonay_train8.p", "rb")
train8_2 = open("userData/Zhang_train8.p", "rb")
train8_3 = open("userData/Mardis_train8.p", "rb")
train9_1 = open("userData/Zonay_train9.p", "rb")
train9_2 = open("userData/Childs_train9.p", "rb")
train9_3 = open("userData/Soccorsi_train9.p", "rb")


test0_load_1 = pickle.load(test0_1)
test0_load_2 = pickle.load(test0_2)
test0_load_3 = pickle.load(test0_3)
test1_load = pickle.load(test1)
test2_load_1 = pickle.load(test2_1)
test2_load_2 = pickle.load(test2_2)
test2_load_3 = pickle.load(test2_3)
test3_load = pickle.load(test3)
test4_load = pickle.load(test4)
test5_load = pickle.load(test5)
test6_load = pickle.load(test6)
test7_load_1 = pickle.load(test7_1)
test7_load_2 = pickle.load(test7_2)
test7_load_3 = pickle.load(test7_3)
test8_load_1 = pickle.load(test8_1)
test8_load_2 = pickle.load(test8_2)
test8_load_3 = pickle.load(test8_3)
test9_load_1 = pickle.load(test9_1)
test9_load_2 = pickle.load(test9_2)
test9_load_3 = pickle.load(test9_3)
train0_load_1 = pickle.load(train0_1)
train0_load_2 = pickle.load(train0_2)
train0_load_3 = pickle.load(train0_3)
train1_load = pickle.load(train1)
train2_load_1 = pickle.load(train2_1)
train2_load_2 = pickle.load(train2_2)
train2_load_3 = pickle.load(train2_3)
train3_load = pickle.load(train3)
train4_load = pickle.load(train4)
train5_load = pickle.load(train5)
train6_load = pickle.load(train6)
train7_load_1 = pickle.load(train7_1)
train7_load_2 = pickle.load(train7_2)
train7_load_3 = pickle.load(train7_3)
train8_load_1 = pickle.load(train8_1)
train8_load_2 = pickle.load(train8_2)
train8_load_3 = pickle.load(train8_3)
train9_load_1 = pickle.load(train9_1)
train9_load_2 = pickle.load(train9_2)
train9_load_3 = pickle.load(train9_3)


def ReduceData(X):
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 1)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)

    return X
train0_reduced_1 = ReduceData(train0_load_1)
train0_reduced_2 = ReduceData(train0_load_2)
train0_reduced_3 = ReduceData(train0_load_3)
train1_reduced = ReduceData(train1_load)
train2_reduced_1 = ReduceData(train2_load_1)
train2_reduced_2 = ReduceData(train2_load_2)
train2_reduced_3 = ReduceData(train2_load_3)
train3_reduced = ReduceData(train3_load)
train4_reduced = ReduceData(train4_load)
train5_reduced = ReduceData(train5_load)
train6_reduced = ReduceData(train6_load)
train7_reduced_1 = ReduceData(train7_load_1)
train7_reduced_2 = ReduceData(train7_load_2)
train7_reduced_3 = ReduceData(train7_load_3)
train8_reduced_1 = ReduceData(train8_load_1)
train8_reduced_2 = ReduceData(train8_load_2)
train8_reduced_3 = ReduceData(train8_load_3)
train9_reduced_1 = ReduceData(train9_load_1)
train9_reduced_2 = ReduceData(train9_load_2)
train9_reduced_3 = ReduceData(train9_load_3)
test0_reduced_1 = ReduceData(test0_load_1)
test0_reduced_2 = ReduceData(test0_load_2)
test0_reduced_3 = ReduceData(test0_load_3)
test1_reduced = ReduceData(test1_load)
test2_reduced_1 = ReduceData(test2_load_1)
test2_reduced_2 = ReduceData(test2_load_2)
test2_reduced_3 = ReduceData(test2_load_3)
test3_reduced = ReduceData(test3_load)
test4_reduced = ReduceData(test4_load)
test5_reduced = ReduceData(test5_load)
test6_reduced = ReduceData(test6_load)
test7_reduced_1 = ReduceData(test7_load_1)
test7_reduced_2 = ReduceData(test7_load_2)
test7_reduced_3 = ReduceData(test7_load_3)
test8_reduced_1 = ReduceData(test8_load_1)
test8_reduced_2 = ReduceData(test8_load_2)
test8_reduced_3 = ReduceData(test8_load_3)
test9_reduced_1 = ReduceData(test9_load_1)
test9_reduced_2 = ReduceData(test9_load_2)
test9_reduced_3 = ReduceData(test9_load_3)



def CenterData(X):
    allXCoordinates = X[:, :, 0, :]
    meanValueX = allXCoordinates.mean()
    X[:, :, 0, :] = allXCoordinates - meanValueX
    allYCoordinates = X[:, :, 1, :]
    meanValueY = allYCoordinates.mean()
    X[:, :, 1, :] = allYCoordinates - meanValueY
    allZCoordinates = X[:, :, 2, :]
    meanValueZ = allZCoordinates.mean()
    X[:, :, 2, :] = allZCoordinates - meanValueZ
    print X[:, :, 0, :].mean()
    print X[:, :, 1, :].mean()
    print X[:, :, 2, :].mean()

    # exit()
    return X
train0_1 = CenterData(train0_reduced_1)
train0_2 = CenterData(train0_reduced_2)
train0_3 = CenterData(train0_reduced_3)
train1 = CenterData(train1_reduced)
train2_1 = CenterData(train2_reduced_1)
train2_2 = CenterData(train2_reduced_2)
train2_3 = CenterData(train2_reduced_3)
train3 = CenterData(train3_reduced)
train4 = CenterData(train4_reduced)
train5 = CenterData(train5_reduced)
train6 = CenterData(train6_reduced)
train7_1 = CenterData(train7_reduced_1)
train7_2 = CenterData(train7_reduced_2)
train7_3 = CenterData(train7_reduced_3)
train8_1 = CenterData(train8_reduced_1)
train8_2 = CenterData(train8_reduced_2)
train8_3 = CenterData(train8_reduced_3)
train9_1 = CenterData(train9_reduced_1)
train9_2 = CenterData(train9_reduced_2)
train9_3 = CenterData(train9_reduced_3)

test0_1 = CenterData(test0_reduced_1)
test0_2 = CenterData(test0_reduced_2)
test0_3 = CenterData(test0_reduced_3)
test1 = CenterData(test1_reduced)
test2_1 = CenterData(test2_reduced_1)
test2_2 = CenterData(test2_reduced_2)
test2_3 = CenterData(test2_reduced_3)
test3 = CenterData(test3_reduced)
test4 = CenterData(test4_reduced)
test5 = CenterData(test5_reduced)
test6 = CenterData(test6_reduced)
test7_1 = CenterData(test7_reduced_1)
test7_2 = CenterData(test7_reduced_2)
test7_3 = CenterData(test7_reduced_3)
test8_1 = CenterData(test8_reduced_1)
test8_2 = CenterData(test8_reduced_2)
test8_3 = CenterData(test8_reduced_3)
test9_1 = CenterData(test9_reduced_1)
test9_2 = CenterData(test9_reduced_2)
test9_3 = CenterData(test9_reduced_3)



def ReshapeData(set0,set1,set2,set3,set4,set5,set6,set7_1,set8_1,set9_1,set7_2,set7_3,set8_2,set8_3,set9_2,set9_3,set0_2,set0_3,set2_2,set2_3):
    X = np.zeros((20000,5*2*3),dtype='f')
    y = np.zeros(20000,dtype='f')
    for row in range(0,1000):
        y[row] = 0
        y[row+1000] = 1
        y[row+2000] = 2
        y[row+3000] = 3
        y[row+4000] = 4
        y[row+5000] = 5
        y[row+6000] = 6
        y[row+7000] = 7
        y[row+8000] = 8
        y[row+9000] = 9
        y[row+10000] = 7
        y[row+11000] = 7
        y[row+12000] = 8
        y[row+13000] = 8
        y[row+14000] = 9
        y[row+15000] = 9
        y[row+16000] = 0
        y[row+17000] = 0
        y[row+18000] = 2
        y[row+19000] = 2


        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for tipAndBase in range(0,3):
                    X[row,col] = set0[finger,bone,tipAndBase,row]
                    X[row+1000,col] = set1[finger,bone,tipAndBase,row]
                    X[row+2000,col] = set2[finger,bone,tipAndBase,row]
                    X[row+3000,col] = set3[finger,bone,tipAndBase,row]
                    X[row+4000,col] = set4[finger,bone,tipAndBase,row]
                    X[row+5000,col] = set5[finger,bone,tipAndBase,row]
                    X[row+6000,col] = set6[finger,bone,tipAndBase,row]
                    X[row+7000,col] = set7_1[finger,bone,tipAndBase,row]
                    X[row+8000,col] = set8_1[finger,bone,tipAndBase,row]
                    X[row+9000,col] = set9_1[finger,bone,tipAndBase,row]
                    X[row+10000,col] = set7_2[finger,bone,tipAndBase,row]
                    X[row+11000,col] = set7_3[finger,bone,tipAndBase,row]
                    X[row+12000,col] = set8_2[finger,bone,tipAndBase,row]
                    X[row+13000,col] = set8_3[finger,bone,tipAndBase,row]
                    X[row+14000,col] = set9_2[finger,bone,tipAndBase,row]
                    X[row+15000,col] = set9_3[finger,bone,tipAndBase,row]
                    X[row+16000,col] = set0_2[finger,bone,tipAndBase,row]
                    X[row+17000,col] = set0_3[finger,bone,tipAndBase,row]
                    X[row+18000,col] = set2_2[finger,bone,tipAndBase,row]
                    X[row+19000,col] = set2_3[finger,bone,tipAndBase,row]

                    col = col + 1
    return X,y
trainX,trainy= ReshapeData(train0_1,train1,train2_1,train3,train4,train5,train6,train7_1,train8_1,train9_1,train7_2,train7_3,train8_2,train8_3,train9_2,train9_3,train0_2,train0_3,train2_2,train2_3)
testX,testy= ReshapeData(test0_1,test1,test2_1,test3,test4,test5,test6,test7_1,test8_1,test9_1,test7_2,test7_3,test8_2,test8_3,test9_2,test9_3,test0_2,test0_3,test2_2,test2_3)


knn.Fit(trainX,trainy)
# for row in range(0,2000):
counter = 0
for row in range(0, 20000):
    itemClass = int(testy[row])
    #  prediction
    prediction = int(knn.Predict(testX[row]))
    if itemClass == prediction:
        counter += 1
        # print counter
print counter
print counter/float(20000)*100

pickle.dump(knn, open('userData/classifier.p','wb'))

