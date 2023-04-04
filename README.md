# MIS-Inform

## Setup and Virtual Environments
To run the project, you have to install the requirements listed in the `requirements.txt` file. You can use the pip command as follows:

`pip install -r requirements.txt`

## Project Structure

The project is made of a main script written in the `main.py` file and submodules written in the submodules directory. In addition there is a database whose cursor is implemented in the `submodules/database.py` file.

### Main Script
The main script is written in main.py. This script reads commands and sends them to the relevant submodule. 
For example when you run the command `misinform budget`, the main script will call the budget function of the budget submodule.

### Submodules
The project is made up of several submodules. Each of which implements a feature. A submodule is a python file whose name is the name of the file. Each module should have a function that will be called by the main script whenever a command is entered that requires that module.

contacts
Display contacts of different government departments.


### Database
The database used in this project is MySQL. As a result, you will need a MySQL connnector installed, which should be installed if you ran the `pip install -r requirements.txt` when setting up the project.

#### Database usage instructions
These instructions are written as part of the `database.py` module.

### OPTIONS 
OPTIONS
       press
Display the latest press releases issued by the government.

       budget
Display the actual and projected income and expenses of the government.

       projects
Display information about all ongoing government projects, including their completion rates and estimated completion dates.

       economy
Display current economic information, including GDP, exchange rate, employment rate, etc.

       population
Display population statistics.

       holidays
Display the list of public holidays for the current year.

       tenders
Display all pending tender notices.

       contact
Display contact information for government departments.

       -h, --help
Display the help page and exit.

# Contributors 
Samuel
Ochan
Anesu
Juliet
Ken
Honore
Benitha
Dimitri
