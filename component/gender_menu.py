#!/bin/python3
# Import modules
import sys

def gender_menu_choice():
    def print_gender_menu():
        print(30 * "-", "GENDER MENU", 30 * "-")
        print("1. Male ")
        print("2. Female ")
        print(73 * "-")

    loop = True

    while loop:
        print_gender_menu()
        choice = input("Enter your choice [1-2]: ")

        if choice == '1':
            print("The platform is only available to women!")
            loop = False
            sys.exit()
        elif choice == '2':
            loop = False
        else:
            input("Wrong menu selection. Enter any key to try again: ")
    return None