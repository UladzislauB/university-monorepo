from PyQt5 import QtWidgets
from PyQt.py.AddPromo import Ui_AddPromoWindow


class AddPromoForm(QtWidgets.QMainWindow, Ui_AddPromoWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.btn_add.clicked.connect(self.insert_promo_code)

    def insert_promo_code(self):
        self.db.insert_tariff(
            self.lineEdit.text(),
            self.dateEdit_expires.date().toString("yyyy-MM-dd"),
            self.spinBox_discount.text()
        )
        self.close()
