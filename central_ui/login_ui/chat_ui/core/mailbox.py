import socket
import threading
from login_ui.chat_ui.core import globals
import time
format = 'utf-8'
range = 1024

class Mailbox:
    def __init__(self) -> None:
        self.host = None
        self.mailbox_socket = None
        self.friend_socket_dict = {}   #addr -> socket
        self.friend_port_dict = {}     #addr -> port 
        self.mailbox_port = 0
        self.recvMsgFrom = {}

    def make_mailbox(self):
        self.mailbox_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.mailbox_socket.bind((self.host,0))
        (mailbox_host, self.mailbox_port) = self.mailbox_socket.getsockname()
        print(f'mailbox started at: ({mailbox_host}, {self.mailbox_port})')
        globals.recvMsgFrom[str(self.mailbox_port)] = {}
        self.mailbox_socket.listen()
    
    def get_mailboxPort(self):
        return self.mailbox_port

    def start_mailbox(self):

        while True:
            try:
                friend_socket, friend_addr = self.mailbox_socket.accept()
                print("Connection Successfully!!")
            except:
                print("Connection Failed!!")
                return

            #RECEIVE FRIEND PORT FROM FISRT SEND OF POSTMAN
            friend_port = friend_socket.recv(range).decode(format)
            
            print('Connected Mailbox to: ' + friend_addr[0] + ' ' + str(friend_port))

            self.friend_port_dict[str(friend_addr[1])] = friend_port
            self.friend_socket_dict[str(friend_addr[1])] = friend_socket
            globals.recvMsgFrom[str(self.mailbox_port)][str(friend_port)] = []

            threading.Thread(target=self.receive_msg, args= (friend_addr[1],)).start()

    def receive_msg(self, friend_addr):
        friend_socket = self.friend_socket_dict[str(friend_addr)]
        friend_port =  self.friend_port_dict[str(friend_addr)]
        
        while True:
            msg = friend_socket.recv(range).decode(format)

            if msg == '':
                continue
            elif msg == '<FILE>':
                file_name = friend_socket.recv(range).decode(format)
                file_recv = open(file_name, "wb")
                file_bytes = b""
                done = False

                while not done:
                    data = friend_socket.recv(range)
                    file_bytes += data
                    if file_bytes[-5:] == b"<END>":
                        done = True

                
                file_recv.write(file_bytes)
                file_recv.close()

                print(str(self.mailbox_port) + " receive file from "+str(friend_port) +": "+ str(file_name))
                globals.recvMsgFrom[str(self.mailbox_port)][str(friend_port)].append(str(friend_port) + ": Receive File " + str(file_name))
                time.sleep(0.2)
            else:
                print(str(self.mailbox_port) + " receive msg from "+str(friend_port) +": "+ str(msg))
                globals.recvMsgFrom[str(self.mailbox_port)][str(friend_port)].append(str(friend_port) + ": " + str(msg))


if __name__ == '__main__':
    mailbox = Mailbox()
    mailbox.make_mailbox()
    mailbox.start_mailbox()
            

