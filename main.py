#!/usr/bin/python3

import sys
from budget import budget
from holidays import holidays


def help():
    # Code to display help information goes here
    print("""
Options:
    press      Display the latest press releases issued by the government.
    budget     Display the actual and projected income and expenses of the government.
    projects   Display information about all ongoing government projects, including their completion rates and estimated completion dates.
    economy    Display current economic information, including GDP, exchange rate, employment rate, etc.
    population Display population statistics.
    holidays   Display the list of public holidays for the current year.
    tenders    Display all pending tender notices.
    contact    Display contact information for government departments.
    -h, --help Display the help page and exit.
""")


# Main program loop
while True:
    print("Welcome to Misinform! Please select an option:")
    print("1. Press")
    print("2. Budget")
    print("3. Projects")
    print("4. Economy")
    print("5. Population")
    print("6. Holidays")
    print("7. Tenders")
    print("8. Contact")
    print("9. Help")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        press()
    elif choice == "2":
        budget()
    elif choice == "3":
        projects()
    elif choice == "4":
        economy()
    elif choice == "5":
        population()
    elif choice == "6":
        holidays()
    elif choice == "7":
        tenders()
    elif choice == "8":
        contact()
    elif choice == "9":
        help()
    elif choice == "0":
        print("Thank you for using Misinform!")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
