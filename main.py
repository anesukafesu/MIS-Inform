#!/usr/bin/python3
from simple_term_menu import TerminalMenu
from submodules.holidays import holidays
from submodules.projects import projects
from submodules.economy import economy
from submodules.population import population
from submodules.tenders import tenders
from submodules.contact import contacts
from os import system

welcome_screen = """
███╗   ███╗██╗███████╗      ██╗███╗   ██╗███████╗ ██████╗ ██████╗ ███╗   ███╗
████╗ ████║██║██╔════╝      ██║████╗  ██║██╔════╝██╔═══██╗██╔══██╗████╗ ████║
██╔████╔██║██║███████╗█████╗██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██╔████╔██║
██║╚██╔╝██║██║╚════██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║
██║ ╚═╝ ██║██║███████║      ██║██║ ╚████║██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝╚══════╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
"""

version = "(Version 1.0.0)"

product_intro = """
Mis-inform aims to bridge the information gap and keep citizens engaged in civic matters.
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

def show_terminal_menu(options = [], menu_title=""):
    centered_options = map(lambda option: option.center(77), options)
    terminal_menu = TerminalMenu(centered_options, menu_cursor="", title=menu_title)
    terminal_menu_selection_index = terminal_menu.show()

    # Get the selected option by name
    # Using names is more readable and generally safer than indexes
    return options[terminal_menu_selection_index]



exit_message = "01000111 01101111 01101111 01100100  01100010 01111001 01100101"

exit_program = False

# Loop to render screen
while True:
    if exit_program:
        print(exit_message)
        break

    def trigger_exit():
        global exit_program
        exit_program = True

    def show_help_info():
        print(guide)

    # Print welcome screen
    system("clear")
    print(welcome_screen)
    print(version)
    
    # Options
    options = {
        'Press': None,
        'Budget': None,
        'Projects': projects,
        'Economy': economy,
        'Population': population,
        'Holidays': holidays,
        'Tenders': tenders,
        'Contact': contacts,
        'Help': show_help_info,
        'Exit': trigger_exit
    }

    options_list = list(options.keys())
    s = show_terminal_menu(options_list, "Main Menu")

    # Calling the function for the option the user picked
    options[s].__call__()
    

    # Create an exit menu
    print("")
    print("")
    print("")
    exit_options = ["Back to Main Menu", "Exit"]
    
    s = show_terminal_menu(exit_options, "Exit options")

    if s == "Exit":
        trigger_exit()

    # Else the user opted to return to main menu
    # So we make sure exit_program is set to false
