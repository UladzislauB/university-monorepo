# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EndRide.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EndRide(object):
    def setupUi(self, EndRide):
        EndRide.setObjectName("EndRide")
        EndRide.resize(326, 191)
        EndRide.setStyleSheet("* {background: #212121}\n"
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
                              "    font: 10pt \"Comic Sans MS\";\n"
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
                              "")
        self.centralwidget = QtWidgets.QWidget(EndRide)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_raiting = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_raiting.setFont(font)
        self.label_raiting.setStyleSheet("")
        self.label_raiting.setObjectName("label_raiting")
        self.gridLayout.addWidget(self.label_raiting, 0, 0, 1, 1)
        self.spinBox_raiting = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_raiting.setStyleSheet("")
        self.spinBox_raiting.setMaximum(5)
        self.spinBox_raiting.setObjectName("spinBox_raiting")
        self.gridLayout.addWidget(self.spinBox_raiting, 0, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
                                         "color: steelblue;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        EndRide.setCentralWidget(self.centralwidget)

        self.retranslateUi(EndRide)
        QtCore.QMetaObject.connectSlotsByName(EndRide)

    def retranslateUi(self, EndRide):
        _translate = QtCore.QCoreApplication.translate
        EndRide.setWindowTitle(_translate("EndRide", "Конец поездки"))
        self.label_raiting.setText(_translate("EndRide", "Рейтинг"))
        self.pushButton.setText(_translate("EndRide", "Подтвердить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    EndRide = QtWidgets.QMainWindow()
    ui = Ui_EndRide()
    ui.setupUi(EndRide)
    EndRide.show()
    sys.exit(app.exec_())
