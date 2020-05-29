# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorDialog(object):
    def setupUi(self, ErrorDialog):
        ErrorDialog.setObjectName("ErrorDialog")
        ErrorDialog.resize(291, 104)
        ErrorDialog.setStyleSheet("* {background: #212121}\n")
        self.horizontalLayout = QtWidgets.QHBoxLayout(ErrorDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(ErrorDialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
                                         "color: #b3b3b3;")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(ErrorDialog)
        self.buttonBox.setStyleSheet("QPushButton{\n"
                                     "color: white;\n"
                                     "background: #1db954;\n"
                                     "border-radius: 5px;\n"
                                     "font: 12pt \"Comic Sans MS\";\n"
                                     "width: 70px;\n"
                                     "}")
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ErrorDialog)
        self.buttonBox.accepted.connect(ErrorDialog.accept)
        self.buttonBox.rejected.connect(ErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ErrorDialog)

    def retranslateUi(self, ErrorDialog):
        _translate = QtCore.QCoreApplication.translate
        ErrorDialog.setWindowTitle(_translate("ErrorDialog", "Error"))
        self.plainTextEdit.setPlainText(_translate("DialogError", "Промокод не существует"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ErrorDialog = QtWidgets.QDialog()
    ui = Ui_ErrorDialog()
    ui.setupUi(ErrorDialog)
    ErrorDialog.show()
    sys.exit(app.exec_())
