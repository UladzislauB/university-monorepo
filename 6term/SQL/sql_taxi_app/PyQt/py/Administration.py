# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Administration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdministrationWindow(object):
    def setupUi(self, AdministrationWindow):
        AdministrationWindow.setObjectName("AdministrationWindow")
        AdministrationWindow.resize(678, 521)
        AdministrationWindow.setStyleSheet("QLineEdit\n"
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
                                           "    color: steelblue;\n"
                                           "    font: 16pt \"Comic Sans MS\";\n"
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
                                           "background: steelblue;\n"
                                           "border-radius: 60px;\n"
                                           "font: 12pt \"Comic Sans MS\";\n"
                                           "}\n"
                                           "\n"
                                           "")
        self.centralwidget = QtWidgets.QWidget(AdministrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.tableWidget, 4, 0, 1, 3)
        self.BoxFullName = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxFullName.setStyleSheet("")
        self.BoxFullName.setObjectName("BoxFullName")
        self.gridLayout = QtWidgets.QGridLayout(self.BoxFullName)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_name2 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_name2.setFont(font)
        self.lbl_name2.setObjectName("lbl_name2")
        self.gridLayout.addWidget(self.lbl_name2, 0, 0, 1, 1)
        self.edit_name2 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name2.setObjectName("edit_name2")
        self.gridLayout.addWidget(self.edit_name2, 0, 1, 1, 1)
        self.lbl_name1 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_name1.setFont(font)
        self.lbl_name1.setObjectName("lbl_name1")
        self.gridLayout.addWidget(self.lbl_name1, 1, 0, 1, 1)
        self.edit_name1 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name1.setObjectName("edit_name1")
        self.gridLayout.addWidget(self.edit_name1, 1, 1, 1, 1)
        self.lbl_name3 = QtWidgets.QLabel(self.BoxFullName)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_name3.setFont(font)
        self.lbl_name3.setObjectName("lbl_name3")
        self.gridLayout.addWidget(self.lbl_name3, 2, 0, 1, 1)
        self.edit_name3 = QtWidgets.QLineEdit(self.BoxFullName)
        self.edit_name3.setObjectName("edit_name3")
        self.gridLayout.addWidget(self.edit_name3, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.BoxFullName, 5, 0, 2, 1)
        self.btn_add_tarif = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_tarif.setObjectName("btn_add_tarif")
        self.gridLayout_2.addWidget(self.btn_add_tarif, 1, 2, 1, 1)
        self.btn_undo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_undo.setObjectName("btn_undo")
        self.gridLayout_2.addWidget(self.btn_undo, 6, 2, 1, 1)
        self.btn_find = QtWidgets.QPushButton(self.centralwidget)
        self.btn_find.setObjectName("btn_find")
        self.gridLayout_2.addWidget(self.btn_find, 6, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rBtn_Blocked = QtWidgets.QRadioButton(self.groupBox)
        self.rBtn_Blocked.setObjectName("rBtn_Blocked")
        self.horizontalLayout_2.addWidget(self.rBtn_Blocked)
        self.rBtn_Active_2 = QtWidgets.QRadioButton(self.groupBox)
        self.rBtn_Active_2.setObjectName("rBtn_Active_2")
        self.horizontalLayout_2.addWidget(self.rBtn_Active_2)
        self.rBtn_all_2 = QtWidgets.QRadioButton(self.groupBox)
        self.rBtn_all_2.setChecked(True)
        self.rBtn_all_2.setObjectName("rBtn_all_2")
        self.horizontalLayout_2.addWidget(self.rBtn_all_2)
        self.gridLayout_2.addWidget(self.groupBox, 5, 1, 1, 2, QtCore.Qt.AlignTop)
        self.BoxUserType = QtWidgets.QGroupBox(self.centralwidget)
        self.BoxUserType.setObjectName("BoxUserType")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BoxUserType)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rBtn_admin = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_admin.setObjectName("rBtn_admin")
        self.horizontalLayout.addWidget(self.rBtn_admin)
        self.rBtn_driver = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_driver.setObjectName("rBtn_driver")
        self.horizontalLayout.addWidget(self.rBtn_driver)
        self.rBtn_client = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_client.setObjectName("rBtn_client")
        self.horizontalLayout.addWidget(self.rBtn_client)
        self.rBtn_all = QtWidgets.QRadioButton(self.BoxUserType)
        self.rBtn_all.setChecked(True)
        self.rBtn_all.setObjectName("rBtn_all")
        self.horizontalLayout.addWidget(self.rBtn_all)
        self.gridLayout_2.addWidget(self.BoxUserType, 1, 0, 2, 2)
        self.btn_promo_codes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_promo_codes.setObjectName("btn_promo_codes")
        self.gridLayout_2.addWidget(self.btn_promo_codes, 2, 2, 1, 1)
        AdministrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdministrationWindow)
        QtCore.QMetaObject.connectSlotsByName(AdministrationWindow)

    def retranslateUi(self, AdministrationWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministrationWindow.setWindowTitle(_translate("AdministrationWindow", "Administration"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AdministrationWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("AdministrationWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AdministrationWindow", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AdministrationWindow", "Role"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AdministrationWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AdministrationWindow", "Patronymic "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("AdministrationWindow", "Lsat Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("AdministrationWindow", "Status"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.BoxFullName.setTitle(_translate("AdministrationWindow", "Full Name"))
        self.lbl_name2.setText(_translate("AdministrationWindow", "First name"))
        self.lbl_name1.setText(_translate("AdministrationWindow", "Last name"))
        self.lbl_name3.setText(_translate("AdministrationWindow", "Patronymic"))
        self.btn_add_tarif.setText(_translate("AdministrationWindow", "Tariffs"))
        self.btn_undo.setText(_translate("AdministrationWindow", "Undo"))
        self.btn_find.setText(_translate("AdministrationWindow", "Find"))
        self.groupBox.setTitle(_translate("AdministrationWindow", "User Status"))
        self.rBtn_Blocked.setText(_translate("AdministrationWindow", "Blocked"))
        self.rBtn_Active_2.setText(_translate("AdministrationWindow", "Active"))
        self.rBtn_all_2.setText(_translate("AdministrationWindow", "All"))
        self.BoxUserType.setTitle(_translate("AdministrationWindow", "User Type"))
        self.rBtn_admin.setText(_translate("AdministrationWindow", "Admin"))
        self.rBtn_driver.setText(_translate("AdministrationWindow", "Driver"))
        self.rBtn_client.setText(_translate("AdministrationWindow", "Client"))
        self.rBtn_all.setText(_translate("AdministrationWindow", "All"))
        self.btn_promo_codes.setText(_translate("AdministrationWindow", "Promo"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AdministrationWindow = QtWidgets.QMainWindow()
    ui = Ui_AdministrationWindow()
    ui.setupUi(AdministrationWindow)
    AdministrationWindow.show()
    sys.exit(app.exec_())
