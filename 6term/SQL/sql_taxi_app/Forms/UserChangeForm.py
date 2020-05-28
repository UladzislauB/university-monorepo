from PyQt5 import QtWidgets
from PyQt.py.UserChange import Ui_MainWindow


class UserChangeForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, login):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.login = login
        self.lbl_login.setText(f"Login - {login}")








