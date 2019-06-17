import random
import time

dataResult = []


def getData():
    return dataResult[-1]


while 1:
    data = random.randint(0,10)
    dataResult.append(data)
    print("Generated: {}".format(data))
    time.sleep(1)

