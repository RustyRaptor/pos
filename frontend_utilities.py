import backend
def login_sequence(x, username, password, window):
    print(username)
    if not backend.login(username, password):
        window["login"].warning_label.setText("INVALID CREDENTIALS")
        window["login"].warning_label.setStyleSheet("QLabel {color : red; }")
        window["login"].warning_label.show()
        
    else:
        window["login"].hide()
        window["non_authorized"].show()
    

