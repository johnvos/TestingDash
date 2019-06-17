import socket


TCP_IP = '10.214.64.21'
TCP_PORT = 2004


tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
tcpServer.listen()
(conn, (ip, port)) = tcpServer.accept()
while 1 :
    data =conn.recv(1024)
    data = data.decode("utf8")
    print (data)
    if not data :
        break
        print ('no data')
    conn.close

