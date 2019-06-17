import socket
import time

f = open("testing_communication.txt", "w")
index = 0
f.close()

TCP_IP = '10.214.64.21'
TCP_PORT = 2004


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
tcpServer.listen()
(conn, (ip, port)) = tcpServer.accept()

starttime = time.time()

while 1 :
    f = open("testing_communication.txt", "a")
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)
    f.write("{}={}\n".format(time.time()-starttime,data))
    if not data :
        print ('no data')
        break
    conn.close
    f.close()
