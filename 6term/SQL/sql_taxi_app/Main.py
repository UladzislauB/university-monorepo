# python -m PyQt5.uic.pyuic -x History.ui -o History.py
from PyQt5 import QtWidgets
from Forms.LoginForm import LoginWindow
from Service.DBHelper import DBHelper


def main():
    my_db = DBHelper()
    my_db.cursor.execute('SET GLOBAL event_scheduler=ON')
    my_db.connect.commit()
    app = QtWidgets.QApplication([])
    window = LoginWindow(my_db)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


