# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(289, 255)
        LoginWindow.setStyleSheet("* {background: #212121}\n")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(272, 231))
        self.frame_2.setStyleSheet("QLineEdit\n"
                                   "{\n"
                                   "background: transparent;\n"
                                   "border: none;\n"
                                   "border-bottom: 1px solid #1db954;\n"
                                   "font: 12pt \"Comic Sans MS\";\n"
                                   "}\n"
                                   "QLineEdit:focus {\n"
                                   " outline:none; }\n"
                                   "\n"
                                   "QLabel{\n"
                                   "    color: #b3b3b3;\n"
                                   "    font: 15pt \"Comic Sans MS\";\n"
                                   "    font-weight:bold;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.img = QtWidgets.QLabel(self.frame_2)
        self.img.setMaximumSize(QtCore.QSize(100, 100))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("../../ico/taxi.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_login = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("")
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 1, 0, 1, 1)
        self.edit_login = QtWidgets.QLineEdit(self.frame_2)
        self.edit_login.setStyleSheet("")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.gridLayout.addWidget(self.edit_login, 1, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.frame_2)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)
        self.edit_password = QtWidgets.QLineEdit(self.frame_2)
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.gridLayout.addWidget(self.edit_password, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setMinimumSize(QtCore.QSize(100, 41))
        self.btn_login.setStyleSheet("QPushButton{\n"
                                     "color: white;\n"
                                     "background: #1db954;\n"
                                     "border-radius: 10px;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "}")
        self.btn_login.setObjectName("btn_login")
        self.gridLayout_2.addWidget(self.btn_login, 1, 0, 1, 1)
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setMinimumSize(QtCore.QSize(100, 41))
        self.btn_register.setStyleSheet("QPushButton{\n"
                                        "color: white;\n"
                                        "background: #1db954;\n"
                                        "border-radius: 10px;\n"
                                        "font: 12pt \"Comic Sans MS\";\n"
                                        "}")
        self.btn_register.setObjectName("btn_register")
        self.gridLayout_2.addWidget(self.btn_register, 1, 1, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Авторизация"))
        self.label_login.setText(_translate("LoginWindow", "Логин"))
        self.label_password.setText(_translate("LoginWindow", "Пароль"))
        self.btn_login.setText(_translate("LoginWindow", "Логин"))
        self.btn_register.setText(_translate("LoginWindow", "Регистрация"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
