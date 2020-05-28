from PyQt5 import QtWidgets

from Forms.AddTariffForm import AddTariffForm
from PyQt.py.Tariffs import Ui_TariffsWindow


class TariffsForm(QtWidgets.QMainWindow, Ui_TariffsWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.tariffs = None
        self.add_tariff_form = None
        self.table_fill()
        self.btn_add.clicked.connect(self.open_add_tariff_form)

    def open_add_tariff_form(self):
        self.add_tariff_form = AddTariffForm(self.db, self.user)
        self.add_tariff_form.show()

    def table_fill(self):
        self.tariffs = self.db.get_all_tariffs()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('Name', 'City', 'No City'))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.tariffs))
        i = 0
        for tariff in self.tariffs:
            self.insert_row(i, tariff.name, tariff.city, tariff.no_city)
            i = i + 1

    def insert_row(self, row_id, name, city, no_city):
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(name))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(city)))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(no_city)))

