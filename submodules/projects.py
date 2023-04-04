from database import create_cursor


def projects():
    cursor, db = create_cursor()
    cursor.execute("SELECT * FROM projects")
    for name, location, description, estimated_completion_date, status in cursor:
        print("Project Name:", name)
        print("Project Location:", location)
        print("Project Description:", description)
        print("Estimated Completion Date:", estimated_completion_date)
        print("Project Status:", status)
        print("")