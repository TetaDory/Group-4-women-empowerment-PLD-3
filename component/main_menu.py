#!/bin/python3
# Import modules
import sys

# Import components
from component.career_menu import career_menu_choice

def main_menu_choice():
    def print_main_menu():
        print(30 * "-", "MAIN MENU", 30 * "-")
        print("1. Careers ")
        print("2. Exit ")
        print(73 * "-")

    loop = True

    while loop:
        print_main_menu()
        choice = input("Enter your choice [1-2]: ")

        if choice == '1':
            # Call career_menu_choice function
            print(career_menu_choice())
            loop = False
        elif choice == '2':
            print("Exiting...")
            loop = False
            sys.exit()
        else:
            input("Wrong menu selection. Enter any key to try again: ")
    return None