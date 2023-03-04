import sys
from PyQt5 import QtWidgets, uic
import backend
from frontend_utilities import *





app = QtWidgets.QApplication(sys.argv)

# login_window = uic.loadUi("Ui/login.ui")

app_windows = {
    "login": uic.loadUi("Ui/login.ui"),
    "money_exchange": uic.loadUi("Ui/money_exchange.ui"),
    "money_withdraw": uic.loadUi("Ui/moneyWidrawl.ui"),
    "non_authorized": uic.loadUi("Ui/nonAutorized.ui"),
    "passwordnoauth": uic.loadUi("Ui/passwordnoautorized.ui"),
    "remove_user": uic.loadUi("Ui/remove_user.ui"),
    "start_day": uic.loadUi("Ui/start_day.ui"),
    "end_day": uic.loadUi("Ui/end_day.ui"),
    "popout_moneyex": uic.loadUi("Ui/popout_moneyEx.ui"),
    "transaction_complete": uic.loadUi("Ui/TransactionComplete.ui"),
    "transactions": uic.loadUi("Ui/transactions.ui"),
    "changepopout": uic.loadUi("Ui/changepopout.ui"),
    "authorized": uic.loadUi("Ui/autorized.ui"),
    "add_user": uic.loadUi("Ui/add_user.ui")
}




app_windows["login"].log_in_button.clicked.connect(
    lambda: login_sequence(app_windows["login"].username_fill.text(),
                           app_windows["login"].password_fill.text(),
                           app_windows))


app_windows["login"].show()


app.exec()
