# Make a simple register function    DONE
# Simple encryption for the user details    DONE
# Add a login function  DONE
# Make the following menus:
#  - Main menu    DONE
#  - When logged in    DONE
#  - Help menu    DONE
#  - Acc details menu    INPROGRESS
#  - The actual database   INPROGRESS
# Create and load databases    INPROGRESS
# Create columns and rows in your database    INPROGRESS
# Queries    INPROGRESS
# Edit / change fields    INPROGRESS


import csv
import os
import time

clearConsole = lambda: os.system("cls")

#======================================================================#
def register():
   
    firstname = input("Enter your first name: ").lower()
    print("First name set to: " + firstname)
    surname = input("Enter your surname: ").lower()
    print("Surname set to: " + surname)
   
    age = input("Enter your age: ")
    if not str.isdecimal(age):
        print("Age must be a number. Please try again.")
        age = input("Enter your age: ")
        print("Age set to: " + age)
   
    password = input("Enter a strong password: ")
    if len(password) < 6:
        print("Password should be between 6 to 18 characters long.")
        password = input("Enter a strong password: ")
        print("Password is: " + password)

    username = firstname[:1] + surname + age
    username.lower()
   
    print("Your username is: " + username + "\nYour password is: " + password + "\nYour firstname is: " + firstname + "\nYour surname is: " + surname + "\nYour age is: " + age)
   
    global encryptedUsername, encryptedPassword, encryptedFirstname, encryptedSuraname, encryptedAge
   
    encryptedUsername = "".join(chr(ord(char)+3) for char in username)
    encryptedPassword = "".join(chr(ord(char)+3) for char in password)
    encryptedFirstname = "".join(chr(ord(char)+3) for char in firstname)
    encryptedSuraname = "".join(chr(ord(char)+3) for char in surname)
    encryptedAge = "".join(chr(ord(char)+3) for char in age)
   
    if not str.isdecimal(age) or len(password) < 6:
        print("Error occured! Please make sure all details are valid!")
        time.sleep(3)
        clearConsole()
        loginMenu()
    else:
        with open("account.txt", "a", newline = "") as myFile:
            writer = csv.writer(myFile)
            writer.writerow([encryptedUsername, encryptedPassword, encryptedFirstname, encryptedSuraname, encryptedAge])
            myFile.close()
            print("Account successfully made! Please login now.")
            time.sleep(1)
            print("Loading...")
            time.sleep(2)
            clearConsole()
            loginMenu()
#======================================================================#
def databaseOptionMenu():
   
    print( "#========================================#   #==============>>")
    print( "|   Please select what you want to do.   |   |   Logged in as:")
    print(f"|                                        |   |   {user0}")
    print( "|         Press 1 to Load table          |   #==============>>")
    print( "|         Press 2 to New table           |")
    print( "|                                        |")
    print( "|     Press 3 to see account details     |")
    print( "|           Press 4 to Log out           |")
    print( "|      Press 5 to exit the program       |")
    print( "#========================================#")
   
    try:
        selection1 = int(input("Option: "))
    except:
        clearConsole()
        print("Select from 1 to 5 please.")
        time.sleep(2)
        clearConsole()
        databaseOptionMenu()
       
    if selection1 == 4:
        print("Loading...")
        time.sleep(2)
        clearConsole()
        loginMenu()
    elif selection1 == 3:
        print("Loading...")
        time.sleep(2)
        clearConsole()
        accountInfo()
    elif selection1 == 1:
        print("Still coding...")
        time.sleep(2)
        clearConsole()
        databaseOptionMenu()
    elif selection1 == 2:
        print("Still coding...")
        time.sleep(2)
        clearConsole()
        databaseOptionMenu()
    if selection1 == 5:
        print("Exiting the program...")
        time.sleep(3)
        clearConsole()
        exit()
    else:
        print("Select from 1 to 6 please.")
        time.sleep(2)
        clearConsole()
        databaseOptionMenu()
#======================================================================#
def login():
   
    global user0
    user0 = input("Username: ").lower()
    global pass0
    pass0 = input("Password: ")
   
    encryptedUsername = "".join(chr(ord(char)+3) for char in user0)
    encryptedPassword = "".join(chr(ord(char)+3) for char in pass0)
   
    try:
        file = open("account.txt", "r")
    except:
        print("Account doesn't exist! Please register an account.")
        time.sleep(3)
        clearConsole()
        print("Loading...")
        time.sleep(2)
        clearConsole()
        loginMenu()
       
    detailsList = []
    for line in file:
        detailsList.append(line.split(","))

    loggedIn = False

    for details in detailsList:
        if encryptedUsername == details[0] and encryptedPassword == details[1]:
            loggedIn = True
            break

    if loggedIn:
        print("Successfully logged in!")
        time.sleep(1)
        print("Loading...")
        time.sleep(2)
        clearConsole()
        databaseOptionMenu()
    else:
        print("Incorrect Username or Password, please try again.")
        time.sleep(1)
        print("Loading...")
        time.sleep(2)
        clearConsole()
        loginMenu()
#======================================================================#
def loginMenu():
   
    print("#===================================#")
    print("|    Welcome to Python Database!    |")
    print("|                                   |")
    print("|        Press 1 to Register        |")
    print("|         Press 2 to Login          |")
    print("|                                   |")
    print("|       Press 3 for help menu       |")
    print("|                                   |")
    print("|     Press 4 to exit the program   |")
    print("#===================================#")
   
    try:
        selection = int(input("Option: "))
    except:
        print("Select from 1 to 4 please.")
        time.sleep(3)
        clearConsole()
        loginMenu()
   
    if selection == 1:
        register()
    elif selection == 2:
        login()
    elif selection == 3:
        clearConsole()
        print("#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Help Menu=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#")
        print("|                                                                             |")
        print("|            First time using? Start by registering an account.               |")
        print("|          To do that you need to press 1, and enter your details             |")
        print("|             If your already a user then press 2 to login.                   |")
        print("|       To view your account details when your're logged in press 5.          |")
        print("|       To log out from your account press 6, when your're logged in.         |")
        print("|                                                                             |")
        print("|                          Press enter to go back                             |")
        print("#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#")
        selection2 = input("Option: ")
        if selection2 == 0:
            print("Loading...")
            time.sleep(2)
            clearConsole()
            loginMenu()
        else:
            print("Loading...")
            time.sleep(2)
            clearConsole()
            loginMenu()
    if selection == 4:
        print("Exiting the program...")
        time.sleep(3)
        clearConsole()
        exit()
    else:
        print("Select from 1 to 4 please.")
        time.sleep(3)
        clearConsole()
        loginMenu()
#======================================================================#
def accountInfo():
   
    file = open("account.txt", "r")
   
    detailsList = []
   
    for line in file:
        detailsList.append(line.split(","))
   
    for details in detailsList:

        encryptedUsername = "".join(chr(ord(char)+3) for char in user0)
        encryptedPassword = "".join(chr(ord(char)+3) for char in pass0)
       
        if encryptedUsername == details[0] and encryptedPassword == details[1]:
           
            decryptedUsername = "".join(chr(ord(char)-3) for char in details[0])
            decryptedPassword = "".join(chr(ord(char)-3) for char in details[1])
            decryptedFirstname = "".join(chr(ord(char)-3) for char in details[2])
            decryptedSurname = "".join(chr(ord(char)-3) for char in details[3])
            decryptedAge = "".join(chr(ord(char)-3) for char in details[4])
           
            print(decryptedUsername + ", " + decryptedPassword + ", " + decryptedFirstname + ", " + decryptedSurname + ", " + decryptedAge)
           
            if input("Press enter to go back."):
                print("Loading...")
                time.sleep(2)
                clearConsole()
                databaseOptionMenu()
            else:
                print("Loading...")
                time.sleep(2)
                clearConsole()
                databaseOptionMenu()
            break
#======================================================================#
clearConsole()
loginMenu()