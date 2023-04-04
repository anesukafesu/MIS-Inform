#!/usr/bin/python3
from database import create_cursor


def economy():
    cursor, db = create_cursor()
    cursor.execute("SELECT * FROM economy")

    for stat, value in cursor:
        print(f"{stat}: {value}")
