from PyQt5 import QtWidgets
from PyQt.py.Error import Ui_ErrorDialog


class ErrorDialog(QtWidgets.QDialog, Ui_ErrorDialog):
    def __init__(self, text):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.plainTextEdit.insertPlainText(text)
