from utilities import *


# Read user and password from user imput and check credentials with the csv file
def login(user, password):
    if (user, password) in [user for user in get_users()]:
        return True
    return False


# Misssing the recording of transaction to process funcitons
# Computes calculations of owe moeny and returns the ammout of money to be returned after customer pay
# and record te transaction into the csv file

def compute_money_owed(money_owed, money_from_Customer, money_returned):
    if money_from_Customer >= money_owed:
        money_returned = money_from_Customer - money_owed

        return money_returned

    return False  # Replace with an error to the screen notifing the customer that he needs to pay more money


# nonautorized widrawl function
# This function will be used to record the ammount of money and the reason for the widrawl with current
# date and time of the widrawl recorded into the csv fil into a csv file


def nonautorized_widrawl(withdrawal, reason):
    write_csv_row([withdrawal, reason, generate_timestamp()],
                  'csv_database/endofdayreports.csv')
    return True

# startday funciton
# This function will grab the ammount of money that was set by admin that the register will have from the beggining of the day


def start_day(starting_money):
    write_csv_row([starting_money],
                  'csv_database/currentmoney_' + generate_date_only_stamp())

    write_csv_row([starting_money, generate_date_only_stamp()],
                  'csv_database/startofdayreports.csv')

    return True  # Replace with a message to the screen saying that the set money was recorded and trake to the main screen

# endday function
# This function will close the reigser recording into the csv file the ammount of money that was left in the register
# This funciton is not complete


def end_day(money_left):
    write_csv_row([money_left, generate_date_only_stamp()],
                  'csv_database/endofdayreports.csv')


# Check if admin has logged the start of workday and we havent closed yet
def check_start_ammount():
    if start_entry_exists() and not end_entry_exists():
        return True
    return False


# EXAMPLE OF THE CSV FILE
# START MONEY AMMOUNT , DATE , END  MONEY AMMOUNT , DATE
# 2000 , 10-30-2020 , 3452 , 10 - 30 - 2020 # THE RECORD TRANSACTION WILL NOT WORK
# 2000  , 10- 30 -2020  # The record transaction button will work
# None # The record transaction button will not work

def open_cash_register():
    set_register_open(True)


def register_is_open():
    filename = 'csv_database/register_status.csv'
    status_code = [status for status in get_rows(filename)][-1][0]
    return True if status_code == "open" else False


def add_money(amount):
    write_csv_row([get_current_money() + amount],
                  'csv_database/currentmoney_' + generate_date_only_stamp())


def withdraw_money(amount):
    add_money(-amount)


def get_current_money():
    return int([row for row in get_rows('csv_database/currentmoney_'
                                        + generate_date_only_stamp())][-1][0])


# Create new user in CSV file
def new_user(username, password, real_name):
    write_csv_row([generate_id(), username, password, real_name],
                  "csv_database/users.csv")
    log_action("added new user " + username, "Administrator")


def delete_user(username):
    users = [user for user in get_rows('csv_database/users.csv')]
    for user in [user for user in users if username not in users]:
        write_csv_row_overwrite(user, 'csv_database/users.csv')


def tests():
    initialize_database()
    print("user doesn't exist: ", login("john", "susy123"))
    print(generate_id())
    new_user("john", "susy123", "John Madden")
    new_user("susan", "susy123", "John Madden")
    print([user for user in get_users()])
    print("user exists: ", login("john", "susy123"))
    delete_user("john")
    print("user exists after delete: ", login("john", "susy123"))
    print([user for user in get_users()])
    print("before start", check_start_ammount())
    start_day(500)
    print("after start before end ", check_start_ammount())
    end_day(1000)
    print("after end", check_start_ammount())
    print(get_current_money())
    add_money(5)
    print(get_current_money())
    withdraw_money(10)
    print(get_current_money())


if __name__ == "__main__":
    tests()
