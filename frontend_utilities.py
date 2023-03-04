import backend

def login_sequence(username, password, window):
    window["login"].warning_label.hide()
    
    if not backend.login(username, password):
        window["login"].warning_label.setText("INVALID CREDENTIALS")
        window["login"].warning_label.setStyleSheet("QLabel {color : red; }")
        window["login"].warning_label.show()
        
    else:
        window["login"].hide()
        window["non_authorized"].show()


