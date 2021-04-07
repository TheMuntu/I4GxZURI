import datetime
import random

database = {}


def init():
    print("Welcome to PacMan Bank")

    haveAccount = int(input("Do you have account with us? 1 (yes) 2 (no) \n"))

    if haveAccount == 1:
        login()

    elif haveAccount == 2:
        register()

    else:
        print("You have selected an invalid option")
        init()


# Login
def login():
    print("********* Login *********")

    accountNumberFromUser = int(input("enter your account number: \n"))
    password = input("Enter your password: \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)
            else:
                print("Invalid account or password")
                login()


# Register
def register():
    print("********* Register *********")
    email = input("Enter your email: \n")
    first_name = input("Enter your first_name: \n")
    last_name = input("Enter your last name: \n")
    password = input("Create a password: \n")

    account_number = generationAccountNumber()

    database[account_number] = [first_name, last_name, email, password]

    print("Your account has been created!")
    print(f"Your account number is {account_number}")
    print("Keep it safe!!\n")

    login()


def bankOperation(user):
    print(f"Welcome {user[0]} {user[1]} ")
    current_date = datetime.datetime.now()
    print(f"Current date and time : {current_date.strftime('%Y-%m-%d %H:%M:%S')}\n")

    selectedOption = int(input("What would you like to do? \n (1) deposit (2) withdrawal "
                               "(3) Complaint (4) exit \n "))

    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation()
    elif selectedOption == 3:
        complainOperation()
    elif selectedOption == 4:
        logout()
    else:
        print("Invalid option selected")
        bankOperation(user)


# logout
def logout():
    exit()


# Generate Account Number
def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

    # Operations

def depositOperation():
    deposit_amount = int(input("How much would you like to deposit? :\n"))
    print(f"Your current balance is ${deposit_amount}")


def withdrawalOperation():
    withdrawal_amount = input("How much would you like to withdraw? :\n")
    print(f"Take your cash ${withdrawal_amount}")


def complainOperation():
    problem = input("What issue will you like to report? :\n")
    print("Thank you for contacting us")

    #### Actual banking System ####


init()
