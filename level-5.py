
import pickle

with open("level-5_banner.p", 'rb') as file:
    BigList = pickle.load(file)
    for SmallList in BigList:      
        for n in range(len(SmallList)):
            Tuple = SmallList[n]
            print(SmallList[n][0] * SmallList[n][1], end = '')
        print()
