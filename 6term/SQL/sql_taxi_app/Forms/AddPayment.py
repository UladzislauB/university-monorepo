import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from PyQt.py.AddPayment import Ui_AddPaymentWindow


class AddPaymentForm(QtWidgets.QMainWindow, Ui_AddPaymentWindow):
    def __init__(self, db, user, order_form):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.img_payment.setPixmap(QPixmap(os.path.abspath("ico/card.png")))
        self.db = db
        self.user = user
        self.order_form = order_form
        self.btn_add.clicked.connect(self.on_add)

    def on_add(self):
        self.db.insert_card(
            self.user.login,
            self.edit_card_holder.text(),
            self.edit_card_number.text(),
            self.dateEdit_expiration_date.date().toString("yyyy-MM-dd"),
            self.edit_security_code.text()
        )
        print(self.user.login)
        self.order_form.fill_payment_cards()
        self.close()








