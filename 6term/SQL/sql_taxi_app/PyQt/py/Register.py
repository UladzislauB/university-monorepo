# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(290, 493)
        RegisterWindow.setStyleSheet("* {background: #212121}\n"
                                     "QLineEdit\n"
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
                                     "}\n"
                                     "\n"
                                     "QRadioButton{\n"
                                     "color: #b3b3b3;\n"
                                     "}\n"
                                     "QPushButton{\n"
                                     "color: white;\n"
                                     "background: #1db954;\n"
                                     "border-radius: 10px;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "}")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(272, 231))
        self.frame.setMaximumSize(QtCore.QSize(272, 231))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.img = QtWidgets.QLabel(self.frame)
        self.img.setMaximumSize(QtCore.QSize(150, 150))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("../../ico/passenger.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 0, 1, 1, 2)
        self.label_login = QtWidgets.QLabel(self.frame)
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
        self.edit_login = QtWidgets.QLineEdit(self.frame)
        self.edit_login.setStyleSheet("")
        self.edit_login.setText("")
        self.edit_login.setObjectName("edit_login")
        self.gridLayout.addWidget(self.edit_login, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.edit_password = QtWidgets.QLineEdit(self.frame)
        self.edit_password.setText("")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_password.setObjectName("edit_password")
        self.gridLayout.addWidget(self.edit_password, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(288, 119))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.edit_lastname = QtWidgets.QLineEdit(self.frame_2)
        self.edit_lastname.setStyleSheet("")
        self.edit_lastname.setText("")
        self.edit_lastname.setObjectName("edit_lastname")
        self.gridLayout_2.addWidget(self.edit_lastname, 1, 1, 1, 1)
        self.label_lastname = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_lastname.setFont(font)
        self.label_lastname.setStyleSheet("")
        self.label_lastname.setObjectName("label_lastname")
        self.gridLayout_2.addWidget(self.label_lastname, 1, 0, 1, 1)
        self.label_patronymic = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setStyleSheet("")
        self.label_patronymic.setObjectName("label_patronymic")
        self.gridLayout_2.addWidget(self.label_patronymic, 2, 0, 1, 1)
        self.edit_firstname = QtWidgets.QLineEdit(self.frame_2)
        self.edit_firstname.setStyleSheet("")
        self.edit_firstname.setText("")
        self.edit_firstname.setObjectName("edit_firstname")
        self.gridLayout_2.addWidget(self.edit_firstname, 0, 1, 1, 1)
        self.label_firstname = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_firstname.setFont(font)
        self.label_firstname.setStyleSheet("")
        self.label_firstname.setObjectName("label_firstname")
        self.gridLayout_2.addWidget(self.label_firstname, 0, 0, 1, 1)
        self.edit_patronymic = QtWidgets.QLineEdit(self.frame_2)
        self.edit_patronymic.setStyleSheet("")
        self.edit_patronymic.setText("")
        self.edit_patronymic.setObjectName("edit_patronymic")
        self.gridLayout_2.addWidget(self.edit_patronymic, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(281, 66))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rbtn_driver = QtWidgets.QRadioButton(self.frame_3)
        self.rbtn_driver.setObjectName("rbtn_driver")
        self.gridLayout_3.addWidget(self.rbtn_driver, 1, 1, 1, 1)
        self.rbtn_client = QtWidgets.QRadioButton(self.frame_3)
        self.rbtn_client.setChecked(True)
        self.rbtn_client.setObjectName("rbtn_client")
        self.gridLayout_3.addWidget(self.rbtn_client, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("")
        self.label_1.setObjectName("label_1")
        self.gridLayout_3.addWidget(self.label_1, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_3)
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_register.setStyleSheet("")
        self.btn_register.setObjectName("btn_register")
        self.verticalLayout.addWidget(self.btn_register)
        RegisterWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Регистрация"))
        self.label_login.setText(_translate("RegisterWindow", "Логин"))
        self.label.setText(_translate("RegisterWindow", "Пароль"))
        self.label_lastname.setText(_translate("RegisterWindow", "Фамилия"))
        self.label_patronymic.setText(_translate("RegisterWindow", "Имя"))
        self.label_firstname.setText(_translate("RegisterWindow", "Отчество"))
        self.rbtn_driver.setText(_translate("RegisterWindow", "Водитель"))
        self.rbtn_client.setText(_translate("RegisterWindow", "Клиент"))
        self.label_1.setText(_translate("RegisterWindow", "Выберите тип"))
        self.btn_register.setText(_translate("RegisterWindow", "Регистрация"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())
