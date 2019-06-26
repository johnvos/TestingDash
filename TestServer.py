import socket

s = socket.socket()

port = 1997

s.bind(('',port))

s.listen(1)

c, addr = s.accept()

i = 0
while 1:

    i+=1

    print("Connected to: {}".format(addr))

    message = "RAWR".encode(encoding='UTF-8')

    if i == 10:
        message = "BOO".encode(encoding='UTF-8')
        c.send(message)
        break

    c.send(message)

c.close()