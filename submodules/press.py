import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(
    user='negpod5',
    password='password',
    port=3306,
    host='129.151.170.34',
    database='pld'
)

cursor = cnx.cursor()


def view_data_by_source(source_str):
    try:
        query = '''
        SELECT title, author, publication_date, publisher, content
        FROM press
        WHERE source LIKE %s
        '''

        cursor.execute(query, ("%" + source_str + "%",))
        result = cursor.fetchall()

        if len(result) == 0:
            print("No articles found.")
            return
        else:
            print()
            print("Press articles from " + source_str)
            print()
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
