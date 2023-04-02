"""
Use this module to connect to the database. To connect to the database,
you will need a cursor. Use the create_cursor function to create a
cursor to the database.

Functions:
    - create_cursor
"""

from mysql.connector import connect

def create_cursor():
    """
    Creates a database cursor that you can use to execute queries.
    Example usage:

    from database import create_cursor
    
    # Create a cursor using the create_cursor function
    cursor = create_cursor()
    
    # Execute a query
    cursor.execute("INSERT INTO test(name, email) VALUES ('John Doe', 'john@example.com');")

    # Execute another query
    cursor.execute("SELECT * FROM test;")

    # Access the result of your query on the cursor object
    for user in cursor:
        print(user)

    Additional tutorial on how to use MySQL in Python: https://www.w3schools.com/python/python_mysql_create_db.asp
    """
    db = connect(
        user='negpod5',
        password='password',
        port=3306,
        host='129.151.170.34',
        database='pld'
    )

    cursor = db.cursor()

    return cursor
