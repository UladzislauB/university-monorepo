# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPayment.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPaymentWindow(object):
    def setupUi(self, AddPaymentWindow):
        AddPaymentWindow.setObjectName("AddPaymentWindow")
        AddPaymentWindow.resize(338, 497)
        AddPaymentWindow.setStyleSheet("* {background: #212121}\n"
                                       "QLineEdit\n"
                                       "{\n"
                                       "background: transparent;\n"
                                       "border: none;\n"
                                       "border-bottom: 1px solid #1db954;\n"
                                       "font: 10pt \"Comic Sans MS\";\n"
                                       "color: #b3b3b3;\n"
                                       "}\n"
                                       "\n"
                                       "QLabel{\n"
                                       "    color: #b3b3b3;\n"
                                       "    transition: all 1s;\n"
                                       "    font: 10pt \"Comic Sans MS\";\n"
                                       "    font-weight:bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton{\n"
                                       "color: white;\n"
                                       "background: #1db954;\n"
                                       "border-radius: 10px;\n"
                                       "font: 12pt \"Comic Sans MS\";\n"
                                       "}\n"
                                       "\n"
                                       "QComboBox{\n"
                                       "background: transparent;\n"
                                       "border: none;\n"
                                       "border-bottom: 1px solid #1db954;\n"
                                       "font: 12pt \"Comic Sans MS\";\n"
                                       "}\n"
                                       "\n"
                                       "QDateEdit{\n"
                                       "background: transparent;\n"
                                       "border: none;\n"
                                       "font: 14pt \"Comic Sans MS\";\n"
                                       "color: #b3b3b3;\n"
                                       "}")
        self.centralwidget = QtWidgets.QWidget(AddPaymentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(130, 40))
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_expiration_date = QtWidgets.QLabel(self.frame_2)
        self.label_expiration_date.setObjectName("label_expiration_date")
        self.verticalLayout_3.addWidget(self.label_expiration_date)
        self.dateEdit_expiration_date = QtWidgets.QDateEdit(self.frame_2)
        self.dateEdit_expiration_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2099, 12, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_expiration_date.setObjectName("dateEdit_expiration_date")
        self.verticalLayout_3.addWidget(self.dateEdit_expiration_date)
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_security_code = QtWidgets.QLabel(self.frame_3)
        self.label_security_code.setObjectName("label_security_code")
        self.verticalLayout_4.addWidget(self.label_security_code)
        self.edit_security_code = QtWidgets.QLineEdit(self.frame_3)
        self.edit_security_code.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_security_code.setObjectName("edit_security_code")
        self.verticalLayout_4.addWidget(self.edit_security_code)
        self.gridLayout.addWidget(self.frame_3, 3, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_card_holder = QtWidgets.QLabel(self.frame_4)
        self.label_card_holder.setObjectName("label_card_holder")
        self.verticalLayout_2.addWidget(self.label_card_holder)
        self.edit_card_holder = QtWidgets.QLineEdit(self.frame_4)
        self.edit_card_holder.setObjectName("edit_card_holder")
        self.verticalLayout_2.addWidget(self.edit_card_holder)
        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 2)
        self.img_payment = QtWidgets.QLabel(self.centralwidget)
        self.img_payment.setMaximumSize(QtCore.QSize(320, 210))
        self.img_payment.setText("")
        self.img_payment.setPixmap(QtGui.QPixmap("../../ico/card.png"))
        self.img_payment.setScaledContents(True)
        self.img_payment.setObjectName("img_payment")
        self.gridLayout.addWidget(self.img_payment, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_card_number = QtWidgets.QLabel(self.frame)
        self.label_card_number.setObjectName("label_card_number")
        self.verticalLayout.addWidget(self.label_card_number)
        self.edit_card_number = QtWidgets.QLineEdit(self.frame)
        self.edit_card_number.setObjectName("edit_card_number")
        self.verticalLayout.addWidget(self.edit_card_number)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        AddPaymentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPaymentWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPaymentWindow)

    def retranslateUi(self, AddPaymentWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPaymentWindow.setWindowTitle(_translate("AddPaymentWindow", "Добавить карту"))
        self.btn_add.setText(_translate("AddPaymentWindow", "Добавить"))
        self.label_expiration_date.setText(_translate("AddPaymentWindow", "Срок действия"))
        self.dateEdit_expiration_date.setDisplayFormat(_translate("AddPaymentWindow", "MM/yy"))
        self.label_security_code.setText(_translate("AddPaymentWindow", "CVC"))
        self.label_card_holder.setText(_translate("AddPaymentWindow", "Владелец карты"))
        self.label_card_number.setText(_translate("AddPaymentWindow", "Номер карты"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddPaymentWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPaymentWindow()
    ui.setupUi(AddPaymentWindow)
    AddPaymentWindow.show()
    sys.exit(app.exec_())
