import socket

host='localhost'
port=50000
size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while 1:
    s.send(raw_input("Enter message: "))
    data=s.recv(size)
    print ('Received: %s' %(data))

s.close()