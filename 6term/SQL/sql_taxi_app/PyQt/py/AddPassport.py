# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddPassport.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPassportWindow(object):
    def setupUi(self, AddPassportWindow):
        AddPassportWindow.setObjectName("AddPassportWindow")
        AddPassportWindow.resize(439, 289)
        AddPassportWindow.setStyleSheet("* {background: #212121}\n"
                                        "QRadioButton{\n"
                                        "color: #b3b3b3;\n"
                                        "}\n"
                                        "QPushButton{\n"
                                        "color: white;\n"
                                        "background: #1db954;\n"
                                        "border-radius: 10px;\n"
                                        "font: 12pt \"Comic Sans MS\";\n"
                                        "}\n"
                                        "QLineEdit\n"
                                        "{\n"
                                        "background: transparent;\n"
                                        "border: none;\n"
                                        "border-bottom: 1px solid #1db954;\n"
                                        "font: 12pt \"Comic Sans MS\";\n"
                                        "}\n"
                                        "QLineEdit:focus {\n"
                                        " outline:none; }\n"
                                        "\n"
                                        "QLabel{\n"
                                        "    color: #b3b3b3;\n"
                                        "    transition: all 1s;\n"
                                        "    font: 14pt \"Comic Sans MS\";\n"
                                        "    font-weight:bold;\n"
                                        "}\n"
                                        "\n"
                                        "QDateEdit{\n"
                                        "background: transparent;\n"
                                        "border: none;\n"
                                        "font: 14pt \"Comic Sans MS\";\n"
                                        "color: #b3b3b3;\n"
                                        "}")
        self.centralwidget = QtWidgets.QWidget(AddPassportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_series = QtWidgets.QLabel(self.frame)
        self.label_series.setObjectName("label_series")
        self.gridLayout_2.addWidget(self.label_series, 0, 0, 1, 1)
        self.edit_series = QtWidgets.QLineEdit(self.frame)
        self.edit_series.setMaximumSize(QtCore.QSize(70, 16777215))
        self.edit_series.setObjectName("edit_series")
        self.gridLayout_2.addWidget(self.edit_series, 0, 1, 1, 1)
        self.label_number = QtWidgets.QLabel(self.frame)
        self.label_number.setObjectName("label_number")
        self.gridLayout_2.addWidget(self.label_number, 0, 2, 1, 2)
        self.edit_number = QtWidgets.QLineEdit(self.frame)
        self.edit_number.setObjectName("edit_number")
        self.gridLayout_2.addWidget(self.edit_number, 0, 5, 1, 1)
        self.label_identification_number = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_identification_number.setFont(font)
        self.label_identification_number.setStyleSheet("font-seize: 10px")
        self.label_identification_number.setObjectName("label_identification_number")
        self.gridLayout_2.addWidget(self.label_identification_number, 1, 0, 1, 3)
        self.edit_identification_number = QtWidgets.QLineEdit(self.frame)
        self.edit_identification_number.setObjectName("edit_identification_number")
        self.gridLayout_2.addWidget(self.edit_identification_number, 1, 3, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_gender = QtWidgets.QLabel(self.frame_2)
        self.label_gender.setObjectName("label_gender")
        self.gridLayout.addWidget(self.label_gender, 0, 0, 1, 1)
        self.rbtn_male = QtWidgets.QRadioButton(self.frame_2)
        self.rbtn_male.setChecked(True)
        self.rbtn_male.setObjectName("rbtn_male")
        self.gridLayout.addWidget(self.rbtn_male, 1, 0, 1, 1)
        self.rbtn_female = QtWidgets.QRadioButton(self.frame_2)
        self.rbtn_female.setObjectName("rbtn_female")
        self.gridLayout.addWidget(self.rbtn_female, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 5)
        self.label_issue_date = QtWidgets.QLabel(self.frame)
        self.label_issue_date.setObjectName("label_issue_date")
        self.gridLayout_2.addWidget(self.label_issue_date, 3, 0, 1, 2)
        self.edit_issue_date = QtWidgets.QDateEdit(self.frame)
        self.edit_issue_date.setObjectName("edit_issue_date")
        self.gridLayout_2.addWidget(self.edit_issue_date, 3, 4, 1, 2)
        self.label_expiration_date = QtWidgets.QLabel(self.frame)
        self.label_expiration_date.setObjectName("label_expiration_date")
        self.gridLayout_2.addWidget(self.label_expiration_date, 4, 0, 1, 3)
        self.edit_expiration_date = QtWidgets.QDateEdit(self.frame)
        self.edit_expiration_date.setObjectName("edit_expiration_date")
        self.gridLayout_2.addWidget(self.edit_expiration_date, 4, 4, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(181, 41))
        self.btn_add.setStyleSheet("")
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout.addWidget(self.btn_add)
        AddPassportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPassportWindow)
        QtCore.QMetaObject.connectSlotsByName(AddPassportWindow)

    def retranslateUi(self, AddPassportWindow):
        _translate = QtCore.QCoreApplication.translate
        AddPassportWindow.setWindowTitle(_translate("AddPassportWindow", "Добавить паспорт"))
        self.label_series.setText(_translate("AddPassportWindow", "Серия"))
        self.label_number.setText(_translate("AddPassportWindow", "Номер"))
        self.label_identification_number.setText(_translate("AddPassportWindow", "Идентификационный номер"))
        self.label_gender.setText(_translate("AddPassportWindow", "Пол"))
        self.rbtn_male.setText(_translate("AddPassportWindow", "Мужской"))
        self.rbtn_female.setText(_translate("AddPassportWindow", "Женский"))
        self.label_issue_date.setText(_translate("AddPassportWindow", "Дата выдачи"))
        self.label_expiration_date.setText(_translate("AddPassportWindow", "Срок действия"))
        self.btn_add.setText(_translate("AddPassportWindow", "Добавить"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddPassportWindow = QtWidgets.QMainWindow()
    ui = Ui_AddPassportWindow()
    ui.setupUi(AddPassportWindow)
    AddPassportWindow.show()
    sys.exit(app.exec_())
