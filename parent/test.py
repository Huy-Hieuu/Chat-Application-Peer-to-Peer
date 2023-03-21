import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets, QtCore
from functools import partial
import threading
import time
idx = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.msgList = []
        self.resize(2970, 1740)
        self.setWindowTitle("My App")

        self.chatBodyWidget = QtWidgets.QWidget(self)
        # self.chatBodyWidget.setGeometry(QtCore.QRect(600,100,2000,1700))
        self.chatBodyWidget.setGeometry(QtCore.QRect(750, 296, 1445, 1086))
        self.chatBodyWidget.setObjectName("chatBodyWidget")

        self.chatBodyLayout = QVBoxLayout(self.chatBodyWidget)
        self.chatBodyLayout.setObjectName('chatBodyLayout')
        self.chatBodyLayout.setContentsMargins(0,0,0,0)

        self.user_label = QtWidgets.QLabel(self)
        self.user_label.setGeometry(QtCore.QRect(750, 150, 1445, 96))
        self.user_label.setStyleSheet("background-color: rgb(248, 240, 255);")
        self.user_label.setObjectName("user_label")

        self.chatBody = []
        for i in range(3):
            self.chatBody.append(QtWidgets.QTextEdit(self.chatBodyWidget))
            self.chatBody[-1].setReadOnly(True)
            # self.chatBody[-1].setGeometry(QtCore.QRect(750, 296, 1445, 1086))
            self.chatBody[-1].setStyleSheet("background-color: rgb(233, 248, 255);")
            self.chatBody[-1].setObjectName("chatBody")
        
        self.chatBodyLayout.addWidget(self.chatBody[0])

        self.sendBtn1 = QtWidgets.QPushButton(self)
        self.sendBtn1.setGeometry(QtCore.QRect(1743, 1405, 215, 95))
        self.sendBtn1.setObjectName("sendBtn1")

        self.sendBtn2 = QtWidgets.QPushButton(self)
        self.sendBtn2.setGeometry(QtCore.QRect(1968, 1405, 215, 95))
        self.sendBtn2.setObjectName("sendBtn2")

        self.sendFileBtn = QtWidgets.QPushButton(self)
        self.sendFileBtn.setGeometry(QtCore.QRect(760, 1405, 225, 90))
        self.sendFileBtn.setObjectName("sendFileBtn")

        self.msgTxt = QtWidgets.QLineEdit(self)
        self.msgTxt.setGeometry(QtCore.QRect(993, 1408, 730, 90))
        self.msgTxt.setObjectName("msgTxt")
        
        self.user_label.setText("username")
        self.sendBtn1.setText("Send 1")
        self.sendBtn2.setText("Send 2")
        self.sendFileBtn.setText("Send File")

        self.button_clicked()
        self.displayContent(1)

        threading.Thread(target=self.counting).start()
        threading.Thread(target=self.multiplying).start()
        threading.Thread(target=self.addToChatBody2).start()

    def addToChatBody2(self):
        while True:
            if len(self.msgList) > 0:
                self.chatBody[2].append(str(self.msgList[0]))
                self.msgList.remove(self.msgList[0])


    def multiplying(self):
        global idx
        for i in range(100):
            idx *= 5
            print(idx)
            time.sleep(3)
            if idx < 100:
                self.displayContent(1)


    def counting(self):
        global idx
        for i in range(100):
            idx += 1
            print(idx)
            time.sleep(1)
            if(idx > 15000):
                self.chatBodyLayout.itemAt(0).widget().setParent(None)
                self.chatBodyLayout.addWidget(self.chatBody[2])
                idx = 15001

    def button_clicked(self):
        self.sendBtn1.clicked.connect(partial(self.displayContent, 1))
        # self.sendBtn2.clicked.connect(partial(self.displayContent, 2))

    def displayContent(self, idx):
        self.chatBodyLayout.itemAt(0).widget().setParent(None)
        self.chatBody[idx].append(self.msgTxt.text())
        self.msgList.append("123123")
        self.msgTxt.setText("")
        self.chatBodyLayout.addWidget(self.chatBody[idx])

    def switchBody(self):
        pass


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
