import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send("1".encode())
while True:
    data = sock.recv(1024)
    print(data.decode('UTF-8'))
sock.close()


