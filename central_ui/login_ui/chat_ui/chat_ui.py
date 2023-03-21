import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QObject, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from login_ui.chat_ui.core.user import User
from login_ui.chat_ui.core import globals
from functools import partial 
import threading
import time
import os

lock = threading.Lock()
temp_friend_port = 0

class WorkerThread(QObject):
    finished = pyqtSignal()
    in_progress = pyqtSignal(int)

    def __init__(self, mailbox_port) -> None:
        super().__init__()
        self.mailbox_port = mailbox_port
        
    def run(self):
        global temp_friend_port
        while True:
            for friend_port in globals.recvMsgFrom[str(self.mailbox_port)]:
                while len(globals.recvMsgFrom[str(self.mailbox_port)][str(friend_port)]) > 0:
                    temp_friend_port = friend_port
                    print("running in thread")
                    self.in_progress.emit(friend_port)
                # time.sleep(0.1)
            time.sleep(1)

class Chat_Form(object):
    def __init__(self) -> None:
        self.user = User()
        self.user.start_user()
        self.mailbox_port = self.user.user_mailbox.get_mailboxPort()
        
    def setupUi(self, Form):       
        self.mainForm = Form
        self.mainForm.setObjectName("Form")
        self.mainForm.resize(2970, 1740)

        self.bg_label = QtWidgets.QLabel(self.mainForm)
        self.bg_label.setGeometry(QtCore.QRect(85, 2, 2790, 1620))
        pixmap = QPixmap('C:/Users/TTC/Desktop/Chat-App- P2P/central_ui/login_ui/chat_ui/bg.png')
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.setObjectName("bg_label")

        self.main_label = QtWidgets.QLabel(self.mainForm)
        self.main_label.setGeometry(QtCore.QRect(660, 90, 1650, 1500))
        self.main_label.setStyleSheet("background-color: rgb(217, 220, 255);\n""")
        self.main_label.setObjectName("main_label")

        #REQUEST LIST
        self.requestLabel = QLabel(self.mainForm)
        self.requestLabel.setGeometry(QRect(2370, 90, 445, 100))
        self.requestLabel.setText('                       REQUEST')
        self.requestLabel.setStyleSheet("background-color: rgb(243, 243, 255);")

        self.requestResetBtn = QPushButton(self.mainForm)
        self.requestResetBtn.setGeometry(QRect(2815, 90, 40, 100))
        self.requestResetBtn.setStyleSheet("background-color: rgb(242, 233, 255);")

        self.requestScrollArea = QScrollArea(self.mainForm)
        self.requestScrollArea.setObjectName('requestScrollBar')
        self.requestScrollArea.setWidgetResizable(True)
        self.requestScrollArea.setGeometry(QtCore.QRect(2370, 190, 485, 325))

        self.requestScrollAreaWidget = QWidget()
        self.requestScrollAreaWidget.setObjectName('onlScrollAreaWidget')
        self.requestScrollAreaWidget.setGeometry(QtCore.QRect(100,100,300, 700))

        self.requestBtnLayout = QVBoxLayout(self.requestScrollAreaWidget)
        #END REQUEST LIST

        #ONLINE LIST
        self.onlLabel = QLabel(self.mainForm)
        self.onlLabel.setGeometry(QRect(2370,600, 450, 100))
        self.onlLabel.setText('                       ONLINE')
        self.onlLabel.setStyleSheet("background-color: rgb(243, 243, 255);")
        self.onlResetBtn = QPushButton(self.mainForm)
        self.onlResetBtn.setGeometry(QRect(2820, 600, 38, 100))
        self.onlResetBtn.setStyleSheet("background-color: rgb(242, 233, 255);")

        self.onlScrollArea = QScrollArea(self.mainForm)
        self.onlScrollArea.setObjectName('onlScrollBar')
        self.onlScrollArea.setWidgetResizable(True)
        self.onlScrollArea.setGeometry(QtCore.QRect(2370, 700, 490, 890))

        self.onlScrollAreaWidget = QWidget()
        self.onlScrollAreaWidget.setObjectName('onlScrollAreaWidget')
        self.onlScrollAreaWidget.setGeometry(QtCore.QRect(100,100,300, 700))

        self.onlBtnlayout = QVBoxLayout(self.onlScrollAreaWidget)

        self.onlScrollArea.setWidget(self.onlScrollAreaWidget)
        #END ONLINE LIST

        self.decor_label = QtWidgets.QLabel(self.mainForm)
        self.decor_label.setGeometry(QtCore.QRect(122, 90, 485, 425))
        self.decor_label.setStyleSheet("background-color: rgb(239, 245, 255);")
        self.decor_label.setObjectName("decor_label")

        #FRIEND LIST
        self.friendLabel = QLabel(self.mainForm)
        self.friendLabel.setGeometry(QRect(117,600, 450, 100))
        self.friendLabel.setText('                      FRIEND')
        self.friendLabel.setStyleSheet("background-color: rgb(243, 243, 255);")
        self.friendResetBtn = QPushButton(self.mainForm)
        self.friendResetBtn.setGeometry(QRect(567, 600, 38, 100))
        self.friendResetBtn.setStyleSheet("background-color: rgb(242, 233, 255);")

        self.friendScrollArea = QScrollArea(self.mainForm)
        self.friendScrollArea.setObjectName('onlScrollBar')
        self.friendScrollArea.setWidgetResizable(True)
        self.friendScrollArea.setGeometry(QtCore.QRect(117, 700, 490, 890))

        self.friendScrollAreaWidget = QWidget()
        self.friendScrollAreaWidget.setObjectName('onlScrollAreaWidget')
        self.friendScrollAreaWidget.setGeometry(QtCore.QRect(100,100,300, 700))

        self.friendBtnlayout = QVBoxLayout(self.friendScrollAreaWidget)

        self.friendScrollArea.setWidget(self.friendScrollAreaWidget)
        #END FRIEND LIST

        #BEGIN CHAT BODY
        self.user_label = QtWidgets.QLabel(self.mainForm)
        self.user_label.setGeometry(QtCore.QRect(750, 150, 1445, 96))
        self.user_label.setStyleSheet("background-color: rgb(248, 240, 255);")
        self.user_label.setObjectName("user_label")

        self.chatBodyWidget = QWidget(self.mainForm)
        self.chatBodyWidget.setGeometry(QRect(750, 296, 1445, 1086))
        self.chatBodyWidget.setObjectName("chatBodyWidget")

        self.chatBodyLayout = QVBoxLayout(self.chatBodyWidget)
        self.chatBodyLayout.setObjectName("chatBodyLayout")

        self.chatBody = {}

        self.chatBody['0'] = QtWidgets.QTextEdit(self.chatBodyWidget)
        self.chatBody['0'].setReadOnly(True)
        self.chatBody['0'].setStyleSheet("background-color: rgb(233, 248, 255);")
        self.chatBody['0'].setObjectName("chatBody")

        self.chatBodyLayout.addWidget(self.chatBody['0'])

        self.sendBtnWidget = QWidget(self.mainForm)
        self.sendBtnWidget.setGeometry(QRect(1965, 1400, 218, 95))
        self.sendBtnWidget.setObjectName("sendBtnWidget")

        self.sendBtnLayout = QVBoxLayout(self.sendBtnWidget)
        self.sendBtnLayout.setObjectName("sendBtnLayout")

        self.sendBtn = {}

        self.sendBtn['0'] = QtWidgets.QPushButton(self.sendBtnWidget)
        # self.sendBtn['0'].setGeometry(QtCore.QRect(1968, 1405, 215, 95))
        self.sendBtn['0'].setText("Send")
        self.sendBtn['0'].setObjectName("sendBtn")
        self.sendBtn['0'].setStyleSheet("background-color: rgb(233, 248, 255);")

        self.sendBtnLayout.addWidget(self.sendBtn['0'])

        self.sendFileBtnWidget = QWidget(self.mainForm)
        self.sendFileBtnWidget.setGeometry(QRect(760, 1405, 225, 90))
        self.sendFileBtnWidget.setObjectName("sendFileBtnWidget")

        self.sendFileBtnLayout = QVBoxLayout(self.sendFileBtnWidget)
        self.sendFileBtnLayout.setObjectName("sendFileBtnLayout")

        self.sendFileBtn = {}

        self.sendFileBtn['0'] = QtWidgets.QPushButton(self.sendFileBtnWidget)
        # self.sendBtn['0'].setGeometry(QtCore.QRect(1968, 1405, 215, 95))
        self.sendFileBtn['0'].setText("File")
        self.sendFileBtn['0'].setObjectName("sendFileBtn")
        self.sendFileBtn['0'].setStyleSheet("background-color: rgb(233, 248, 255);")

        self.sendFileBtnLayout.addWidget(self.sendFileBtn['0'])


        self.msgTxt = QtWidgets.QLineEdit(self.mainForm)
        self.msgTxt.setGeometry(QtCore.QRect(993, 1408, 968, 90))
        self.msgTxt.setObjectName("msgTxt")
        # self.displayChatBodyUI()
        #END CHAT BODY
        self.handleBtn()

        self.handleThread()

        self.retranslateUi(self.mainForm)
        QtCore.QMetaObject.connectSlotsByName(self.mainForm)

    def handleThread(self):
        self.thread = QThread()
        self.worker = WorkerThread(self.mailbox_port)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.in_progress.connect(self.appendMsgToChatBody)

        self.thread.start()

    def appendMsgToChatBody(self):
        global temp_friend_port
        if temp_friend_port != 0:
            while len(globals.recvMsgFrom[str(self.mailbox_port)][str(temp_friend_port)]) > 0:
                print("running in appendMsgToChatBody")
                message = globals.recvMsgFrom[str(self.mailbox_port)][str(temp_friend_port)][0]
                print("appendMsgToChatBody() of " + str(self.mailbox_port) + " from " + str(temp_friend_port)+": " + str(message))
                self.chatBody[str(temp_friend_port)].append(message)
                globals.recvMsgFrom[str(self.mailbox_port)][str(temp_friend_port)].pop(0)

    def resetLayout(self, layout, scrollArea, scrollAreaWidget, user_list, function):
        for idx in reversed(range(layout.count())):
            layout.itemAt(idx).widget().setParent(None)
        for port in user_list:
            layout.addWidget(QPushButton(str(port), scrollAreaWidget))
        scrollArea.setWidget(scrollAreaWidget)

        self.button = []
        for idx in reversed(range(layout.count())):
            self.button.append(layout.itemAt(idx).widget())
            self.button[-1].clicked.connect(partial(function, int(self.button[-1].text())))

    def handleStartChatWith(self, friend_port):
        self.sendBtn[str(friend_port)] = QtWidgets.QPushButton(self.sendBtnWidget)
        self.sendBtn[str(friend_port)].setText("Send")
        self.sendBtn[str(friend_port)].setObjectName("sendBtn")

        self.sendFileBtn[str(friend_port)] = QtWidgets.QPushButton(self.sendFileBtnWidget)
        self.sendFileBtn[str(friend_port)].setText("File")
        self.sendFileBtn[str(friend_port)].setObjectName("sendFileBtn")

        self.user_label.setText(str(friend_port))

        for idx in range(self.sendBtnLayout.count()):
            self.sendBtnLayout.itemAt(idx).widget().setParent(None)
        self.sendBtnLayout.addWidget(self.sendBtn[str(friend_port)])

        for idx in range(self.sendFileBtnLayout.count()):
            self.sendFileBtnLayout.itemAt(idx).widget().setParent(None)
        self.sendFileBtnLayout.addWidget(self.sendFileBtn[str(friend_port)])

        for idx in range(self.chatBodyLayout.count()):
            self.chatBodyLayout.itemAt(idx).widget().setParent(None)
        self.chatBodyLayout.addWidget(self.chatBody[str(friend_port)])

        self.sendBtn[str(friend_port)].clicked.connect(partial(self.displayChatBodyContent, friend_port))
        self.sendFileBtn[str(friend_port)].clicked.connect(partial(self.handleSendFile, friend_port))

    def handleSendFile(self, friend_port):
        file_info = QFileDialog.getOpenFileName()
        file_path = file_info[0]
        self.user.send_file_to(friend_port, file_path)
        file_name = os.path.basename(file_path)
        
        msg = str(self.mailbox_port) + " Send File: " + str(file_name)
        self.chatBody[str(friend_port)].append(str(msg))


    def displayChatBodyContent(self, friend_port):
        if self.msgTxt.text() == "":
            return
        self.user.send_msg_to(friend_port, self.msgTxt.text())
        self.chatBody[str(friend_port)].append(str(self.mailbox_port) + " send: " + self.msgTxt.text())
        self.msgTxt.setText("")

    def createNewChatBodyWith(self, friend_port):
        #make new connection to new friend_port
        self.user.set_connection_to(friend_port)

        #check whether chatBody[friend_port] is existed or not
        if str(friend_port) in self.chatBody:
            return
        #display chatBody to chat with new friend
        print("create new body chat of " + str(friend_port))
        self.chatBody[str(friend_port)] = QtWidgets.QTextEdit(self.chatBodyWidget)
        self.chatBody[str(friend_port)].setReadOnly(True)
        self.chatBody[str(friend_port)].setStyleSheet("background-color: rgb(233, 248, 255);")
        self.chatBody[str(friend_port)].setObjectName("chatBody")
        
    def requestNewFriend(self, friend_port):
        self.user.request_new_friend(friend_port)
        self.createNewChatBodyWith(friend_port)

    def acceptNewFriend(self, friend_port):
        self.user.accept_new_friend(friend_port)
        self.createNewChatBodyWith(friend_port)

    def handleBtn(self):
        self.onlResetBtn.clicked.connect(lambda: self.resetLayout(self.onlBtnlayout, self.onlScrollArea, self.onlScrollAreaWidget, globals.online_list, self.requestNewFriend))
        self.friendResetBtn.clicked.connect(lambda: self.resetLayout(self.friendBtnlayout, self.friendScrollArea, self.friendScrollAreaWidget, globals.friend_list[str(self.mailbox_port)], self.handleStartChatWith))
        self.requestResetBtn.clicked.connect(lambda: self.resetLayout(self.requestBtnLayout, self.requestScrollArea, self.requestScrollAreaWidget, globals.friend_request[str(self.mailbox_port)], self.acceptNewFriend))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bg_label.setText(_translate("Form", ""))
        self.main_label.setText(_translate("Form", ""))
        self.decor_label.setText(_translate("Form", str(self.mailbox_port)))
        self.user_label.setText(_translate("Form", "Username"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget() #base object
    ui = Chat_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
