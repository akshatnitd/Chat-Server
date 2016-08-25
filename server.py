import socket

host=''
port=50000
size=1024
backlog=5

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
client,address=s.accept()

while 1:
    data=client.recv(size)
    print data
    if(data):
        client.send(raw_input("Enter message: "))
client.close()  