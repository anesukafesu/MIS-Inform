# MI-System


## Setup
To run the project, you have to run the setup script in the root directory. This script will add the project directory to your PATH variable.

`./misystem-setup`

## Run the project
Once the script, has been setup, you may start the application with the command
`misystem`

or if the current folder was not successfully added to your PATH variable you may use the relative path variable:
`./misystem`

## Current features
 
press - display the latest press releases issued by the government.
budget - display the actual and projected income and expenses of the government.
projects - display information about all ongoing government projects, including their completion rates and estimated completion dates.
economy - display current economic information, including GDP, exchange rate, employment rate, etc.
population - display population statistics.
holidays - display the list of public holidays for the current year.
tenders - display all pending tender notices.
contact - display contact information for government departments.

## Technical documentation
This part of the documentation is only relevant to developers/contributors.

### Project Structure

The main program runs in the `main.py`. This file creates the menu and receives user input. Based on the user's input it calls a function from the submodules directory. These functions are responsible for rendering the content needs. However, before the main script runs, there is some preparation work that needs to be done. This is handled by the `misystem` bash script. The script acts like a boot loader. When you write the `misystem` command, it does some preparatory work before running the `main.py` file that then takes over.

### Database
The application relies on data stored in a cloud MySQL database. The `submodules/database.py` module provides an easy way to connect to the database and make SQL queries. For instructions on how to use `database.py` module, you can read its documentation and the documentation of its functions. This application only has read access to the database.

# Contributors 
Samuel
Ochan
Anesu
Juliet
Ken
Honore
Benitha
Dimitri
