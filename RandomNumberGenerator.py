import random
import time

# creates a random number per line and writes them on the log file
# as of now, it closes the file and reopens it every line,
# for the sake of allowing readers to read the file in between writes
# must find a more efficient way

f = open("testing_communication.log", "w")
index = 0
f.close()

while 1:
    f = open("testing_communication.log", "a")
    number = random.randint(0,10)
    f.write("{},{}\n".format(index, number))
    print(index,number)
    f.close()
    time.sleep(0.1)
    index+=1
