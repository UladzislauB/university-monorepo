from PyQt5 import QtWidgets

from Forms.PromoCodesForm import PromoCodesForm
from Forms.TariffsForm import TariffsForm
from Forms.UserChangeForm import UserChangeForm
from Models.UserStatus import UserStatus
from Models.UserType import UserType
from PyQt.py.Administration import Ui_AdministrationWindow


class AdministrationForm(QtWidgets.QMainWindow, Ui_AdministrationWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.users = None
        self.tariffs_form = None
        self.promo_codes_form = None
        self.table_fill()
        self.btn_add_tarif.clicked.connect(self.open_tariffs_form)
        self.btn_promo_codes.clicked.connect(self.open_promo_codes_form)
        self.rBtn_driver.clicked.connect(self.table_fill)
        self.rBtn_all.clicked.connect(self.table_fill)
        self.rBtn_client.clicked.connect(self.table_fill)
        self.rBtn_admin.clicked.connect(self.table_fill)
        self.rBtn_Active_2.clicked.connect(self.table_fill)
        self.rBtn_Blocked.clicked.connect(self.table_fill)
        self.rBtn_all_2.clicked.connect(self.table_fill)
        self.tableWidget.clicked.connect(self.view_clicked)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)


    def open_promo_codes_form(self):
        self.promo_codes_form = PromoCodesForm(self.db, self.user)
        self.promo_codes_form.show()

    def open_tariffs_form(self):
        self.tariffs_form = TariffsForm(self.db, self.user)
        self.tariffs_form.show()

    def table_fill(self):
        self.users = self.db.get_all_user(
            self.edit_name1.text(),
            self.edit_name2.text(),
            self.edit_name3.text(),
            self.get_user_type(),
            self.get_user_status()
        )
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(('Login', 'Role', 'Name 1', 'Name 2', 'Name 3', 'Status'))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.users))
        i = 0
        for user in self.users:
            self.insert_row(i, user.login, user.role, user.status, user.name1, user.name2, user.name3)
            i = i + 1

    def insert_row(self, row_id, login, role, status, name1, name2, name3):
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(login))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(role))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(name1))
        self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(name2))
        self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(name3))
        self.tableWidget.setItem(row_id, 5, QtWidgets.QTableWidgetItem(status))

    def get_user_type(self):
        if self.rBtn_admin.isChecked():
            return UserType.Admin.value
        elif self.rBtn_client.isChecked():
            return UserType.Client.value
        elif self.rBtn_driver.isChecked():
            return UserType.Driver.value
        elif self.rBtn_all.isChecked():
            return UserType.All.value

    def get_user_status(self):
        if self.rBtn_Active_2.isChecked():
            return UserStatus.Active.value
        elif self.rBtn_Blocked.isChecked():
            return UserStatus.Blocked.value
        elif self.rBtn_all_2.isChecked():
            return UserStatus.All.value

    def view_clicked(self):
        indexes = self.tableWidget.selectionModel().selectedRows()
        id_row = indexes[0].row()
        login = self.tableWidget.item(id_row, 0).text()
        self.user_change_form = UserChangeForm(self.db, login)
        self.user_change_form.show()
