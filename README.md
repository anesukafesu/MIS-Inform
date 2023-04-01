# MIS-Inform

## Setup and Virtual Environments
To run the project, you have to install the requirements listed in the `requirements.txt` file. You can use the pip command as follows:

`pip install -r requirements.txt`

It is recommended that you use a virtual environment to avoid dependency conflicts with other programs. To set one up, follow the following steps:

1. Create the virtual environment
`python3 -m venv venv`

2. Activate the virtual environment
`source venv/bin/activate`

3. Install the project dependencies
`pip install -r requirements.txt`

After this you can run the scripts and this project's dependencies will be isolated from your other system-wide dependencies.

When you are done you can deactivate the environment
4. Deactivate the environment
`source venv/bin/deactivate`

Any other time you need to run the project, just activate(Step 2) and deactivate(Step 4) the virtual environment. Also make sure to reinstall the requirements.txt after each `git pull` in case there are additional dependencies.

## Project Structure

The project is made of a main script written in the `main.py` file and submodules written in the submodules directory. In addition there is a database that stores data at the root of the project

### Main Script
The main script is written in main.py. This script reads commands and sends them to the relevant submodule. 
For example when you run the command `misinform budget`, the main script will call the budget function of the budget submodule.

### Submodules
The project is made up of several submodules. Each of which implements a feature. A submodule is a python file whose name is the name of the file. Each module should have a function that will be called by the main script whenever a command is entered that requires that module.

contacts
Display contacts of different government departments.


### Database

#### Database usage instructions
...pending

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
