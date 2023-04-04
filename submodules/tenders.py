from database import create_cursor

cursor, db = create_cursor()

cursor.execute("""
CREATE TABLE tenders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  closing_date DATE
);
""")

add_tender = "INSERT INTO tenders (title, description, closing_date) VALUES (%s, %s, %s)"

tender_data1 = ('Building a house', 'Building a house near the road', '2023-07-12')
tender_data2 = ('Construction of a new school building ', 'The project involves the construction of a new school building with classrooms, offices, and a gymnasium.', '2023-08-02')
tender_data3 = ('Supply and installation of solar panels', 'The tender is for the supply and installation of solar panels to power a new office building.', '2023-07-12')
tender_data4 = ('Renovation of a historic landmark building', 'Building a house near the road', '2023-07-12')
tender_data5 = ('Construction of a new bridge', 'The tender is for the construction of a new bridge over a river, including the design, engineering, and construction.', '2023-07-12')
tender_data6 = ('Provision of security services', 'The tender is for the provision of security services to a commercial building, including security personnel, equipment, and monitoring.', '2023-07-12')
tender_data7 = ('Construction of a new hospital', 'The tender is for the construction of a new hospital with specialized facilities and equipment.', '2023-07-12')
tender_data8 = ('Renovation of an existing office building', 'The tender is for the renovation of an existing office building to make it more energy-efficient and environmentally friendly.', '2023-07-12')
tender_data9 = ('Installation of a new HVAC system', 'The tender is for the installation of a new HVAC (heating, ventilation, and air conditioning) system in a commercial building.', '2023-07-12')
tender_data10 = ('Construction of a new shopping center', 'The tender is for the construction of a new shopping center with multiple stores and a parking area.', '2023-07-12')
tender_data11 = ('Provision of IT services', 'The tender is for the provision of IT (information technology) services to a government agency, including hardware, software, and technical support.', '2023-07-12')

tender_data = [tender_data1, tender_data2, tender_data3, tender_data4, tender_data5, tender_data6, tender_data7, tender_data8, tender_data9, tender_data10, tender_data11]

for data in tender_data:
    cursor.execute(add_tender, data)
    db.commit()

query = "SELECT id, title, description, closing_date FROM tenders ORDER BY closing_date DESC"
cursor.execute(query)

for (id, title, description, closing_date) in cursor:
    print(f"Tender {id}: {title}\nDescription: {description}\nClosing date: {closing_date}\n")

# Close the database connection
cursor.close()
db.close()
