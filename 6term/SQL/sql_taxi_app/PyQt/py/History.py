# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        HistoryWindow.setObjectName("HistoryWindow")
        HistoryWindow.resize(653, 320)
        HistoryWindow.setStyleSheet("* {background: #212121}\n"
                                    "QLabel{\n"
                                    "    color:  #b3b3b3;\n"
                                    "    font: 16pt \"Comic Sans MS\";\n"
                                    "    font-weight:bold;\n"
                                    "}")
        self.centralwidget = QtWidgets.QWidget(HistoryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayout.addWidget(self.lbl_title, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        HistoryWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HistoryWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryWindow)

    def retranslateUi(self, HistoryWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryWindow.setWindowTitle(_translate("HistoryWindow", "История"))
        self.lbl_title.setText(_translate("HistoryWindow", "История поездок"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HistoryWindow = QtWidgets.QMainWindow()
    ui = Ui_HistoryWindow()
    ui.setupUi(HistoryWindow)
    HistoryWindow.show()
    sys.exit(app.exec_())
