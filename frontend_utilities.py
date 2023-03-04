import backend
import utilities

def connect_buttons(window):
    pass

def login_sequence(username, password, window):
    window["login"].warning_label.hide()
    
    if not backend.login(username, password):
        window["login"].warning_label.setText("INVALID CREDENTIALS")
        window["login"].warning_label.setStyleSheet("QLabel {color : red; }")
        window["login"].warning_label.show()
        
    else:
        window["login"].hide()
        # TODO: Add logic for authorized users vs unauthorized
        session_start_unauthorized(
            utilities.get_full_name_by_username(username), window)

def session_start_unauthorized(name, window):
    window["non_authorized"].show()
    window["non_authorized"].username_label.setText(name)


