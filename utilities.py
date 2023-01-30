import os
import datetime
import uuid
import csv

### DATABASE FUNCTIONS ###

# Iterator for the username and passwords
def get_users():
    with open('csv_database/users.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield (row[1], row[2])

def get_rows(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row
def set_register_open(is_open):
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        if is_open:
            writer.writerow(["open"])
        else:
            writer.writerow(["closed"])

# Write a row to a CSV
def write_csv_row(row, filename):
    with open(filename, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)

# Initialize the folder and files for the database empty
def initialize_database():
    try:
        os.mkdir("./csv_database")
    except:
        print("already there")
    
    file_list = ["users.csv", "nonauthorizedpassword.csv",
                 "nonauthorizedwithdrawals.csv", "startofdayreports.csv",
                 "endofdayreports.csv", "actionlog.csv","register_status.csv"]
    
    for file in file_list:
        with open('csv_database/'+file, 'w') as file:
            pass
#Misssing the recording of transaction to process funcitons 
#Checks password requiered for withatrawal to guarantee access from the csv

def check_password_nonautorized_widrawal(password):
    
    with open('csv_database/nonautorizedpassword.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == password:
                return True #Replace for open the widrawl windown
        return False #Trow error and record attempt of acess without autorization

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
    
def log_action(action_string, username):
    with open("csv_database/actionlog.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.datetime.now(), action_string, username])


# Generate timestamp with seconds
def generate_timestamp():
    return str(datetime.datetime.now())

# Generates the required string for a date stamp
# Only does date without time for EOD and SOD reports
def generate_date_only_stamp():
    year = str(datetime.datetime.now().date().year)
    month = str(datetime.datetime.now().date().month)
    day = str(datetime.datetime.now().date().day)
    return year + month + day
        
# Generate the unique user ID in hex
def generate_id():
    return uuid.uuid4().hex