import math
import os
import random
import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from Forms.AddAdderssForm import AddAddressForm
from Forms.AddPayment import AddPaymentForm
from Forms.EndOrderForm import EndOrderForm
from Forms.ErrorDialog import ErrorDialog
from PyQt.py.Order import Ui_MainWindow


class OrderForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.img_locality.setPixmap(QPixmap(os.path.abspath("ico/locality.png")))
        self.img_payment.setPixmap(QPixmap(os.path.abspath("ico/credit-card.png")))
        self.btn_add.clicked.connect(self.open_add_payment_form)
        self.edit_from.clicked.connect(lambda: self.open_add_address_form(1))
        self.edit_to.clicked.connect(lambda: self.open_add_address_form(2))
        self.btn_submit.clicked.connect(self.on_submit)
        self.db = db
        self.user = user
        self.cards = self.db.get_cards(self.user.login)
        self.tariffs = self.db.get_tariffs()
        self.address_form = None
        self.address_to = None
        self.profile_form = None
        self.end_order_form = None
        self.add_payment_form = None
        self.add_address_form = None
        self.error_from = None
        self.fill_payment_cards()
        self.fill_tariffs()

    def fill_tariffs(self):
        self.comboBox_tarif.clear()
        self.tariffs = self.db.get_tariffs()
        for tariff in self.tariffs:
            self.comboBox_tarif.addItem(str(tariff.name))

    def fill_payment_cards(self):
        self.comboBox_payment.clear()
        self.cards = self.db.get_cards(self.user.login)
        for card in self.cards:
            self.comboBox_payment.addItem(str(card.card_number))

    def fill_address(self):
        if self.address_form is not None:
            a = self.address_form
            self.edit_from.setText(
                f"{a.street_type} {a.street} {a.house}-{a.flat}")
        if self.address_to is not None:
            a = self.address_to
            self.edit_to.setText(
                f"{a.street_type} {a.street} {a.house}-{a.flat}")

    def open_end_order_form(self, id_sale):
        self.end_order_form = EndOrderForm(self.db, self.user, id_sale)
        self.end_order_form.show()
        self.close()

    def open_add_payment_form(self):
        self.add_payment_form = AddPaymentForm(self.db, self.user, self)
        self.add_payment_form.show()

    def open_add_address_form(self, mode):
        self.add_address_form = AddAddressForm(self.db, self.user, mode, self)
        self.add_address_form.show()

    def on_submit(self):
        discount = 0
        if self.edit_promo.text():
            discount = self.db.check_promo(self.edit_promo.text())

        if discount >= 0:
            price = math.floor(random.randint(100, 150)*10)
            price = math.floor(price*(100-discount)/100)
            self.edit_price.setText(str(price))
            id_driver = self.db.get_free_driver()
            id_sale = self.db.order_taxi(
                self.user.login,
                id_driver,
                self.cards[self.comboBox_payment.currentIndex()].id,
                self.tariffs[self.comboBox_tarif.currentIndex()].id,
                price,
                self.address_form.id,
                self.address_to.id
            )
            self.open_end_order_form(id_sale)

        elif discount == -1:
            self.error_from = ErrorDialog("Promo code not found")
            self.error_from.show()
        elif discount == -2:
            self.error_from = ErrorDialog("The promo code has expired")
            self.error_from.show()









