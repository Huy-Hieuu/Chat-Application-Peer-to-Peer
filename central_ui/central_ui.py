from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
from login_ui.login_form_ui import Login_Form
from login_ui.chat_ui.core.central_server import CentralServer
from login_ui.chat_ui.core import globals
import threading

class Central_Ui(object):
    def __init__(self) -> None:

        #initialize global online list
        globals.initOnlineList()
        globals.initFriendControl()
        globals.initRecvMsgDict()
        
        #create central server
        threading.Thread(target=CentralServer().start_centralserver).start()
        self.loginWidgetList = []
        self.loginFormList = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 580)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.bg_label = QtWidgets.QLabel(Form)
        self.bg_label.setGeometry(QtCore.QRect(0,0,785, 580))
        self.bg_label.setStyleSheet("background-color: rgba(0, 0, 0,50);\n"
        "border-radius: 20px;")

        self.port_line = QtWidgets.QLineEdit(Form)
        self.port_line.setGeometry(QtCore.QRect(200, 165, 380, 110))
        self.port_line.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
        self.port_line.setText("")
        self.port_line.setObjectName("port_line")
        self.port_line.setPlaceholderText('Port Number')

        self.startBtn = QtWidgets.QPushButton('Start',Form)
        self.startBtn.setGeometry(QtCore.QRect(200, 300, 380, 110))
        
        self.handleBtn()

    def handleBtn(self):
        self.startBtn.clicked.connect(self.switchToLogin)

    def switchToLogin(self):
        self.loginWidgetList.append(QtWidgets.QWidget())
        self.loginFormList.append(Login_Form())
        self.loginFormList[-1].setupUi(self.loginWidgetList[-1])
        self.loginWidgetList[-1].show()

def startCentralUi():
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget() 
    ui = Central_Ui()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    
    startCentralUi()




