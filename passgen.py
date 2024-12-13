"""
passgen.py

VERSION = 1.0.1

This script checks in the local directory that the file is in and makes a passwords folder and stores
a text file labeled 'passwords.txt' and creates the amount of pass words selected
or it will just print them out to the console if the user does not want a file for them

I am aware of the random module vulnerabilities but this was just to test my documentation understanding 
and to see how far I could go without looking for online/documentation resources

I could take this a step further and make a GUI using Tkinter but that would probably be unneccesary

Ideas:
1. Porting this into a chrome extension for easy to make passwords and they would save to your computer in 
a save location with info such as Website name and password

"""

import os
import random as rand

# Global variables
CURRENT_DIR = os.getcwd()

# Used to create a file to store passwords
def createFile(filename):
    try:
        with open(os.path.join(f"{CURRENT_DIR}\\passwords",filename), 'x') as f:
            print(f"File '{filename}' created successfully.")
    except FileNotFoundError:
        os.makedirs(f"{CURRENT_DIR}/passwords")
        with open(os.path.join(f"{CURRENT_DIR}\\passwords",filename), 'x') as f:
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"Opening '{filename}' ")

# Function to create password(s) based off of the user inputs
def passGen(length,complexity):
    # Variables for making password
    generatedPass = []
    chars = "abcdefghijklmnopqrstuvwxyz"
    nums = "123456789"
    special = "!@#$%&*"

    # logic for making the passwords
    if complexity == 1:
        for i in range(length):
            x = rand.randint(1,2)
            if x == 1:
                x = chars[rand.randint(0, len(chars) - 1)]
            elif x == 2:
                x = nums[rand.randint(0, len(nums) - 1)]
            generatedPass.append(x)

    if complexity == 2:
        for i in range(length):
            x = rand.randint(1,3)
            if x == 1:
                x = chars[rand.randint(1, len(chars) - 1)]
            elif x == 2:
                x = nums[rand.randint(0, len(nums) - 1)]
            elif x == 3:
                x = special[rand.randint(0, len(special) - 1)]
            generatedPass.append(x)

    return generatedPass


def main():
    # Variables
    PASSWORDS = []
    COUNT = 0

    # Asking user how they want their password
    amount = int(input(f"How many passwords would you like to create?\n>> "))
    length = int(input(f"\nHow many characters long would you like the password to be? (16 recommened for security)\n>> "))
    complexity = int(input(f"\nHow complex would you like the password?\n1. Letters and numbers\n2. Letters, numbers, and special characters\n>> "))
    saveFile = input(f"\nWould you like the passwords saved to a file named passwords.txt (yes or no)\n>> ").lower()
    
    if saveFile[0] == "y":

        createFile("passwords.txt")
        passFile = open(os.path.join(f"{CURRENT_DIR}\\passwords","passwords.txt"), "a")
  

        for i in range(amount):
            password = passGen(length,complexity)
            PASSWORDS.append("".join(password))

        for i in PASSWORDS:
            COUNT += 1
            passFile.write(f"{COUNT}. {i}\n")

        passFile.close()
    


    elif saveFile[0] == "n":
        print(f"\nHere are {amount} passwords with a length of {length}:\n--------------------")
        for i in range(amount):
            password = passGen(length,complexity)
            print("".join(password))
        print("--------------------")


    


if __name__ == "__main__":
    main()