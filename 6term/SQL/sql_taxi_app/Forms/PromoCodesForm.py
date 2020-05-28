from PyQt5 import QtWidgets

from Forms.AddPromoForm import AddPromoForm
from PyQt.py.Tariffs import Ui_TariffsWindow


class PromoCodesForm(QtWidgets.QMainWindow, Ui_TariffsWindow):
    def __init__(self, db, user):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.setWindowTitle('Promo codes')
        self.promo_codes = None
        self.add_promo_code_form = None
        self.table_fill()
        self.btn_add.clicked.connect(self.open_add_promo_form)

    def table_fill(self):
        self.promo_codes = self.db.get_all_promo_codes()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('Promo', 'Date', 'Discount'))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.promo_codes))
        i = 0
        for promo in self.promo_codes:
            self.insert_row(i, promo.promo , promo.expiration_date , promo.discount_percent)
            i = i + 1

    def insert_row(self, row_id, promo, date, discount):
        self.tableWidget.setItem(row_id, 0, QtWidgets.QTableWidgetItem(promo))
        self.tableWidget.setItem(row_id, 1, QtWidgets.QTableWidgetItem(str(date)))
        self.tableWidget.setItem(row_id, 2, QtWidgets.QTableWidgetItem(str(discount)))

    def open_add_promo_form(self):
        self.add_promo_code_form = AddPromoForm(self.db, self.user)
        self.add_promo_code_form.show()
