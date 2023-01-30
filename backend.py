import csv
import datetime
import uuid
import os


# Generates the required string for a date stamp
# Only does date without time for EOD and SOD reports
def generate_date_only_stamp():
    year = str(datetime.datetime.now().date().year)
    month = str(datetime.datetime.now().date().month)
    day = str(datetime.datetime.now().date().day)
    return year + month + day

#Read user and password from user imput and check credentials with the csv file
def login(user, password):
    
    with open('csv_database/users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user and row[1] == password:
                return True
        return False

#Misssing the recording of transaction to process funcitons 
#Checks password requiered for withatrawal to guarantee access from the csv

def check_password_nonautorized_widrawal(password):
    
    with open('csv_database/nonautorizedpassword.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == password:
                return True #Replace for open the widrawl windown
        return False #Trow error and record attempt of acess without autorization
    

#Misssing the recording of transaction to process funcitons 
#Computes calculations of owe moeny and returns the ammout of money to be returned after customer pay
# and record te transaction into the csv file

def compute_money_owed(money_owed, money_from_Customer ,money_returned):
    if money_from_Customer >= money_owed:
        money_returned = money_from_Customer - money_owed
        
        return money_returned
    
    return false #Replace with an error to the screen notifing the customer that he needs to pay more money


#nonautorized widrawl function
#This function will be used to record the ammount of money and the reason for the widrawl with current 
# date and time of the widrawl recorded into the csv fil into a csv file


def nonautorized_widrawl(widrawl, reason):
    
    with open('csv_database/nonauthorizedwithdrawals.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([widrawl, reason,datetime.datetime.now()])
    
    return True #Replace with a message to the screen saying that the widrawl was recorded and trake to the main screen
    

#startday funciton 
#This function will grab the ammount of money that was set by admin that the register will have from the beggining of the day

def start_day(starting_money):
    
    with open('csv_database/startofdayreports.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([starting_money,generate_date_only_stamp()])
    
    return True #Replace with a message to the screen saying that the set money was recorded and trake to the main screen

#endday function
#This function will close the reigser recording into the csv file the ammount of money that was left in the register
# This funciton is not complete 
def end_day(money_left):
    with open('csv_database/endofdayreports.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([money_left,generate_date_only_stamp()])
        return True #Replace with a message to the screen saying that the money left was recorded and trake to the main screen



# Check if admin has logged the start of workday and we havent closed yet
def check_start_ammount():
    if start_entry_exists() and not end_entry_exists():
        return True
    return False
    
# Check if we opened today yet
def start_entry_exists():
    with open('csv_database/startofdayreports.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if int(row[0]) > 0 and row[1] == generate_date_only_stamp():
                return True
        return False

# Check if we closed today yet
def end_entry_exists():
    with open('csv_database/endofdayreports.csv', 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if int(row[0]) > 0 and row[1] == generate_date_only_stamp():
                return True
        return False

#EXAMPLE OF THE CSV FILE
# START MONEY AMMOUNT , DATE , END  MONEY AMMOUNT , DATE 
# 2000 , 10-30-2020 , 3452 , 10 - 30 - 2020 # THE RECORD TRANSACTION WILL NOT WORK
# 2000  , 10- 30 -2020  # The record transaction button will work
# None # The record transaction button will not work

def open_cash_register():
    pass

def add_money(amount):
    pass

def withdraw_money(amount):
    pass

def get_current_money():
    pass
    

def log_action(action_string, username):
    with open("csv_database/actionlog.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), action_string, username])

def new_user(id, username, password, real_name):
    with open("csv_database/users.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow([id, username, password, real_name])
    log_action("added new user " + username, "Administrator")

def generate_id():
    return uuid.uuid4().hex

def initialize_database():
    try:
        os.mkdir("./csv_database")
    except:
        print("already there")
    
    file_list = ["users.csv", "nonauthorizedpassword.csv",
                 "nonauthorizedwithdrawals.csv", "startofdayreports.csv",
                 "endofdayreports.csv", "actionlog.csv"]
    
    for file in file_list:
        with open('csv_database/'+file, 'w') as file:
            pass

def tests():
    initialize_database()
    print(generate_id())
    new_user(generate_id(), "john", "susy123", "John Madden")
    print("before start", check_start_ammount())
    start_day(500)
    print("after start before end ", check_start_ammount())
    end_day(1000)
    print("after end", check_start_ammount())


if __name__ == "__main__":
    tests()
