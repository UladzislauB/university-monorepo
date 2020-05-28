from PyQt5 import QtWidgets
from PyQt.py.AddTariff import Ui_AddTariffWindow


class AddTariffForm(QtWidgets.QMainWindow, Ui_AddTariffWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.btn_add.clicked.connect(self.insert_tariff)

    def insert_tariff(self):
        self.db.insert_tariff(
            self.edit_name.text(),
            str(self.spinBox_city.text()),
            str(self.spinBox_no_city.text())
        )
        self.close()
