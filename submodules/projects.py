from database import create_cursor
import datetime

cursor,db = create_cursor()


project_name = "Amahoro Stadium Refurbishment"
project_location = "Kigali City, Kigali Province"
project_description = "Renovating Amahoro stadium to align with international stadium standards. The objective is to make Kigali a sporting destination and promote tourism in Rwanda."
duration_months = "12"
estimated_completion_date = "28 March 2024"
project_status = "Ongoing"

cursor.execute("INSERT INTO projects(name, location, description, estimated_completion_date, status) VALUES(%s,%s,%s,%s,%s)",(project_name, project_location, project_description, estimated_completion_date, project_status))

db.commit()

