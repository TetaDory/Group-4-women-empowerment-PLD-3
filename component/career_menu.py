#!/bin/python3
# Import modules
import sys

# Function to display career menu choice
def career_menu_choice():
    def print_career_menu():
        print(30 * "-", "CAREER MENU", 30 * "-")
        print("1. Information & Communication Technology ")
        print("2. Medicine ")
        print("3. Agriculture ")
        print("4. Exit ")
        print(73 * "-")

    loop = True

    while loop:
        print_career_menu()
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            print("Information & Communication Technology")
            loop = False
        elif choice == '2':
            print("Medicine")
            loop = False
        elif choice == '3':
            print("Agriculture")
            loop = False
        elif choice == '4':
            print("Exiting...")
            loop = False
            sys.exit()
        else:
            input("Wrong menu selection. Enter any key to try: ")