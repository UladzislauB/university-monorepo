import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from PyQt.py.AddCar import Ui_AddCarWindow


class AddCarForm(QtWidgets.QMainWindow, Ui_AddCarWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.add_profile_form = None
        self.img.setPixmap(QPixmap(os.path.abspath("ico/car.png")))
        self.btn_add.clicked.connect(self.on_add)

    def on_add(self):
        self.db.insert_car(
            self.user.id,
            self.edit_model.text(),
            self.edit_number.text()
        )
        self.open_profile_form()

    def open_profile_form(self):
        from Forms.ProfileForm import ProfileForm
        self.add_profile_form = ProfileForm(self.db, self.db.get_user(self.user.login))
        self.add_profile_form.show()
        self.close()





