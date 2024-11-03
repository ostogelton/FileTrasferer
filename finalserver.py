import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('IP_Address', 8080))

serversocket.listen(5)
conn, addr = serversocket.accept()
print("Connected to", addr)
file = open('image.jpg', 'rb')
data = file.read()

while data:
    conn.send(data)
    data = file.read(1024)

file.close()
print("Successfully Transfered")


















