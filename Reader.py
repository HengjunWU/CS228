# import Del03b
import pickle



class READER:
    file = open("userData/gesture.p", "rb")
    gestureData = pickle.load(file)
    print gestureData
