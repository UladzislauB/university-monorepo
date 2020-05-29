# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Order.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 268)
        MainWindow.setStyleSheet("* {background: #212121}\n"
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
                                 "    font: 14pt \"Comic Sans MS\";\n"
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
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.img_locality = QtWidgets.QLabel(self.frame)
        self.img_locality.setMaximumSize(QtCore.QSize(50, 50))
        self.img_locality.setText("")
        self.img_locality.setPixmap(QtGui.QPixmap("../../ico/locality.png"))
        self.img_locality.setScaledContents(True)
        self.img_locality.setObjectName("img_locality")
        self.gridLayout.addWidget(self.img_locality, 0, 0, 2, 1)
        self.label_from = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_from.setFont(font)
        self.label_from.setStyleSheet("")
        self.label_from.setObjectName("label_from")
        self.gridLayout.addWidget(self.label_from, 0, 1, 1, 1)
        self.edit_from = ClickableLineEdit(self.frame)
        self.edit_from.setStyleSheet("")
        self.edit_from.setReadOnly(False)
        self.edit_from.setObjectName("edit_from")
        self.gridLayout.addWidget(self.edit_from, 0, 2, 1, 1)
        self.label_to = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_to.setFont(font)
        self.label_to.setStyleSheet("")
        self.label_to.setObjectName("label_to")
        self.gridLayout.addWidget(self.label_to, 1, 1, 1, 1)
        self.edit_to = ClickableLineEdit(self.frame)
        self.edit_to.setStyleSheet("")
        self.edit_to.setObjectName("edit_to")
        self.gridLayout.addWidget(self.edit_to, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_payment = QtWidgets.QLabel(self.frame_2)
        self.lbl_payment.setObjectName("lbl_payment")
        self.gridLayout_2.addWidget(self.lbl_payment, 0, 1, 1, 2)
        self.comboBox_payment = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_payment.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_payment.setStyleSheet("")
        self.comboBox_payment.setObjectName("comboBox_payment")
        self.gridLayout_2.addWidget(self.comboBox_payment, 0, 3, 1, 2)
        self.btn_add = QtWidgets.QPushButton(self.frame_2)
        self.btn_add.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_add.setMaximumSize(QtCore.QSize(50, 25))
        self.btn_add.setStyleSheet("")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 5, 1, 1)
        self.lbl_tarif = QtWidgets.QLabel(self.frame_2)
        self.lbl_tarif.setObjectName("lbl_tarif")
        self.gridLayout_2.addWidget(self.lbl_tarif, 1, 1, 1, 2)
        self.lbl_price = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_price.setFont(font)
        self.lbl_price.setStyleSheet("")
        self.lbl_price.setObjectName("lbl_price")
        self.gridLayout_2.addWidget(self.lbl_price, 2, 1, 2, 1)
        self.edit_price = QtWidgets.QLineEdit(self.frame_2)
        self.edit_price.setEnabled(False)
        self.edit_price.setStyleSheet("QLineEdit\n"
                                      "{\n"
                                      "background: transparent;\n"
                                      "border: none;\n"
                                      "font: 16pt \"Comic Sans MS\";\n"
                                      "color: #b3b3b3;\n"
                                      "}")
        self.edit_price.setObjectName("edit_price")
        self.gridLayout_2.addWidget(self.edit_price, 2, 2, 2, 1)
        self.lbl_promo = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_promo.setFont(font)
        self.lbl_promo.setStyleSheet("")
        self.lbl_promo.setObjectName("lbl_promo")
        self.gridLayout_2.addWidget(self.lbl_promo, 2, 3, 2, 1)
        self.edit_promo = QtWidgets.QLineEdit(self.frame_2)
        self.edit_promo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.edit_promo.setObjectName("edit_promo")
        self.gridLayout_2.addWidget(self.edit_promo, 3, 4, 1, 2)
        self.comboBox_tarif = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_tarif.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_tarif.setStyleSheet("")
        self.comboBox_tarif.setObjectName("comboBox_tarif")
        self.gridLayout_2.addWidget(self.comboBox_tarif, 1, 3, 1, 3)
        self.img_payment = QtWidgets.QLabel(self.frame_2)
        self.img_payment.setMaximumSize(QtCore.QSize(100, 100))
        self.img_payment.setText("")
        self.img_payment.setPixmap(QtGui.QPixmap("../../ico/credit-card.png"))
        self.img_payment.setScaledContents(True)
        self.img_payment.setObjectName("img_payment")
        self.gridLayout_2.addWidget(self.img_payment, 0, 0, 4, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_submit.setStyleSheet("")
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Заказать такси"))
        self.label_from.setText(_translate("MainWindow", "Откуда"))
        self.edit_from.setText(_translate("MainWindow", ""))
        self.label_to.setText(_translate("MainWindow", "Куда"))
        self.edit_to.setText(_translate("MainWindow", ""))
        self.lbl_payment.setText(_translate("MainWindow", "Способ оплаты"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.lbl_tarif.setText(_translate("MainWindow", "Выбрать тариф"))
        self.lbl_price.setText(_translate("MainWindow", "Цена"))
        self.edit_price.setText(_translate("MainWindow", "1100"))
        self.lbl_promo.setText(_translate("MainWindow", "Промокод"))
        self.btn_submit.setText(_translate("MainWindow", "Подтвердить"))


from PyQt.mycomponent.clickablelineedit import ClickableLineEdit

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
