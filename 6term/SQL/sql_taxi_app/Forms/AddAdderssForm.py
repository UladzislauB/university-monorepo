from PyQt5 import QtWidgets

from Models.CityType import CityType
from Models.StreetType import StreetType
from PyQt.py.AddAddress import Ui_AddAddressWindow


class AddAddressForm(QtWidgets.QMainWindow, Ui_AddAddressWindow):
    def __init__(self, db, user, mode, order_form):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.mode = mode
        self.order_form = order_form
        self.btn_add.clicked.connect(self.on_add)
        self.fill_combo_boxes()

    def fill_combo_boxes(self):
        for street in StreetType:
            self.comboBox_street_type.addItem(street.value)
        for city in CityType:
            self.comboBox_city_type.addItem(city.value)

    def on_add(self):

        #address = self.db.get_address(id)
        if self.mode == 1:
            self.order_form.address_form = self.db.get_address(5)
        else:
            self.order_form.address_to = self.db.get_address(6)

        self.order_form.fill_address()
        self.close()












