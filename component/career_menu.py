#!/bin/python3
# Import modules
import sys

# Dictionary to store ICT careers
ict_careers = {
    "1": "Software Developer \n Software developers design, develop, test, and maintain software applications.\n They are responsible for the entire software development life cycle, from the initial design to the final testing and deployment. \n",
    "2": "Web Developer \n Web developers design and create websites. They are responsible for the look of the site.\n They are also responsible for the site's technical aspects, such as its performance and capacity, which are measures of a website's speed and how much traffic the site can handle. \n",
    "3": "Data Scientist \n Data scientists use advanced analytics, machine learning techniques, and statistical algorithms to extract insights from data.\n They are responsible for collecting, cleaning, and analyzing data to identify trends and patterns. \n",
    "4": "Network Engineer \n Network engineers design, build, and maintain computer networks.\n They are responsible for the day-to-day operation of these networks, including planning, implementation, and monitoring of network infrastructure. \n",
    "5": "Database Administrator \n Database administrators design, implement, and maintain databases.\n They are responsible for ensuring the security, reliability, and performance of databases. \n",
}

# Dictionary to Medicine careers
medicine_careers = {
    "1": "Doctor \n Doctors diagnose and treat patients.\n They are responsible for the physical and mental health of their patients. \n",
    "2": "Nurse \n Nurses provide and coordinate patient care, educate patients and the public about various health conditions,\n and provide advice and emotional support to patients and their family members. \n",
    "3": "Pharmacist \n Pharmacists dispense prescription medication to patients and offer expertise in the safe use of prescriptions.\n They are responsible for the proper storage and disposal of medication. \n",
    "4": "Dentist \n Dentists diagnose and treat problems with patients' teeth, gums, and related parts of the mouth.\n They are responsible for the prevention, diagnosis, and treatment of diseases and conditions of the oral cavity. \n",
    "5": "Veterinarian \n Veterinarians diagnose, treat, and research medical conditions and diseases of animals.\n They are responsible for the health and well-being of animals. \n",
}

# Dictionary to Agriculture careers
agriculture_careers = {
    "1": "Agricultural Engineer \n Agricultural engineers design, develop, and improve agricultural machinery, equipment, and facilities.\n They are responsible for the design and construction of agricultural machinery, equipment, and facilities. \n",
    "2": "Agricultural Scientist \n Agricultural scientists conduct research and develop new technologies to improve agricultural production.\n They are responsible for the development of new technologies to improve agricultural production. \n",
    "3": "Agricultural Technician \n Agricultural technicians assist agricultural scientists and engineers in the development of new technologies.\n They are responsible for the development of new technologies to improve agricultural production. \n",
    "4": "Agricultural Economist \n Agricultural economists study the economic aspects of agricultural production.\n They are responsible for the economic aspects of agricultural production. \n",
    "5": "Agricultural Consultant \n Agricultural consultants provide advice to farmers and other agricultural producers.\n They are responsible for providing advice to farmers and other agricultural producers. \n",
}

# Dictionary to store Business careers
business_careers = {
    "1": "Accountant \n Accountants prepare and examine financial records.\n They are responsible for the financial health of an organization. \n",
    "2": "Business Analyst \n Business analysts identify ways to improve an organization's efficiency and profitability.\n They are responsible for the efficiency and profitability of an organization. \n",
    "3": "Business Development Manager \n Business development managers identify new business opportunities.\n They are responsible for the growth of an organization. \n",
    "4": "Business Manager \n Business managers oversee the daily operations of an organization.\n They are responsible for the daily operations of an organization. \n",
    "5": "Business Owner \n Business owners oversee the daily operations of an organization.\n They are responsible for the daily operations of an organization. \n",
}

# Dictionary to store Education careers
education_careers = {
    "1": "Teacher \n Teachers educate students in a specific subject.\n They are responsible for the education of students. \n",
    "2": "Lecturer \n Lecturers teach students in a specific subject.\n They are responsible for the education of students. \n",
    "3": "Professor \n Professors teach students in a specific subject.\n They are responsible for the education of students. \n",
    "4": "Librarian \n Librarians manage and organize a library's resources.\n They are responsible for the organization of a library's resources. \n",
    "5": "School Administrator \n School administrators manage and organize a school's resources.\n They are responsible for the organization of a school's resources. \n",
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