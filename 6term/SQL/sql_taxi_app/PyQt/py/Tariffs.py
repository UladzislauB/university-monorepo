# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tariffs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TariffsWindow(object):
    def setupUi(self, TariffsWindow):
        TariffsWindow.setObjectName("TariffsWindow")
        TariffsWindow.resize(287, 320)
        TariffsWindow.setStyleSheet("* {background: #212121}\n"
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
                                    "QHeaderView::section {\n"
                                    "color:#b3b3b3;\n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "color: white;\n"
                                    "background: #1db954;\n"
                                    "border-radius: 5px;\n"
                                    "font: 12pt \"Comic Sans MS\";\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.centralwidget = QtWidgets.QWidget(TariffsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        TariffsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TariffsWindow)
        QtCore.QMetaObject.connectSlotsByName(TariffsWindow)

    def retranslateUi(self, TariffsWindow):
        _translate = QtCore.QCoreApplication.translate
        TariffsWindow.setWindowTitle(_translate("TariffsWindow", "Промокоды"))
        self.btn_add.setText(_translate("TariffsWindow", "Добавить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TariffsWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TariffsWindow", "Истекает"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TariffsWindow", "Скидка"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TariffsWindow = QtWidgets.QMainWindow()
    ui = Ui_TariffsWindow()
    ui.setupUi(TariffsWindow)
    TariffsWindow.show()
    sys.exit(app.exec_())