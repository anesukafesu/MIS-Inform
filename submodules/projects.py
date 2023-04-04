from database import create_cursor
import datetime

cursor,db = create_cursor()


project_name = "Amahoro Stadium Refurbishment"
project_location = "Kigali City, Kigali Province"
project_description = "Renovating Amahoro stadium to align with international stadium standards. The objective is to make Kigali a sporting destination and promote tourism in Rwanda."
duration_months = "12"
estimated_completion_date = "28 March 2024"
project_status = "Ongoing"

project_name = "Upgrading of unpaved roads to paved"
project_location = "Musanze, Eastern Province"
project_description = "Upgrade the roads to meet the international statandards of roads."
duration_months = "8"
estimated_completion_date = "30th October 2023"
project_status = "To be started"

cursor.execute("INSERT INTO projects(name,location, description, estimated_completion_date, status) VALUES(%s,%s,%s,%s,%s)",(project_name, project_location, project_description, estimated_completion_date, project_status))

project_name = "Informal settlement upgrade"
project_location = "Nyarugege, Kigali Province"
project_description = "Upgrade slums to achieve good sustainable housing in the city of Kigali."
duration_months = "12"
estimated_completion_date = "28 April 2025"
project_status = "Ongoing"

cursor.execute("INSERT INTO projects(name,location, description, estimated_completion_date, status) VALUES(%s,%s,%s,%s,%s)",(project_name, project_location, project_description, estimated_completion_date, project_status))

project_name = "Install and operationalize weighbridge stations"
project_location = "All the Rwandan Borders"
project_description = "The weighbridge will facilitate easy, smooth and reliable movement at all the border post."
duration_months = "6"
estimated_completion_date = "20 september 2023"
project_status = "Ongoing"

cursor.execute("INSERT INTO projects(name,location, description, estimated_completion_date, status) VALUES(%s,%s,%s,%s,%s)",(project_name, project_location, project_description, estimated_completion_date, project_status))

project_name = "Nyabarongo hydro power project"
project_location = "Rukira, Eastern Province"
project_description = "The poject is for Rwanda to generate its own hydro electric power to supply electrity at low cost to the citizens of Rwanda."
duration_months = "18"
estimated_completion_date = "20 september 2025"
project_status = "Ongoing"

db.commit()

