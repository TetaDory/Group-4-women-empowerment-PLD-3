#!/bin/python3
# Import modules
import sys

def main_menu_choice():
    def print_main_menu():
        print(30 * "-", "MAIN MENU", 30 * "-")
        print("1. Careers ")
        print("2. Edit profile ")
        print("3. View matches ")
        print("4. View messages ")
        print("5. Exit ")
        print(73 * "-")

    loop = True

    while loop:
        print_main_menu()
        choice = input("Enter your choice [1-2]: ")

        if choice == '1':
            print("Careers")
            loop = False
        elif choice == '2':
            print("Edit profile")
            loop = False
        elif choice == '3':
            print("View matches")
            loop = False
        elif choice == '4':
            print("View messages")
            loop = False
        elif choice == '5':
            print("Exit")
            loop = False
            sys.exit()
        else:
            input("Wrong menu selection. Enter any key to try again: ")
    return None