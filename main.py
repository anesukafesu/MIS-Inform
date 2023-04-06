#!/usr/bin/python3
from simple_term_menu import TerminalMenu
from holidays import holidays
from projects import projects
from economy import economy
from population import population
from tenders import tenders
from contact import contacts
from press import press
from budget import budget
from os import system, name as os_name
from time import sleep

welcome_screen ="""
███╗   ███╗██╗      ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
████╗ ████║██║      ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
██╔████╔██║██║█████╗███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
██║╚██╔╝██║██║╚════╝╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
██║ ╚═╝ ██║██║      ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝      ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
"""

version = "(Version 1.0.0)"

product_intro = """
Mi-system aims to bridge the information gap and keep citizens engaged in civic matters.
We do this by providing up-to-date information on government affairs.
"""

guide = """
Here are the current features:

    press      Display the latest press releases issued by the government.
    budget     Display the actual and projected income and expenses of the government.
    projects   Display information about all ongoing government projects, including their completion rates and estimated completion dates.
    economy    Display current economic information, including GDP, exchange rate, employment rate, etc.
    population Display population statistics.
    holidays   Display the list of public holidays for the current year.
    tenders    Display all pending tender notices.
    contact    Display contact information for government departments.
    help       Display this informaiton page again
    exit       Exit MIS-Inform
"""

exit_message = "01100010 01111001 01100101 which is binary for 'bye'..."

flags = {
    'exit_program': False
}


def show_terminal_menu(options = [], menu_title=""):
    centered_options = map(lambda option: option.center(73), options)
    terminal_menu = TerminalMenu(centered_options, menu_cursor="", title=menu_title)
    terminal_menu_selection_index = terminal_menu.show()

    # Get the selected option by name
    # Using names is more readable and generally safer than indexes
    return options[terminal_menu_selection_index]


# Clears screen
def clear_screen():
    if os_name == "posix":
        # Use clear command on Linux, Mac OS, BSD
        system("clear")
    else:
        # Else the system is Windows
        system("cls")


# Tells the program to exit
def trigger_exit():
    flags['exit_program'] = True

# Prints the guide
def show_help_info():
    print(guide)

# Loop to render screen
while True:
    try:
        # Checks if the program should exit
        if flags['exit_program']:
            clear_screen()
            print(exit_message)
            sleep(1)
            break

        clear_screen()

        # Print welcome screen and version
        print(welcome_screen)
        print(version)
    
        # Options
        options = {
            'Press': press,
            'Budget': budget,
            'Projects': projects,
            'Economy': economy,
            'Population': population,
            'Holidays': holidays,
            'Tenders': tenders,
            'Contact': contacts,
            'Help': show_help_info,
            'Exit': trigger_exit
        }
    
        # Creating a list of all available options
        options_list = list(options.keys())

        # Showing the terminal menu
        # User's selection will be returned and stored in s
        s = show_terminal_menu(options_list, "Main Menu")

        # Calling the function for the option the user picked
        options[s].__call__()
    

        # Create an exit menu
        print("")
        print("")
        print("")
        exit_options = ["Back to Main Menu", "Exit"]
    
        s = show_terminal_menu(exit_options, "Exit Options")

        if s == "Exit":
            trigger_exit()
        else:
            # The user opted to return to the main menu
            # We make sure that they do not exit
            flags['exit_program'] = False
    except:
        print("Something went wrong. Please try again...")
        sleep(1.5)
