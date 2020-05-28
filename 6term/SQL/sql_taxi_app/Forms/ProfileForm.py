from PyQt5 import QtWidgets
from Forms.AddCarForm import AddCarForm
from Forms.AddPassportForm import AddPassportForm
from Forms.AdministrationForm import AdministrationForm
from Forms.HistoryForm import HistoryForm
from Forms.OrderForm import OrderForm
from Models.UserType import UserType
from PyQt.py.Profile import Ui_ProfileWindow


class ProfileForm(QtWidgets.QMainWindow, Ui_ProfileWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.add_car_form = None
        self.add_passport_form = None
        self.administration_form = None
        self.history_form = None
        self.order_form = None
        self.fill_user_properties(user)
        self.btn_history.clicked.connect(self.kek)
        self.edit_car.clicked.connect(self.open_add_car_form)
        self.edit_passport.clicked.connect(self.open_add_passport_form)
        self.btn_order.clicked.connect(self.open_order_form)
        self.btn_adminitration.clicked.connect(self.open_administration_form)
        self.btn_history.clicked.connect(self.open_history_form)

    def open_history_form(self):
        self.history_form = HistoryForm(self.db, self.user)
        self.history_form.show()
        self.close()

    def open_administration_form(self):
        self.administration_form = AdministrationForm(self.db, self.user)
        self.administration_form.show()
        self.close()

    def open_add_car_form(self):
        self.add_car_form = AddCarForm(self.db, self.user)
        self.add_car_form.show()
        self.close()

    def open_order_form(self):
        self.order_form = OrderForm(self.db, self.user)
        self.order_form.show()

    def open_add_passport_form(self):
        self.add_passport_form = AddPassportForm(self.db, self.user)
        self.add_passport_form.show()
        self.close()

    def kek(self):
        print(self.height())
        self.db.get_address(2)

    def fill_user_properties(self, user):
        self.edit_login.setText(user.login)
        self.edit_role.setText(user.role)
        self.edit_lastname.setText(user.name1)
        self.edit_firstname.setText(user.name2)
        self.edit_patronymic.setText(user.name3)

        if self.user.role == UserType.Client.value:
            self.btn_order.setVisible(True)
            self.driver_block.setVisible(False)
            self.btn_adminitration.setVisible(False)

        if self.user.role == UserType.Driver.value:
            self.btn_order.setVisible(False)
            self.btn_adminitration.setVisible(False)
            self.db.set_driver_status(
                self.user.login,
                'Online'
            )
        self.edit_rating.setText(f"{user.rating} star")
        if user.series is not None:
            text = f"{user.series}{user.number}"
            self.edit_passport.setText(text)
        if user.model is not None:
            text = f"{user.model} - {user.car_number}"
            self.edit_car.setText(text)

    def closeEvent(self, event):
        if self.user.role == UserType.Driver.value:
            self.db.set_driver_status(
                self.user.login,
                'Offline'
            )
        event.accept()



