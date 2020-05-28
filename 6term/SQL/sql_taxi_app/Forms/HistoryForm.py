from PyQt5 import QtWidgets
from PyQt.py.History import Ui_HistoryWindow


class HistoryForm(QtWidgets.QMainWindow, Ui_HistoryWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.sales = None
        self.lbl_title.setText(f"{user.login} - History")
        self.db.get_history(user.login)
        self.table_fill()

    def table_fill(self):
        self.sales = self.db.get_history(self.user.login)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(('From', 'To', 'Date begin', 'Date End', 'Cost', 'Name'))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.sales))
        i = 0
        for sale in self.sales:
            self.insert_row(i, sale.id_address_from, sale.id_address_to, sale.date
                            , sale.date1, sale.cost, sale.name2)
            i = i + 1

    def insert_row(self, row_id, address_from, address_to, date_begin, date_end, cost, name):
        a_from = self.db.get_address(address_from)
        a_to = self.db.get_address(address_to)
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(f"{a_from.street_type} {a_from.street} {a_from.house}-{a_from.flat}"))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(f"{a_to.street_type} {a_to.street} {a_to.house}-{a_to.flat}"))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(date_begin)))
        self.tableWidget.setItem(row_id, 3, QtWidgets.QTableWidgetItem(str(date_end)))
        self.tableWidget.setItem(row_id, 4, QtWidgets.QTableWidgetItem(str(cost)))
        self.tableWidget.setItem(row_id, 5, QtWidgets.QTableWidgetItem(name))

