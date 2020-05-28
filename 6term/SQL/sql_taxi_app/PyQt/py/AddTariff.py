# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTariff.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTariffWindow(object):
    def setupUi(self, AddTariffWindow):
        AddTariffWindow.setObjectName("AddTariffWindow")
        AddTariffWindow.resize(240, 163)
        AddTariffWindow.setStyleSheet("* {background: #212121}\n"
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
                                      "")
        self.centralwidget = QtWidgets.QWidget(AddTariffWindow)
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
        self.lbl_name = QtWidgets.QLabel(self.frame)
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.edit_name = QtWidgets.QLineEdit(self.frame)
        self.edit_name.setObjectName("edit_name")
        self.gridLayout.addWidget(self.edit_name, 0, 1, 1, 1)
        self.label_city = QtWidgets.QLabel(self.frame)
        self.label_city.setObjectName("label_city")
        self.gridLayout.addWidget(self.label_city, 1, 0, 1, 1)
        self.spinBox_city = QtWidgets.QSpinBox(self.frame)
        self.spinBox_city.setObjectName("spinBox_city")
        self.gridLayout.addWidget(self.spinBox_city, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox_no_city = QtWidgets.QSpinBox(self.frame)
        self.spinBox_no_city.setObjectName("spinBox_no_city")
        self.gridLayout.addWidget(self.spinBox_no_city, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        AddTariffWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddTariffWindow)
        QtCore.QMetaObject.connectSlotsByName(AddTariffWindow)

    def retranslateUi(self, AddTariffWindow):
        _translate = QtCore.QCoreApplication.translate
        AddTariffWindow.setWindowTitle(_translate("AddTariffWindow", "Добавить тариф"))
        self.btn_add.setText(_translate("AddTariffWindow", "Добавить"))
        self.lbl_name.setText(_translate("AddTariffWindow", "Название"))
        self.label_city.setText(_translate("AddTariffWindow", "В городе"))
        self.label_3.setText(_translate("AddTariffWindow", "За чертой"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddTariffWindow = QtWidgets.QMainWindow()
    ui = Ui_AddTariffWindow()
    ui.setupUi(AddTariffWindow)
    AddTariffWindow.show()
    sys.exit(app.exec_())
