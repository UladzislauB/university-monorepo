from PyQt5 import QtWidgets

from Models.Gender import Gender
from PyQt.py.AddPassport import Ui_AddPassportWindow


class AddPassportForm(QtWidgets.QMainWindow, Ui_AddPassportWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.add_profile_form = None
        self.btn_add.clicked.connect(self.on_add)

    def get_gender(self):
        if self.rbtn_male.isChecked():
            return Gender.Male.value
        elif self.rbtn_female.isChecked():
            return Gender.Female.value
        else:
            return 0

    def open_profile_form(self):
        from Forms.ProfileForm import ProfileForm
        self.add_profile_form = ProfileForm(self.db, self.db.get_user(self.user.login))
        self.add_profile_form.show()
        self.close()

    def on_add(self):
        self.db.insert_passport(
            self.user.id,
            self.edit_series.text(),
            self.edit_number.text(),
            self.edit_identification_number.text(),
            self.get_gender(),
            self.edit_expiration_date.date().toString("yyyy-MM-dd"),
            self.edit_issue_date.date().toString("yyyy-MM-dd"),
        )
        self.open_profile_form()







