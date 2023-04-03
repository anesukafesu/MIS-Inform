#!/usr/bin/python3
from database import create_cursor

def holidays():
    # Create a cursor and db connection
    cursor, db = create_cursor()

    # Get all holidays from the holidays table in the database
    cursor.execute('SELECT * FROM holidays')
    
    # Print the headings
    print("Date   | Holiday Name")
    
    # Print the holidays
    for date, holiday in cursor:
        print(date, "|", holiday)
