# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAddress.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddAddressWindow(object):
    def setupUi(self, AddAddressWindow):
        AddAddressWindow.setObjectName("AddAddressWindow")
        AddAddressWindow.resize(352, 369)
        AddAddressWindow.setStyleSheet("\n"
                                       "*{\n"
                                       "background: #212121;\n"
                                       "}\n"
                                       "\n")
        self.centralwidget = QtWidgets.QWidget(AddAddressWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QLineEdit\n"
                                 "{\n"
                                 "background: transparent;\n"
                                 "border: none;\n"
                                 "border-bottom: 1px solid 	#1db954;\n"
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
                                 "    color: #b3b3b3;\n"
                                 "    transition: all 1s;\n"
                                 "    font: 10pt;\n"
                                 "    font-weight:bold;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "QComboBox{\n"
                                 "background: #535353;\n"
                                 "border: none;\n"
                                 "border-bottom: 1px solid 	#1db954;\n"
                                 "font: 12pt \"Comic Sans MS\";\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(5000, 5000))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_country = QtWidgets.QLabel(self.frame_3)
        self.label_country.setObjectName("label_country")
        self.gridLayout.addWidget(self.label_country, 0, 0, 1, 1)
        self.lbl_city_typ = QtWidgets.QLabel(self.frame_3)
        self.lbl_city_typ.setObjectName("lbl_city_typ")
        self.gridLayout.addWidget(self.lbl_city_typ, 1, 0, 1, 1)
        self.comboBox_city_type = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_city_type.setMaximumSize(QtCore.QSize(500, 30))
        self.comboBox_city_type.setStyleSheet("")
        self.comboBox_city_type.setObjectName("comboBox_city_type")
        self.gridLayout.addWidget(self.comboBox_city_type, 1, 1, 1, 1)
        self.label_city = QtWidgets.QLabel(self.frame_3)
        self.label_city.setObjectName("label_city")
        self.gridLayout.addWidget(self.label_city, 2, 0, 1, 1)
        self.edit_city = QtWidgets.QLineEdit(self.frame_3)
        self.edit_city.setObjectName("edit_city")
        self.gridLayout.addWidget(self.edit_city, 2, 1, 1, 1)
        self.label_region = QtWidgets.QLabel(self.frame_3)
        self.label_region.setObjectName("label_region")
        self.gridLayout.addWidget(self.label_region, 3, 0, 1, 1)
        self.edit_region = QtWidgets.QLineEdit(self.frame_3)
        self.edit_region.setObjectName("edit_region")
        self.gridLayout.addWidget(self.edit_region, 3, 1, 1, 1)
        self.label_district = QtWidgets.QLabel(self.frame_3)
        self.label_district.setObjectName("label_district")
        self.gridLayout.addWidget(self.label_district, 4, 0, 1, 1)
        self.edit_district = QtWidgets.QLineEdit(self.frame_3)
        self.edit_district.setObjectName("edit_district")
        self.gridLayout.addWidget(self.edit_district, 4, 1, 1, 1)
        self.lbl_street_type = QtWidgets.QLabel(self.frame_3)
        self.lbl_street_type.setObjectName("lbl_street_type")
        self.gridLayout.addWidget(self.lbl_street_type, 5, 0, 1, 1)
        self.comboBox_street_type = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_street_type.setMaximumSize(QtCore.QSize(3000, 20))
        self.comboBox_street_type.setStyleSheet("QComboBox::drop-down \n"
                                                "{\n"
                                                "    border: 0px;\n"
                                                "}")
        self.comboBox_street_type.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_street_type.setIconSize(QtCore.QSize(15, 15))
        self.comboBox_street_type.setFrame(True)
        self.comboBox_street_type.setModelColumn(0)
        self.comboBox_street_type.setObjectName("comboBox_street_type")
        self.gridLayout.addWidget(self.comboBox_street_type, 5, 1, 1, 1)
        self.lbl_street = QtWidgets.QLabel(self.frame_3)
        self.lbl_street.setObjectName("lbl_street")
        self.gridLayout.addWidget(self.lbl_street, 6, 0, 1, 1)
        self.edit_street = QtWidgets.QLineEdit(self.frame_3)
        self.edit_street.setObjectName("edit_street")
        self.gridLayout.addWidget(self.edit_street, 6, 1, 1, 1)
        self.edit_country = QtWidgets.QLineEdit(self.frame_3)
        self.edit_country.setText("")
        self.edit_country.setObjectName("edit_country")
        self.gridLayout.addWidget(self.edit_country, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 71))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_house = QtWidgets.QLabel(self.frame_2)
        self.lbl_house.setObjectName("lbl_house")
        self.horizontalLayout.addWidget(self.lbl_house)
        self.edit_house = QtWidgets.QLineEdit(self.frame_2)
        self.edit_house.setObjectName("edit_house")
        self.horizontalLayout.addWidget(self.edit_house)
        self.lbl_building = QtWidgets.QLabel(self.frame_2)
        self.lbl_building.setObjectName("lbl_building")
        self.horizontalLayout.addWidget(self.lbl_building)
        self.edit_building = QtWidgets.QLineEdit(self.frame_2)
        self.edit_building.setObjectName("edit_building")
        self.horizontalLayout.addWidget(self.edit_building)
        self.lbl_flat = QtWidgets.QLabel(self.frame_2)
        self.lbl_flat.setObjectName("lbl_flat")
        self.horizontalLayout.addWidget(self.lbl_flat)
        self.edit_flat = QtWidgets.QLineEdit(self.frame_2)
        self.edit_flat.setObjectName("edit_flat")
        self.horizontalLayout.addWidget(self.edit_flat)
        self.verticalLayout.addWidget(self.frame_2)
        self.btn_add = QtWidgets.QPushButton(self.frame)
        self.btn_add.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_add.setStyleSheet("QPushButton{\n"
                                   "color:  white;\n"
                                   "background: #1db954;\n"
                                   "border-radius: 10px;\n"
                                   "font: 12pt;\n"
                                   "}")
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        self.verticalLayout_2.addWidget(self.frame)
        AddAddressWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddAddressWindow)
        QtCore.QMetaObject.connectSlotsByName(AddAddressWindow)

    def retranslateUi(self, AddAddressWindow):
        _translate = QtCore.QCoreApplication.translate
        AddAddressWindow.setWindowTitle(_translate("AddAddressWindow", "Адрес"))
        self.label_country.setText(_translate("AddAddressWindow", "Страна"))
        self.label_region.setText(_translate("AddAddressWindow", "Область"))
        self.lbl_city_typ.setText(_translate("AddAddressWindow", "Тип города"))
        self.label_city.setText(_translate("AddAddressWindow", "Город"))
        self.label_district.setText(_translate("AddAddressWindow", "Район"))
        self.lbl_street_type.setText(_translate("AddAddressWindow", "Тип улицы"))
        self.lbl_street.setText(_translate("AddAddressWindow", "Улица"))
        self.lbl_house.setText(_translate("AddAddressWindow", "Дом"))
        self.lbl_building.setText(_translate("AddAddressWindow", "Корпус"))
        self.lbl_flat.setText(_translate("AddAddressWindow", "Квартира"))
        self.btn_add.setText(_translate("AddAddressWindow", "Добавить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddAddressWindow = QtWidgets.QMainWindow()
    ui = Ui_AddAddressWindow()
    ui.setupUi(AddAddressWindow)
    AddAddressWindow.show()
    sys.exit(app.exec_())
