import threading
from login_ui.chat_ui.core.mailbox import Mailbox
from login_ui.chat_ui.core.postman import Connectserver, Postman
from login_ui.chat_ui.core import globals
import os

format = 'utf-8'

class User:
    def __init__(self):
        self.user_mailbox = Mailbox()
        self.user_postman = Postman()
        self.user_connect_server = Connectserver()

    def start_user(self):
        # make mailbox in order to get port
        self.user_mailbox.make_mailbox()
        #get mailbox_port
        self.mailbox_port = self.user_mailbox.get_mailboxPort()
        # init mailbox port into globals friend_request dict
        globals.friend_request[str(self.mailbox_port)] = []
        # init friend_list 
        globals.friend_list[str(self.mailbox_port)] = []
        #connect to central server
        self.user_connect_server.start_connectServer(host_port=9999, mailbox_port= self.user_mailbox.get_mailboxPort())

        
        #start mailbox to wait
        threading.Thread(target=self.user_mailbox.start_mailbox).start()

    #put mailbox port into list of globals friend_requests dict
    def request_new_friend(self, friend_port):
        if (self.mailbox_port in globals.friend_request[str(friend_port)]) or (friend_port == self.mailbox_port) or (friend_port in globals.friend_request[str(self.mailbox_port)]):
            print("failed to append mailbox_port: " + str(self.mailbox_port) + " to friend_port: " + str(friend_port) + " list: " + str(globals.friend_request[str(friend_port)]))
            return
        print("successfully append mailbox_port: " + str(self.mailbox_port) + " to friend_port: " + str(friend_port))
        globals.friend_request[str(friend_port)].append(self.mailbox_port)

    #put new friend port into self.friend list
    def accept_new_friend(self, friend_port):
        if friend_port in globals.friend_list[str(self.mailbox_port)]:
            print("FAILED! friend_port: " + str(friend_port) +" has already been in the friend_list of " + str(self.mailbox_port))
            return
        print("SUCCEEDED! friend_port: " + str(friend_port) +" has been now in the friend_list of " + str(self.mailbox_port))
        globals.friend_list[str(self.mailbox_port)].append(friend_port)
        globals.friend_list[str(friend_port)].append(self.mailbox_port)

    def set_connection_to(self, friend_port):
        self.user_postman.start_postman(mailbox_port=self.mailbox_port ,friend_port=int(friend_port))

    def send_msg_to(self, friend_port, msg):
        print(str(self.mailbox_port) +" send to " + str(friend_port) + ": " + str(msg))
        self.user_postman.send_msg(friend_port, msg)
    
    def send_file_to(self, friend_port, file_path):
        print(str(self.mailbox_port) +" send to " + str(friend_port) + ": " + str(file_path))
        self.user_postman.send_file(friend_port, file_path)

#CHUA LAM TRUONG HOP KHI PEER 1 CHAT PEER 2 THI PEER 2 CUNG PHAI KET NOI LAI

if __name__ == '__main__':
    user = User()
    user.start_user()
    user.set_connection_to(friend_id=0)
    user.set_connection_to(friend_id=1)
    user.start_chat_with()
    # user.start_chat_with(friend_id=1)



        
        
