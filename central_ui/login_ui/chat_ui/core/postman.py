import os
import socket
import time
format = 'utf-8'
range = 1024

class Connectserver:
    def __init__(self) -> None:
        self.host = socket.gethostbyname(socket.gethostname())
        self.mailbox_port = None
        self.conn_socket = None
        self.port = None
    
    def start_connectServer(self, host_port, mailbox_port):
        self.mailbox_port = mailbox_port
        self.port = host_port

        self.conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.conn_socket.connect((self.host, self.port))
        
        #send mailbox_port to server
        self.conn_socket.send(str(self.mailbox_port).encode(format))



class Postman:
    def __init__(self) -> None:
        self.port = None
        self.host = socket.gethostbyname(socket.gethostname())
        self.postman_socket = None
        self.postman_socket_dict = {}

    def start_postman(self,mailbox_port, friend_port):

        self.port = friend_port
        self.postman_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.postman_socket.connect((self.host, self.port))
        except:
            print("No Connection!")
            return

        print(f'{mailbox_port} Started Postman to {self.host} - {self.port}')

        self.postman_socket_dict[str(friend_port)] = self.postman_socket

        self.postman_socket.send(str(mailbox_port).encode(format))

    def send_msg(self, friend_port, msg):
        postman_socket = self.postman_socket_dict[str(friend_port)]
        print("start send msg: " + str(msg) +  " to " + str(friend_port) + " ---- " + str(postman_socket))
        postman_socket.send(msg.encode(format))

    def send_file(self, friend_port, file_path):
        print("Send File: " + str(file_path))
        file_name = os.path.basename(file_path)
        file_name = "recv_" + file_name
        postman_socket = self.postman_socket_dict[str(friend_port)]
        
        postman_socket.send("<FILE>".encode(format))
        time.sleep(0.1)
        postman_socket.send(str(file_name).encode(format))

        send_file = open(file_path, "rb")
        data = send_file.read()
        postman_socket.sendall(data)
        postman_socket.send(b"<END>")
        

    

    