# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.
# Task 1: Directory Inspector:
# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the 
# user for the directory path and then display the contents.
# Code Example:
# import os
# def list_directory_contents(path):
# List and print all files and subdirectories in the given path
# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for invalid 
# paths or inaccessible directories.
# 1. Create a function that will search the path given for a directory
# 2. Have the function locate the directory and print the contents of the directory.
# 3. Use exception handling to print a user friendly statement when a directory cannot be found, or a path does not exist.
# 4. Exceptions should include: FileNotFoundError, PermissionError, and IOError
# 5. Create a user input to ask for a path to a directory to be given.
# 6. Use the path given to call the function.

import os

def list_directory_contents(path):
    try:
        list_dir = os.listdir(path)
        for file in list_dir:
            print(file)
    except FileNotFoundError:
        print("The path given could not find a directory, please try again.")
    except PermissionError:
        print("You do not have permission to access the directory at the path given, please try again.")
    except IOError:
        print("We could not read the files in the directory for the path given, please try again.")

while True:
    user_input = input("Would you like to display the contents of a directory? (yes/no): ").lower()
    if user_input == "yes":
        user_prompt = input("Please use the format: 'drive:\\folder\\folder\\folder' to identify the path of the directory you wish to display\nWhat is the path to the directory you wish to display?: ")
        list_directory_contents(user_prompt)
    else:
        break