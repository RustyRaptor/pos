import backend
import utilities

def connect_buttons(window):
    window["login"].log_in_button.clicked.connect(
    lambda: login_button(window["login"].username_fill.text(),
                           window["login"].password_fill.text(),
                           window))
    return window

def login_sequence(window):
    window["login"].show()
    
    window["login"].warning_label.hide()
    window["login"].warning_label.setText("INVALID CREDENTIALS")
    window["login"].warning_label.setStyleSheet("QLabel {color : red; }")

def login_button(username, password, window):
    if not backend.login(username, password):
        window["login"].warning_label.show()
        
    else:
        window["login"].hide()
        # TODO: Add logic for authorized users vs unauthorized
        session_start_unauthorized(
            utilities.get_full_name_by_username(username), window)

def session_start_unauthorized(name, window):
    window["non_authorized"].show()
    window["non_authorized"].username_label.setText(name)


