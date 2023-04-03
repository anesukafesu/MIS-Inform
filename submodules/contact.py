from database import create_cursor


def contacts():
    """
    Display contact information of key government departments. The contact information should include the name of the department, the physical address, the email, the website and the telephone number. Try to include ministries and critical agencies such as the Rwanda Development Board and the Rwanda National Police. Also include emergency numbers such as the ambulance, fire department and police.

    Sample output
    Ministry of Finance and Economic Planning
    Website: minecofin.gov.rw
    Telephone: +250 252 577 581
    Physical Address: 12 KN3 Ave, Kigali

    Database
    Table: contact
    Schema:

    name (string), e.g. Ministry of Finance and Economic Planning
    website (string), e.g. minecofin.gov.rw
    email (string), e.g. info@minecofin.gov.rw
    tel (string), e.g. +250 252 577 581
    physical_address (string), e.g. 12 KN3 Ave, Kigali
    """
    cursor, db = create_cursor()
    cursor.execute('SELECT * FROM contacts')

    for name, website, email, tel, physical_address in cursor:
        print('Department name:', name)
        print('Website:', website)
        print('Email:', email)
        print('Tel:', tel)
        print('Physical Address:', physical_address)
        print("")
