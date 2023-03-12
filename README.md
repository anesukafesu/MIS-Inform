# MIS-Inform

## Project Structure

The project is made of a main script written in the `main.py` file and submodules written in the submodules directory. In addition there is a database that stores data at the root of the project

### Main Script
The main script is written in main.py. This script reads commands and sends them to the relevant submodule. 
For example when you run the command `misinform budget`, the main script will call the budget function of the budget submodule.

### Submodules
The project is made up of several submodules. Each of which implements a feature. A submodule is a python file whose name is the name of the file. Each module should have a function that will be called by the main script whenever a command is entered that requires that module.

contacts


### Database
The database uses sqlite3. The project only makes and uses one connection to the database to prevent errors. Therefore to interact with database, you use functions implemented in the `database.py` file.

#### Database usage instructions
To interact with the database import the `db` function from `database.py` into your code

`from database import db`

Then call the db function with an SQL statement to execute queries

`db('CREATE TABLE team_members(name TEXT, email TEXT);')`

You can also get the result of your query by doing

`rows = db('SELECT * FROM team_members')`
