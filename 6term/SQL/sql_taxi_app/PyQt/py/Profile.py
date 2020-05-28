# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Profile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.resize(291, 470)
        ProfileWindow.setStyleSheet("QLineEdit\n"
                                    "{\n"
                                    "background: transparent;\n"
                                    "border: none;\n"
                                    "font: 14pt \"Comic Sans MS\";\n"
                                    "color: steelblue;\n"
                                    "}\n"
                                    "\n"
                                    "QLabel{\n"
                                    "    color: steelblue;\n"
                                    "    transition: all 1s;\n"
                                    "    font: 14pt \"Comic Sans MS\";\n"
                                    "    font-weight:bold;\n"
                                    "}")
        self.centralwidget = QtWidgets.QWidget(ProfileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_login = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("")
        self.label_login.setObjectName("label_login")
        self.gridLayout_3.addWidget(self.label_login, 0, 0, 1, 1)
        self.edit_login = QtWidgets.QLineEdit(self.frame)
        self.edit_login.setEnabled(False)
        self.edit_login.setStyleSheet("")
        self.edit_login.setObjectName("edit_login")
        self.gridLayout_3.addWidget(self.edit_login, 0, 1, 1, 1)
        self.label_role = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_role.setFont(font)
        self.label_role.setStyleSheet("")
        self.label_role.setObjectName("label_role")
        self.gridLayout_3.addWidget(self.label_role, 1, 0, 1, 1)
        self.edit_role = QtWidgets.QLineEdit(self.frame)
        self.edit_role.setEnabled(False)
        self.edit_role.setStyleSheet("")
        self.edit_role.setObjectName("edit_role")
        self.gridLayout_3.addWidget(self.edit_role, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_firstname = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_firstname.setFont(font)
        self.label_firstname.setStyleSheet("")
        self.label_firstname.setObjectName("label_firstname")
        self.gridLayout_2.addWidget(self.label_firstname, 0, 0, 1, 1)
        self.edit_firstname = QtWidgets.QLineEdit(self.frame_3)
        self.edit_firstname.setEnabled(False)
        self.edit_firstname.setStyleSheet("")
        self.edit_firstname.setObjectName("edit_firstname")
        self.gridLayout_2.addWidget(self.edit_firstname, 0, 1, 1, 1)
        self.label_lastname = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_lastname.setFont(font)
        self.label_lastname.setStyleSheet("")
        self.label_lastname.setObjectName("label_lastname")
        self.gridLayout_2.addWidget(self.label_lastname, 1, 0, 1, 1)
        self.edit_lastname = QtWidgets.QLineEdit(self.frame_3)
        self.edit_lastname.setEnabled(False)
        self.edit_lastname.setStyleSheet("")
        self.edit_lastname.setObjectName("edit_lastname")
        self.gridLayout_2.addWidget(self.edit_lastname, 1, 1, 1, 1)
        self.label_patronymic = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_patronymic.setFont(font)
        self.label_patronymic.setStyleSheet("")
        self.label_patronymic.setObjectName("label_patronymic")
        self.gridLayout_2.addWidget(self.label_patronymic, 2, 0, 1, 1)
        self.edit_patronymic = QtWidgets.QLineEdit(self.frame_3)
        self.edit_patronymic.setEnabled(False)
        self.edit_patronymic.setStyleSheet("")
        self.edit_patronymic.setObjectName("edit_patronymic")
        self.gridLayout_2.addWidget(self.edit_patronymic, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.driver_block = QtWidgets.QFrame(self.centralwidget)
        self.driver_block.setStyleSheet("")
        self.driver_block.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.driver_block.setFrameShadow(QtWidgets.QFrame.Raised)
        self.driver_block.setObjectName("driver_block")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.driver_block)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_car = QtWidgets.QLabel(self.driver_block)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_car.setFont(font)
        self.label_car.setStyleSheet("")
        self.label_car.setObjectName("label_car")
        self.gridLayout_4.addWidget(self.label_car, 0, 0, 1, 1)
        self.edit_car = ClickableLineEdit(self.driver_block)
        self.edit_car.setStyleSheet("QLineEdit\n"
                                    "{\n"
                                    "background: transparent;\n"
                                    "border: none;\n"
                                    "border-bottom: 1px solid steelblue;\n"
                                    "font: 10pt \"Comic Sans MS\";\n"
                                    "color: steelblue;\n"
                                    "}")
        self.edit_car.setReadOnly(False)
        self.edit_car.setObjectName("edit_car")
        self.gridLayout_4.addWidget(self.edit_car, 0, 1, 1, 1)
        self.label_passport = QtWidgets.QLabel(self.driver_block)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_passport.setFont(font)
        self.label_passport.setStyleSheet("")
        self.label_passport.setObjectName("label_passport")
        self.gridLayout_4.addWidget(self.label_passport, 1, 0, 1, 1)
        self.edit_passport = ClickableLineEdit(self.driver_block)
        self.edit_passport.setStyleSheet("QLineEdit\n"
                                         "{\n"
                                         "background: transparent;\n"
                                         "border: none;\n"
                                         "border-bottom: 1px solid steelblue;\n"
                                         "font: 10pt \"Comic Sans MS\";\n"
                                         "color: steelblue;\n"
                                         "}")
        self.edit_passport.setReadOnly(False)
        self.edit_passport.setObjectName("edit_passport")
        self.gridLayout_4.addWidget(self.edit_passport, 1, 1, 1, 1)
        self.label_rating = QtWidgets.QLabel(self.driver_block)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_rating.setFont(font)
        self.label_rating.setStyleSheet("")
        self.label_rating.setObjectName("label_rating")
        self.gridLayout_4.addWidget(self.label_rating, 2, 0, 1, 1)
        self.edit_rating = QtWidgets.QLineEdit(self.driver_block)
        self.edit_rating.setStyleSheet("")
        self.edit_rating.setReadOnly(False)
        self.edit_rating.setObjectName("edit_rating")
        self.gridLayout_4.addWidget(self.edit_rating, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.driver_block)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_order = QtWidgets.QPushButton(self.frame_2)
        self.btn_order.setMinimumSize(QtCore.QSize(170, 30))
        self.btn_order.setStyleSheet("QPushButton{\n"
                                     "color: white;\n"
                                     "background: steelblue;\n"
                                     "border-radius: 60px;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "}")
        self.btn_order.setObjectName("btn_order")
        self.verticalLayout.addWidget(self.btn_order, 0, QtCore.Qt.AlignHCenter)
        self.btn_history = QtWidgets.QPushButton(self.frame_2)
        self.btn_history.setMinimumSize(QtCore.QSize(170, 30))
        self.btn_history.setStyleSheet("QPushButton{\n"
                                       "color: white;\n"
                                       "background: steelblue;\n"
                                       "border-radius: 60px;\n"
                                       "font: 12pt \"Comic Sans MS\";\n"
                                       "}")
        self.btn_history.setObjectName("btn_history")
        self.verticalLayout.addWidget(self.btn_history, 0, QtCore.Qt.AlignHCenter)
        self.btn_adminitration = QtWidgets.QPushButton(self.frame_2)
        self.btn_adminitration.setMinimumSize(QtCore.QSize(170, 30))
        self.btn_adminitration.setStyleSheet("QPushButton{\n"
                                             "color: white;\n"
                                             "background: steelblue;\n"
                                             "border-radius: 60px;\n"
                                             "font: 12pt \"Comic Sans MS\";\n"
                                             "}")
        self.btn_adminitration.setObjectName("btn_adminitration")
        self.verticalLayout.addWidget(self.btn_adminitration, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_2)
        ProfileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "Profile"))
        self.label_login.setText(_translate("ProfileWindow", "Login"))
        self.edit_login.setText(_translate("ProfileWindow", "DeneKyn"))
        self.label_role.setText(_translate("ProfileWindow", "Role"))
        self.edit_role.setText(_translate("ProfileWindow", "Driver"))
        self.label_firstname.setText(_translate("ProfileWindow", "FirsName"))
        self.edit_firstname.setText(_translate("ProfileWindow", "Denis"))
        self.label_lastname.setText(_translate("ProfileWindow", "LastName"))
        self.edit_lastname.setText(_translate("ProfileWindow", "Solovjov"))
        self.label_patronymic.setText(_translate("ProfileWindow", "Patronymic"))
        self.edit_patronymic.setText(_translate("ProfileWindow", "MIK"))
        self.label_car.setText(_translate("ProfileWindow", "Car"))
        self.edit_car.setText(_translate("ProfileWindow", "Click to add"))
        self.label_passport.setText(_translate("ProfileWindow", "Passport"))
        self.edit_passport.setText(_translate("ProfileWindow", "Clock to add"))
        self.label_rating.setText(_translate("ProfileWindow", "Raiting"))
        self.edit_rating.setText(_translate("ProfileWindow", "10 star"))
        self.btn_order.setText(_translate("ProfileWindow", "Order a taxi"))
        self.btn_history.setText(_translate("ProfileWindow", "History"))
        self.btn_adminitration.setText(_translate("ProfileWindow", "Administration"))


from PyQt.mycomponent.clickablelineedit import ClickableLineEdit

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ProfileWindow = QtWidgets.QMainWindow()
    ui = Ui_ProfileWindow()
    ui.setupUi(ProfileWindow)
    ProfileWindow.show()
    sys.exit(app.exec_())
