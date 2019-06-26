import socket

s = socket.socket()

port = 1997

s.connect(('10.214.64.21',port))

while 1:
    received = s.recv(1024)

    if received.decode(encoding='UTF-8').lower() == "boo":
        print("DONE")
        break

    print(received.decode(encoding='UTF-8'))

s.close()
exit(0)