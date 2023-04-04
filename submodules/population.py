from database import create_cursor


def population():
    cursor, db = create_cursor()
    cursor.execute("SELECT * FROM population")
    for stat, amount in cursor:
        print(f"{stat}: {amount}")
