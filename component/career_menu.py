#!/bin/python3
# Import modules
import sys

# Dictionary to store ICT careers
ict_careers = {
    "1": "Software Developer",
    "2": "Web Developer",
    "3": "Data Scientist",
    "4": "Network Engineer",
    "5": "Database Administrator",
}

# Dictionary to Medicine careers
medicine_careers = {
    "1": "Doctor",
    "2": "Nurse",
    "3": "Pharmacist",
    "4": "Dentist",
    "5": "Veterinarian",
}

# Dictionary to Agriculture careers
agriculture_careers = {
    "1": "Agricultural Engineer",
    "2": "Agricultural Scientist",
    "3": "Agricultural Technician",
    "4": "Agricultural Economist",
    "5": "Agricultural Consultant",
}

# Dictionary to store Business careers
business_careers = {
    "1": "Accountant",
    "2": "Business Analyst",
    "3": "Business Development Manager",
    "4": "Business Manager",
    "5": "Business Owner",
}

# Dictionary to store Education careers
education_careers = {
    "1": "Teacher",
    "2": "Lecturer",
    "3": "Professor",
    "4": "Librarian",
    "5": "School Administrator",
}

# Function to display career menu choice
def career_menu_choice():
    def print_career_menu():
        print(30 * "-", "CAREER MENU", 30 * "-")
        print("1. Information & Communication Technology ")
        print("2. Medicine ")
        print("3. Agriculture ")
        print("4. Business ")
        print("5. Education ")
        print("6. Exit ")
        print(73 * "-")

    loop = True

    while loop:
        print_career_menu()
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            print(ict_careers["1"])
            print(ict_careers["2"])
            print(ict_careers["3"])
            print(ict_careers["4"])
            print(ict_careers["5"])
            loop = False
        elif choice == '2':
            print(medicine_careers["1"])
            print(medicine_careers["2"])
            print(medicine_careers["3"])
            print(medicine_careers["4"])
            print(medicine_careers["5"])
            loop = False
        elif choice == '3':
            print(agriculture_careers["1"])
            print(agriculture_careers["2"])
            print(agriculture_careers["3"])
            print(agriculture_careers["4"])
            print(agriculture_careers["5"])
            loop = False
        elif choice == '4':
            print(business_careers["1"])
            print(business_careers["2"])
            print(business_careers["3"])
            print(business_careers["4"])
            print(business_careers["5"])
            loop = False
        elif choice == '5':
            print(education_careers["1"])
            print(education_careers["2"])
            print(education_careers["3"])
            print(education_careers["4"])
            print(education_careers["5"])
            loop = False
        elif choice == '6':
            print("Exiting...")
            loop = False
            sys.exit()
        else:
            input("Wrong menu selection. Enter any key to try: ")