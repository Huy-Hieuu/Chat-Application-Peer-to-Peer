import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_path = 'C:\\Users\\TTC\\Desktop\\Chat-App- P2P\\parent\\jisoo_1.png'
file = open(file_path, "rb")
file_size = os.path.getsize(file_path)

client.send("recv_jisoo.png".encode('utf-8'))

data = file.read()
client.sendall(data)
client.send(b"<END>")
