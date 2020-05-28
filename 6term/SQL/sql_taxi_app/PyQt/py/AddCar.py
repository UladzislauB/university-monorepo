# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddCarWindow(object):
    def setupUi(self, AddCarWindow):
        AddCarWindow.setObjectName("AddCarWindow")
        AddCarWindow.resize(290, 320)
        self.centralwidget = QtWidgets.QWidget(AddCarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(272, 231))
        self.frame.setMaximumSize(QtCore.QSize(272, 231))
        self.frame.setStyleSheet("QLineEdit\n"
                                 "{\n"
                                 "background: transparent;\n"
                                 "border: none;\n"
                                 "border-bottom: 1px solid steelblue;\n"
                                 "font: 12pt \"Comic Sans MS\";\n"
                                 "}\n"
                                 "QLineEdit:focus {\n"
                                 " outline:none; }\n"
                                 "\n"
                                 "QLabel{\n"
                                 " text-shadow: -1px -1px #FFF,\n"
                                 "               -2px -2px #FFF,\n"
                                 "               -1px 1px #FFF,\n"
                                 "               -2px 2px #FFF,\n"
                                 "               1px 1px #FFF,\n"
                                 "               2px 2px #FFF,\n"
                                 "               1px -1px #FFF,\n"
                                 "               2px -2px #FFF,\n"
                                 "               -3px -3px 2px #BBB,\n"
                                 "               -3px 3px 2px #BBB,\n"
                                 "               3px 3px 2px #BBB,\n"
                                 "               3px -3px 2px #BBB;\n"
                                 "    color: steelblue;\n"
                                 "    transition: all 1s;\n"
                                 "    font: 15pt \"Comic Sans MS\";\n"
                                 "    font-weight:bold;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_model = QtWidgets.QLineEdit(self.frame)
        self.edit_model.setStyleSheet("")
        self.edit_model.setText("")
        self.edit_model.setObjectName("edit_model")
        self.gridLayout.addWidget(self.edit_model, 1, 2, 1, 1)
        self.edit_number = QtWidgets.QLineEdit(self.frame)
        self.edit_number.setText("")
        self.edit_number.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.edit_number.setObjectName("edit_number")
        self.gridLayout.addWidget(self.edit_number, 2, 2, 1, 1)
        self.label_number = QtWidgets.QLabel(self.frame)
        self.label_number.setObjectName("label_number")
        self.gridLayout.addWidget(self.label_number, 2, 0, 1, 2)
        self.label_model = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_model.setFont(font)
        self.label_model.setStyleSheet("")
        self.label_model.setObjectName("label_model")
        self.gridLayout.addWidget(self.label_model, 1, 0, 1, 1)
        self.img = QtWidgets.QLabel(self.frame)
        self.img.setMaximumSize(QtCore.QSize(125, 125))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("../../ico/car.png"))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 0, 1, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_add.setStyleSheet("QPushButton{\n"
                                   "color: white;\n"
                                   "background: steelblue;\n"
                                   "border-radius: 60px;\n"
                                   "font: 12pt \"Comic Sans MS\";\n"
                                   "}")
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        AddCarWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddCarWindow)
        QtCore.QMetaObject.connectSlotsByName(AddCarWindow)

    def retranslateUi(self, AddCarWindow):
        _translate = QtCore.QCoreApplication.translate
        AddCarWindow.setWindowTitle(_translate("AddCarWindow", "Add car"))
        self.label_number.setText(_translate("AddCarWindow", "Number"))
        self.label_model.setText(_translate("AddCarWindow", "Model"))
        self.btn_add.setText(_translate("AddCarWindow", "Add"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddCarWindow = QtWidgets.QMainWindow()
    ui = Ui_AddCarWindow()
    ui.setupUi(AddCarWindow)
    AddCarWindow.show()
    sys.exit(app.exec_())
