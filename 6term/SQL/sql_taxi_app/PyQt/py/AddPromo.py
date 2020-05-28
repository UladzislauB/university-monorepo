# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPromo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPromoWindow(object):
    def setupUi(self, AddPromoWindow):
        AddPromoWindow.setObjectName("AddPromoWindow")
        AddPromoWindow.resize(258, 160)
        AddPromoWindow.setStyleSheet("* {background: #212121}\n"
                                     "QLineEdit\n"
                                     "{\n"
                                     "background: transparent;\n"
                                     "border: none;\n"
                                     "border-bottom: 1px solid #1db954;\n"
                                     "font: 16pt \"Comic Sans MS\";\n"
                                     "}\n"
                                     "QLineEdit:focus {\n"
                                     " outline:none; }\n"
                                     "\n"
                                     "QLabel{\n"
                                     "    color: #b3b3b3;\n"
                                     "    font: 12pt \"Comic Sans MS\";\n"
                                     "    font-weight:bold;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QSpinBox{\n"
                                     "background: transparent;\n"
                                     "border: none;\n"
                                     "border-bottom: 1px solid #1db954;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton{\n"
                                     "color: white;\n"
                                     "background: #1db954;\n"
                                     "border-radius: 5px;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "}\n"
                                     "\n"
                                     "QDateEdit{\n"
                                     "background: transparent;\n"
                                     "border: none;\n"
                                     "font: 14pt \"Comic Sans MS\";\n"
                                     "color: #b3b3b3;\n"
                                     "}")
        self.centralwidget = QtWidgets.QWidget(AddPromoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_2.addWidget(self.btn_add, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_promo = QtWidgets.QLabel(self.frame)
        self.lbl_promo.setObjectName("lbl_promo")
        self.gridLayout.addWidget(self.lbl_promo, 0, 0, 1, 1)
        self.label_discount = QtWidgets.QLabel(self.frame)
        self.label_discount.setObjectName("label_discount")
        self.gridLayout.addWidget(self.label_discount, 2, 0, 1, 1)
        self.lbl_expires = QtWidgets.QLabel(self.frame)
        self.lbl_expires.setObjectName("lbl_expires")
        self.gridLayout.addWidget(self.lbl_expires, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.spinBox_discount = QtWidgets.QSpinBox(self.frame)
        self.spinBox_discount.setObjectName("spinBox_discount")
        self.gridLayout.addWidget(self.spinBox_discount, 2, 1, 1, 1)
        self.dateEdit_expires = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_expires.setObjectName("dateEdit_expires")
        self.gridLayout.addWidget(self.dateEdit_expires, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        AddPromoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPromoWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPromoWindow)

    def retranslateUi(self, AddPromoWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPromoWindow.setWindowTitle(_translate("AddPromoWindow", "Добавить промокод"))
        self.btn_add.setText(_translate("AddPromoWindow", "Добавить"))
        self.lbl_promo.setText(_translate("AddPromoWindow", "Промокод"))
        self.label_discount.setText(_translate("AddPromoWindow", "Скидка"))
        self.lbl_expires.setText(_translate("AddPromoWindow", "Истекает"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddPromoWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPromoWindow()
    ui.setupUi(AddPromoWindow)
    AddPromoWindow.show()
    sys.exit(app.exec_())
