# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserChange.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(404, 137)
        MainWindow.setStyleSheet("* {background: #212121}\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "background: transparent;\n"
                                 "border: none;\n"
                                 "border-bottom: 1px solid steelblue;\n"
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
                                 "border-bottom: 1px solid steelblue;\n"
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
                                 "QComboBox{\n"
                                 "background: transparent;\n"
                                 "border: none;\n"
                                 "border-bottom: 1px solid steelblue;\n"
                                 "font: 12pt \"Comic Sans MS\";\n"
                                 "}\n"
                                 "\n"
                                 "QDateEdit{\n"
                                 "background: transparent;\n"
                                 "border: none;\n"
                                 "font: 14pt \"Comic Sans MS\";\n"
                                 "color: #b3b3b3;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setMinimumSize(QtCore.QSize(0, 23))
        self.lbl_login.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout_2.addWidget(self.lbl_login, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_unlock = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_unlock.setObjectName("btn_unlock")
        self.gridLayout.addWidget(self.btn_unlock, 0, 0, 1, 1)
        self.btn_lock = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_lock.setObjectName("btn_lock")
        self.gridLayout.addWidget(self.btn_lock, 0, 1, 1, 1)
        self.btn_time_block = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_time_block.setObjectName("btn_time_block")
        self.gridLayout.addWidget(self.btn_time_block, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_apply = QtWidgets.QPushButton(self.groupBox)
        self.btn_apply.setObjectName("btn_apply")
        self.horizontalLayout.addWidget(self.btn_apply)
        self.comboBox_userType = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_userType.setObjectName("comboBox_userType")
        self.comboBox_userType.addItem("")
        self.comboBox_userType.addItem("")
        self.comboBox_userType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_userType)
        self.gridLayout_2.addWidget(self.groupBox, 1, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_2.addWidget(self.btn_delete, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конфигурация"))
        self.lbl_login.setText(_translate("MainWindow", "Юзернейм - UladBlr"))
        self.groupBox_2.setTitle(_translate("MainWindow", ""))
        self.btn_unlock.setText(_translate("MainWindow", "Разблокировать"))
        self.btn_lock.setText(_translate("MainWindow", "Блокировать"))
        self.btn_time_block.setText(_translate("MainWindow", "Block untill"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.btn_apply.setText(_translate("MainWindow", "Apply"))
        self.comboBox_userType.setItemText(0, _translate("MainWindow", "Клиент"))
        self.comboBox_userType.setItemText(1, _translate("MainWindow", "Провайдер"))
        self.comboBox_userType.setItemText(2, _translate("MainWindow", "Админ"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить пользователя"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
