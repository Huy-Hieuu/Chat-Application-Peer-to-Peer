import socket
import threading
import time
from login_ui.chat_ui.core import globals
format = 'utf-8'
range = 1024

class CentralServer:
    def __init__(self) -> None:
        self.host = None
        self.central_socket = None
        self.user = None
        self.user_socket_dict = {}
         
    def make_centralserver(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(socket.gethostname())
        s.bind((self.host,9999))
        _address = s.getsockname()
        print(f'Central Server started at: {_address}')
        s.listen()
        return s

    def start_centralserver(self):
        self.central_socket = self.make_centralserver()

        while True:
            self.user, addr = self.central_socket.accept()

            #receive port from user
            user_port = self.user.recv(range).decode(format)
            print(f'socket: {self.user}')
            print(f'receive: {user_port}')
            globals.online_list.append(user_port)
            self.user_socket_dict[str(user_port)] = self.user

            print('------Online List-------')
            for _user in globals.online_list:
                print(_user)

            print('------------------------')

            # threading.Thread(target=self.fetch_friend_port, args = (user_port,)).start()

    # def fetch_friend_port(self, user_port): 
    #     user_socket = self.user_socket_dict[str(user_port)]

    #     while True:
    #         friend_id = user_socket.recv(range).decode(format)

    #         if friend_id == '':
    #             return

    #         if int(friend_id) > len(globals.online_list) - 1:
    #             user_socket.send('-1'.encode(format))
    #         else:
    #             user_socket.send(str(globals.online_list[int(friend_id)]).encode(format))
            

if __name__ == '__main__':
    globals.initOnlineList()
    CentralServer().start_centralserver()




