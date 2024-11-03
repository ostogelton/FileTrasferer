import socket

socketclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketclient.connect(('IP_Address',8080))

file = open('image.jpg', 'wb')

while True:
    data = socketclient.recv(1024)
    while data:
        file.write(data)
        data = socketclient.recv(1024)
    file.close()
    break
print("Successfully Received")









