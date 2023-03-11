import sys


def press():
    # Code to display press releases goes here
    print("Press Releases")


def budget():
    # Code to display budget information goes here
    print("Budget Information")


def projects():
    # Code to display ongoing projects information goes here
    print("Ongoing Projects")


def economy():
    # Code to display current economic information goes here
    print("Economic Information")


def population():
    # Code to display population statistics goes here
    print("Population Statistics")


def holidays():
    # Code to display public holidays goes here
    print("Public Holidays")


def tenders():
    # Code to display tender notices goes here
    print("Tender Notices")


def contact():
    # Code to display contact information goes here
    print("Contact Information")


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
