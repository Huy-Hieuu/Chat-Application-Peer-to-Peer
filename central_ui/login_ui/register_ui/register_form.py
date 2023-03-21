from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
import sys

class Register_Form(object):

        def __init__(self, mydb, mycursor) -> None:
                super().__init__()
                self.mydb = mydb
                self.mycursor = mycursor

        def setupUi(self, Form):
                self.mainForm = Form
                self.mainForm.setObjectName("Form")
                self.mainForm.resize(1300, 1652)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

                self.form = QtWidgets.QWidget(self.mainForm) #inherit from From class

                self.form.setGeometry(QtCore.QRect(100, 100, 1114, 1382))
                self.form.setObjectName("form")

                pixmap = QPixmap('C:/Users/TTC/Desktop/Chat-App- P2P/central_ui/login_ui/register_ui/jisoo_1.png')
                self.image_label = QtWidgets.QLabel(self.form)
                self.image_label.setPixmap(pixmap)
                self.image_label.setGeometry(QtCore.QRect(60, 60, 969, 1186))
                self.image_label.setStyleSheet(
        "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
        "border-radius: 50px;")
                
                self.image_label.setObjectName("image_label")

                self.inside_label = QtWidgets.QLabel(self.form)
                self.inside_label.setGeometry(QtCore.QRect(120, 130, 855, 1048))
                self.inside_label.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
        "border-radius: 20px;")
                self.inside_label.setObjectName("inside_label")

                self.register_label = QtWidgets.QLabel(self.form)
                self.register_label.setGeometry(QtCore.QRect(380, 150, 622, 123))

                font = QtGui.QFont()
                font.setPointSize(20)
                font.setBold(True)
                font.setWeight(75)
                self.register_label.setFont(font)
                self.register_label.setStyleSheet("color: rgba(255, 255, 255, 210);\n"
        "")
                self.register_label.setObjectName("register_label")

                self.username = QtWidgets.QLineEdit(self.form)
                self.username.setGeometry(QtCore.QRect(200, 350, 700, 132))
                self.username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
                self.username.setText("")
                self.username.setObjectName("username")

                self.password = QtWidgets.QLineEdit(self.form)
                self.password.setGeometry(QtCore.QRect(200, 500, 700, 132))
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
                self.password.setObjectName("password")

                self.gmail = QtWidgets.QLineEdit(self.form)
                self.gmail.setGeometry(QtCore.QRect(200, 650, 700, 132))
                self.gmail.setStyleSheet("background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-bottom: 2px solid rgba(105,118,132,255);\n"
        "color: rgba(255, 255, 255,210);\n"
        "padding-bottom: 7px;")
                self.gmail.setObjectName("gmail")

                self.error = QtWidgets.QLabel(self.form)
                self.error.setText("")
                self.error.setGeometry(QtCore.QRect(200, 800, 700, 50))
                self.error.setStyleSheet("color: rgb(255, 233, 254);")

                self.sign_up_button = QtWidgets.QPushButton(self.form)
                self.sign_up_button.setGeometry(QtCore.QRect(230, 900, 574, 93))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.sign_up_button.setFont(font)
                self.sign_up_button.setStyleSheet("QPushButton#pushButton{\n"
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
                self.sign_up_button.setObjectName("sign_up_button")

                self.sign_up_button.clicked.connect(self.registerToDB)

                self.retranslateUi(self.mainForm)
                QtCore.QMetaObject.connectSlotsByName(self.mainForm)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.image_label.setText(_translate("Form", ""))
                self.inside_label.setText(_translate("Form", ""))
                self.register_label.setText(_translate("Form", "Sign Up"))
                self.username.setPlaceholderText(_translate("Form", "UserName"))
                self.password.setPlaceholderText(_translate("Form", "Password"))
                self.sign_up_button.setText(_translate("Form", "Sign up"))
                self.gmail.setPlaceholderText(_translate("" , "Gmail"))

        def registerToDB(self):
                print("receive button event")
                if len(self.get_username()) == 0 or len(self.get_password()) == 0 or len(self.gmail.text()) == 0:
                    self.error.setText("Please fill up all information") 
                else:
                    self.mycursor.execute("select count(*) from user_register where username = '" + self.get_username() + "';")
                    count_res = self.mycursor.fetchone()[0]

                    if count_res == 0:
                        self.mycursor.execute("insert into user_register values('" + self.get_username() +"','"+ self.get_password() + "','" + self.gmail.text() + "');")
                        self.mydb.commit()
                        self.error.setText("Sign Up Successfully!")
                    else:
                        self.error.setText("Username already exists!")
                                
                
                self.mycursor.execute("select * from user_register;")
                myresult = self.mycursor.fetchall()

                for x in myresult:
                        print(x)

        def get_username(self):
                return self.username.text()

        def get_password(self):
                return self.password.text()
                


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget() #base object
        ui = Register_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())