from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
import sys, login_ui
import mysql.connector
from login_ui.register_ui.register_form import Register_Form 
from login_ui.chat_ui.chat_ui import Chat_Form


class Login_Form(object):

        def __init__(self) -> None:
                self.mydb = mysql.connector.connect(
                user='root', password='hieu1905',
                host='localhost', database='chat_app'
                )

                self.mycursor = self.mydb.cursor()
                self.register_form = Register_Form(self.mydb, self.mycursor)

        def setupUi(self, Form):
                self.mainForm = Form
                self.mainForm.setObjectName("main form")
                self.mainForm.resize(1300, 1652)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

                self.form = QtWidgets.QWidget(self.mainForm) #inherit from From class

                self.form.setGeometry(QtCore.QRect(100, 100, 1114, 1382))
                self.form.setObjectName("form")

                pixmap = QPixmap('C:/Users/TTC/Desktop/Chat-App- P2P/central_ui/login_ui/jisoo1.png')
                self.image_label = QtWidgets.QLabel(self.mainForm)
                self.image_label.setGeometry(QtCore.QRect(60, 60, 969, 1186))
                self.image_label.setPixmap(pixmap)
                self.image_label.setScaledContents(True)
                self.image_label.setStyleSheet(
        "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
        "border-radius: 50px;")
                self.image_label.setObjectName("image_label")

                self.inside_label = QtWidgets.QLabel(self.mainForm)
                self.inside_label.setGeometry(QtCore.QRect(120, 130, 855, 1048))
                self.inside_label.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
        "border-radius: 20px;")
                self.inside_label.setObjectName("inside_label")

                self.login_label = QtWidgets.QLabel(self.mainForm)
                self.login_label.setGeometry(QtCore.QRect(450, 150, 622, 123))

                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.login_label.setFont(font)
                self.login_label.setStyleSheet("color: rgba(255, 255, 255, 210);\n"
        "")
                self.login_label.setObjectName("login_label")

                self.username = QtWidgets.QLineEdit(self.mainForm)
                self.username.setGeometry(QtCore.QRect(200, 380, 700, 132))
                self.username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
                self.username.setText("")
                self.username.setObjectName("username")
                self.password = QtWidgets.QLineEdit(self.mainForm)
                self.password.setGeometry(QtCore.QRect(200, 550, 700, 132))
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
                self.password.setObjectName("password")

                self.error = QtWidgets.QLabel(self.mainForm)
                self.error.setText("")
                self.error.setGeometry(QtCore.QRect(200, 720, 700, 50))
                self.error.setStyleSheet("color: rgb(255, 233, 254);")

                self.login_button = QtWidgets.QPushButton(self.mainForm)
                self.login_button.setGeometry(QtCore.QRect(230, 800, 574, 93))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.login_button.setFont(font)
                self.login_button.setStyleSheet("QPushButton#pushButton{\n"
        "    border-radius: 50;\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(255, 247, 248), stop:1 rgb(251, 233, 255));\n"
        "    color: rgb(100, 100, 100);\n"
        "}\n"
        "QPushButton#pushButton:hover{\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(255, 247, 248), stop:1 rgb(255, 247, 248));\n"
        "}\n"
        "QPushButton#pushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "    background-color: rgb(230, 220, 255);\n"
        "}\n"
        "\n"
        "")
                self.login_button.setObjectName("login_button")

                self.sign_up_button = QtWidgets.QPushButton(self.mainForm)
                self.sign_up_button.setGeometry(QtCore.QRect(230, 920, 574, 93))
                self.sign_up_button.setStyleSheet("")
                self.sign_up_button.setObjectName("sign_up_button")

                self.login_button.clicked.connect(self.saveToDB)

                self.sign_up_button.clicked.connect(self.switchToRegister)

                self.retranslateUi(self.mainForm)
                QtCore.QMetaObject.connectSlotsByName(self.mainForm)

                # return self.mainForm

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.image_label.setText(_translate("Form", ""))
                self.inside_label.setText(_translate("Form", ""))
                self.login_label.setText(_translate("Form", "Log In"))
                self.username.setPlaceholderText(_translate("Form", "User Name"))
                self.password.setPlaceholderText(_translate("Form", "Password"))
                self.login_button.setText(_translate("Form", "Log In"))
                self.sign_up_button.setText(_translate("Form", "Sign up"))

        def saveToDB(self):
                
                self.mycursor.execute("select count(*) from user_register where username = '" + self.get_username() + "';")
                count_res = self.mycursor.fetchone()[0]
                if count_res > 0:
                        self.mycursor.execute("select password from user_register where username = '" + self.get_username() + "';")
                        result = self.mycursor.fetchone()[0]
                        if result == self.get_password():
                                self.error.setText("Successfully LogIn!!!")
                                self.mycursor.execute("insert into user_login values('" + self.get_username() +"','"+ self.get_password() + "',now());")
                                self.mydb.commit()
                                
                                #add Chat Form here
                                self.switchToChatForm()

                        else:
                                self.error.setText("Wrong password!!!")
                else:
                        self.error.setText("Not a member!!!")
                                

                self.username.setText("")
                self.password.setText("")
                
        
        def switchToChatForm(self):
                self.mainForm.close()
                self.chatForm = QtWidgets.QWidget() #base object
                ui = Chat_Form()
                ui.setupUi(self.chatForm)
                self.chatForm.show()

        def switchToRegister(self):
                self.signupForm = QtWidgets.QWidget() #base object
                self.register_form.setupUi(self.signupForm)
                self.signupForm.show()

        def get_username(self):
                return self.username.text()

        def get_password(self):
                return self.password.text()
                


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)

        Form = QtWidgets.QWidget() #base object
        ui = Login_Form()
        ui.setupUi(Form)
        Form.show()

        sys.exit(app.exec_())