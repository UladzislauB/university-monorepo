import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from Forms.ErrorDialog import ErrorDialog
from Forms.RegisterForm import RegisterForm
from Models.User import User
from PyQt.py.Login import Ui_LoginWindow
from Forms.ProfileForm import ProfileForm


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, db):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.img.setPixmap(QPixmap(os.path.abspath("ico/taxi.png")))
        self.db = db
        self.profile_form = None
        self.error_from = None
        self.register_form = None
        self.btn_register.clicked.connect(self.open_registration_form)
        self.btn_login.clicked.connect(self.login_user)

    def login_user(self):
        result = self.db.login_user(self.edit_login.text(), self.edit_password.text())
        if result == 0:
            user = self.db.get_user(self.edit_login.text())
            self.open_profile_form(user)
        elif result == 1:
            self.open_error_dialog('Wrong login or password')
        elif result == 2:
            self.open_error_dialog('User is blocked')

    def open_registration_form(self):
        self.register_form = RegisterForm(self.db)
        self.register_form.show()
        self.close()

    def open_profile_form(self, user):
        self.register_form = ProfileForm(self.db, user)
        self.register_form.show()
        self.close()

    def open_error_dialog(self, text):
        self.error_from = ErrorDialog(text)
        self.error_from.show()
