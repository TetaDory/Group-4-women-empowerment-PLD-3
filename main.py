#!/bin/python3
# Import modules
import sys
import random
import time

# Import components
from component.gender_menu import gender_menu_choice
from component.main_menu import main_menu_choice

# Ask user to input name
print("Enter first name: ")
first_name = input()
print("Enter Last name: ")
last_name = input()

# Call gender_menu_choice function       
print(gender_menu_choice())

# Ask user to input age

print("Enter your age: ")
age = int(input())
if age < 18:
    print("You are under age")
    sys.exit()
elif age > 45:
        print("You are over age")
        sys.exit()

# Function to check if email is valid
def email_check(email):
    if "@" in email:
        print("Welcome to the platform!")
        # Wait for 2 seconds
        time.sleep(2)
    else:
        print("Email is invalid")
        sys.exit()

# Ask user to input email
print("Enter email: ")
email = input()

# Call email_check function
email_check(email)

# Dictionary to store greeting messages
greetings = {
    "1": "Hello",
    "2": "Hey",
    "3": "Greetings",
    "4": "Howdy",
    "5": "What's up",
}

# Generate a random number between 1 and 5
greetings_number = random.randint(1, 5)

# Print greeting message
if greetings_number == 1:
    print(f"{greetings['1']}, {first_name}")
elif greetings_number == 2:
    print(f"{greetings['2']}, {first_name}")
elif greetings_number == 3:
    print(f"{greetings['3']}, {first_name}")
elif greetings_number == 4:
    print(f"{greetings['4']}, {first_name}")
elif greetings_number == 5:
    print(f"{greetings['5']}, {first_name}")

# Dictionary to store quotes
quotes = {
    "1": "You are beautiful",
    "2": "You are smart",
    "3": "You are strong",
    "4": "You are loved",
    "5": "You are worthy",
}

# Generate a random number between 1 and 5
quotes_number = random.randint(1, 5)

# Print quote message
if quotes_number == 1:
    print(f"{quotes['1']}")
elif quotes_number == 2:
    print(f"{quotes['2']}")
elif quotes_number == 3:
    print(f"{quotes['3']}")
elif quotes_number == 4:
    print(f"{quotes['4']}")
elif quotes_number == 5:
    print(f"{quotes['5']}")
time.sleep(2)

# Call main_menu_choice function
print(main_menu_choice())
