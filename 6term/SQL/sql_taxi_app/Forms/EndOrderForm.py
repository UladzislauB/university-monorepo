import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from PyQt.py.EndRide import Ui_EndRide


class EndOrderForm(QtWidgets.QMainWindow, Ui_EndRide):
    def __init__(self, db, user, id_sale):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = db
        self.user = user
        self.id_sale = id_sale
        self.pushButton.clicked.connect(self.on_submit)

    def on_submit(self):
        self.db.end_order_taxi(
            self.id_sale,
            self.plainTextEdit.toPlainText(),
            int(self.spinBox_raiting.text())
        )
        self.close()









