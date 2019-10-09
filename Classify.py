import numpy as np
import pickle
import os
from knn import KNN



knn = KNN()
knn.Use_K_Of(15)

path, dirs, files = next(os.walk("userData"))
# numGestures = len(files)

# for i in range(numGestures):
# file = open("userData/gesture{}.p".format(i), "rb")
test5 = open("userData/test5.p", "rb")
test6 = open("userData/test6.p", "rb")
train5 = open("userData/train5.dat", "rb")
train6 = open("userData/train6.dat", "rb")


test5_load = pickle.load(test5)
test6_load = pickle.load(test6)
train5_load = pickle.load(train5)
train6_load = pickle.load(train6)

def ReduceData(X):
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 1)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)

    return X

train5_reduced = ReduceData(train5_load)
train6_reduced = ReduceData(train6_load)
test5_reduced = ReduceData(test5_load)
test6_reduced = ReduceData(test6_load)

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

train5 = CenterData(train5_reduced)
train6 = CenterData(train6_reduced)
test5 = CenterData(test5_reduced)
test6 = CenterData(test6_reduced)

def ReshapeData(set1,set2):
    X = np.zeros((2000,5*2*3),dtype='f')
    y = np.zeros(2000,dtype='f')
    for row in range(0,1000):
        y[row] = 5
        y[row+1000] = 6
        col = 0
        for finger in range(0,5):
            for bone in range(0,2):
                for tipAndBase in range(0,3):
                    X[row,col] = set1[finger,bone,tipAndBase,row]
                    X[row+1000,col] = set2[finger,bone,tipAndBase,row]
                    col = col + 1
    return X,y
trainX,trainy= ReshapeData(train5,train6)
testX,testy= ReshapeData(test5,test6)


knn.Fit(trainX,trainy)
# for row in range(0,2000):
counter = 0
for row in range(0, 2000):
    itemClass = int(testy[row])
    #  prediction
    prediction = int(knn.Predict(testX[row]))
    if itemClass == prediction:
        counter += 1
        # print counter
print counter
print counter/float(2000)*100

