import socket
import time
import mysql.connector

cnx = mysql.connector.connect(user='Andrey', password = '12345678', database='sakila')
cursor = cnx.cursor()

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    elif data.decode("utf-8") == '1':
        query = ("SELECT first_name, last_name FROM actor ")
        cursor.execute(query)
        for (first_name, last_name) in cursor:
            conn.send(first_name.encode())
    else:
        conn.send("unknown data".encode())
        print(data.decode("utf-8"))
