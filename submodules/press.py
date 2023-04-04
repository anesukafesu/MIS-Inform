import mysql.connector

my_data = [
    {'title': 'Kenyan President William Ruto to visit Rwanda', 'author': 'J.D. Salinger', 'publication_date': '2023-04-03',
        'publisher': 'Little, Brown and Company', 'content': 'President William Ruto of Kenya is scheduled to begin a two-day state visit to Rwanda on April 4th, 2023. During his trip, he plans to meet with the Kenyan diaspora residing in Rwanda to discuss matters concerning the diaspora and government policies.',
        'source': 'https://en.igihe.com/news/article/kenyan-president-for-two-day-visit-to-rwanda'},
    {'title': 'Rwanda and Uganda commit to joint efforts in fighting ADF and FDLR', 'author': 'Harper Lee', 'publication_date': '1960-03-27',
        'publisher': 'J. B. Lippincott &amp; Co.', 'content': 'Rwanda and Uganda have committed to working together to find a solution to security problems in eastern part of the Democratic Republic of Congo (DRC) which is home to armed groups including the Allied Democratic Forces (ADF) and the Democratic Forces for the Liberation of Rwanda (FDLR) that pose threats to both countries security.',
        'source': 'https://en.igihe.com/news/article/rwanda-and-uganda-commit-to-joint-efforts-in-fighting-adf-and-fdlr-in-eastern'},
    {'title': 'Fuel prices go down', 'author': 'Aurore Teta Ufitiwabo', 'publication_date': '2023-04-03', 'publisher': 'Secker &amp; Warburg.',
        'content': 'Newly announced prices for petroleum products will see a litre of gasoline costing Rwf1,528, down from 1,544, the Rwanda Utilities Regulatory Authority (RURA) announced on April 2. It is also noted that a litre of diesel will cost Rwf1,518, down from Rwf1,562.',
        'source': 'https://www.newtimes.co.rw/article/6370/news/energy/fuel-prices-go-down'},
]

# Connect to the MySQL server
cnx = mysql.connector.connect(
    user='negpod5',
    password='password',
    port=3306,
    host='129.151.170.34',
    database='pld'
)

cursor = cnx.cursor()


def create_press_table(data):
    create_table = '''
    CREATE TABLE if not exists press (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255),
        publication_date DATE,
        publisher VARCHAR(255),
        content TEXT, 
        source VARCHAR(255)
    )
    '''
    cursor.execute(create_table)
    cursor.execute("SELECT COUNT(*) FROM press")
    count = cursor.fetchone()[0]

    # If the table is empty, insert the data
    if count == 0:
        insert_data = '''
        INSERT INTO press (title, author, publication_date, publisher, content, source)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        for row in data:
            values = values = (row['title'], row.get('author'), row.get(
                'publication_date'), row.get('publisher'), row.get('content'), row.get('source'))
            cursor.execute(insert_data, values)

        cnx.commit()


def view_data_by_source(source_str):
    try:
        query = '''
        SELECT title, author, publication_date, publisher, content
        FROM press
        WHERE source LIKE %s
        '''

        cursor.execute(query, ("%" + source_str + "%",))
        result = cursor.fetchall()

        for row in result:
            print("Title:", row[0])
            print("Author:", row[1])
            print("Publication Date:", row[2])
            print("Publisher:", row[3])
            print("Content:", row[4])
            print()

    except Exception as e:
        print("Error: ", e)


def press():
    create_press_table(my_data)

    print("Select a source to view press articles:")
    print("1. The New Times")
    print("2. Igihe")
    print("3. Kigali Today")

    selection = input("Enter your selection: ")
    if selection == '1':
        view_data_by_source('https://www.newtimes.co.rw/')
    elif selection == '2':
        view_data_by_source('https://en.igihe.com/')
    elif selection == '3':
        view_data_by_source('https://www.kigalitoday.com/')
    else:
        print("Invalid selection.")


press()

cursor.close()
cnx.close()
