import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from knn import KNN



knn = KNN()
knn.Load_Dataset('iris.csv')
x = knn.data[:,0]
y = knn.data[:,1]
# ::2 even rows
trainX = knn.data[::2,1:3]
trainy = knn.target[::2]


testX = knn.data[1::2,1:3]
testy = knn.target[1::2]

knn.Use_K_Of(15)
knn.Fit(trainX,trainy)
# for i in range(0,75):
#     actualClass = testy[i]
#     prediction = knn.Predict(testX[i,1:3])
    # print(actualClass, prediction)

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]
black_colors = np.zeros((3,3),dtype='f')
black_colors[0,:] = [0,0,0]
black_colors[1,:] = [0,0,0]
black_colors[2,:] = [0,0,0]
plt.figure()

[numItems,numFeatures] = knn.data.shape
for i in range(0,numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    black = black_colors[itemClass, :]
    backcolor = black
    facecolor = currColor
    # s is point size, lw is line width
    plt.scatter(trainX[i,0],trainX[i,1],c=backcolor,s=50)
    plt.scatter(trainX[i,0],trainX[i,1],c=facecolor,s=20)

counter = 0
for i in range(0,numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    facecolor = currColor
    #  prediction
    prediction = int(knn.Predict(testX[i, :]))
    edgeColor = colors[prediction, :]
    edgecolor = edgeColor
    if itemClass == prediction:
        counter +=1
    # s is point size, lw is line width
    plt.scatter(testX[i,0],testX[i,1],c=edgecolor,s=50)

    plt.scatter(testX[i,0],testX[i,1],c=facecolor,s=20)
print counter/float(numItems/2)*100

# plt.scatter(knn.data[::2,0],knn.data[::2,1],c=trainy)
# plt.scatter(knn.data[1::2,0],knn.data[1::2,1],c=trainy)
plt.show()