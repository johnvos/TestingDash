import random
import time

f = open("testing_communication.txt", "w")
index = 0
f.close()
while 1:
    f = open("testing_communication.txt", "a")
    number = random.randint(0,10)
    f.write("{},{}\n".format(index, number))
    print(index,number)
    f.close()
    time.sleep(1)
    index+=1
