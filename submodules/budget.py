"""
BUDGET SUBMODULE:
    FEATURES:
        1 - Yearly Budget of the Rwandan Government.
        2 - Yearly Allocation and Expenditure of the Rwandan Government.
        3 - Yearly Revenues of the Rwandan Government
"""

from database import create_cursor

cursor, db = create_cursor()

def create_tables():

    cursor.execute("DROP TABLE IF EXISTS Budgets")
    cursor.execute("DROP TABLE IF EXISTS Allocations")
    cursor.execute("DROP TABLE IF EXISTS Revenues")

    # CREATE TABLE Budgets IF NOT EXIST
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Budgets (year YEAR NOT NULL, amount FLOAT(5) NOT NULL)")
    # INSERT VALUES
    sql = "INSERT IGNORE INTO Budgets (year, amount) VALUES (%s, %s)"
    val = [
        (2021, 3.2457),
        (2020, 3.2457),
        (2019, 2.8784),
        (2018, 2.4435),
        (2017, 2.0945),
        (2016, 1.9494),
        (2015, 1.7002),
        (2014, 1.5699),
        (2013, 1.3168),
        (2012, 1.1843)
    ]
    cursor.executemany(sql, val)

    # CREATE TABLE Allocation IF NOT EXIST
    cursor.execute("CREATE TABLE IF NOT EXISTS Allocations (year YEAR NOT NULL, education FLOAT(5) NOT NULL, health FLOAT(4) NOT NULL,\
                infrastructure FLOAT(4) NOT NULL, agriculture FLOAT(4) NOT NULL)")
    # INSERT VALUES
    sql = "INSERT IGNORE INTO Allocations (year, education, health, infrastructure, agriculture) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (2021, 17.8, 11.5, 24.2, 5.5),
        (2020, 16.5, 10.2, 26.0, 5.1),
        (2019, 16.6, 9.6, 24.8, 5.2),
        (2018, 16.4, 9.1, 26.0, 4.9),
        (2017, 16.0, 9.4, 26.0,	4.9),
        (2016, 16.6, 9.1, 25.1,	5.2),
        (2015, 16.2, 9.7, 23.5,	6.0),
        (2014, 16.0, 9.5, 23.7,	5.9),
        (2013, 16.2, 8.7, 23.5,	6.3),
        (2012, 16.3, 8.5, 22.7,	6.4)
    ]
    cursor.executemany(sql, val)

    # CREATE TABLE Revenues IF NOT EXIST
    cursor.execute("CREATE TABLE IF NOT EXISTS Revenues (year YEAR NOT NULL, tax_revenue FLOAT(5) NOT NULL, grants FLOAT(5) NOT NULL, loans FLOAT(5) NOT NULL, non_tax_revenue FLOAT(5) NOT NULL)")
    sql = "INSERT IGNORE INTO Revenues (year, tax_revenue, grants, loans, non_tax_revenue) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (2021, 1705.9, 771.1, 2395.6, 57.3),
        (2020, 1424.9, 641.8, 2228.5, 65.4),
        (2019, 1350.9, 563.3, 2098.4, 61.1),
        (2018, 1240.7, 511.8, 1820.1, 47.1),
        (2017, 1113.4, 500.3, 1467.4, 41.2),
        (2016, 1054.7, 462.6, 1389.6, 48.8),
        (2015, 945.1, 404.2, 1238.2, 34.3),
        (2014, 849.6, 386.8, 1155.5, 40.3),
        (2013, 772.9, 347.1, 905.5,	47.6),
        (2012, 678.9, 357.6, 616.5,	44.6)
    ]
    cursor.executemany(sql, val)
    db.commit()


Budget_request_template = """
        THE RWANDAN GOVERNMENT BUDGET FOR THE YEAR {} - OVERVIEW
    The Rwandan government's budget for the year {} was RWF {} trillion,
    which is equivalent to USD {} billion, according to the approved budget by the parliament.

    KEY ALLOCATIONS:
    Prioritization in resource allocation to various sectors such as Education, Health, Infrastructural
    Development, Economic Tranformation, Scaling of ICT and Agriculture.
"""

Allocation_request_template = """
        THE RWANDAN GOVERNMENT BUDGET ALLOCATION FOR THE YEAR {} - OVERVIEW
    The Budget allocation for Education, Health, Infrastructural Development, and 
    Agriculture for the year {} went as follows:

    - Education: {}%
    - Health: {}%
    - Infrastructural Development: {}%
    - Agriculture: {}%

    These are a few among many other priorities of the Rwandan Government for the year {}.
"""

Revenue_request_template = """
        THE RWANDAN GOVERNMENT SOURCES OF REVENUE FOR THE YEAR {} - OVERVIEW
    The sources of revenue for the Rwandan Govertnement for the year {} was as follows:

    - Tax Revenue: Frw {} Billion
    - Grants: Frw {} Billion
    - Loans: Frw {} Billion
    - Non-Tax Revenue: Frw {} Billion
"""

def get_budget(year=2021):
    """
    Get the budget of the Rwandan Govt for the specified year
        - params: year(date)
        - range: 2012 to 2021
    """
    try:
        if not isinstance(year,  int):
            raise ValueError
        if year < 2012 or year > 2021:
            raise Exception
        
    except ValueError:
        return 'Year must be a digit!'
    except Exception:
        return 'Please Input a year between 2021 and 2012(Both inclusive)'
    
    else:
        sql = "SELECT * FROM Budgets WHERE year = %s"
        year = (year,)
        cursor.execute(sql, year)
        res = cursor.fetchall()
        row = res[0]
        return Budget_request_template.format(row[0], row[0], row[1], round((row[1]/1094), 3))


def get_allocations(year=2021):
    """
    Get the budget allocations for each sector for the specified year
        - params: year(date)
        - range: 2012 to 2021
    """
    try:
        if not isinstance(year,  int):
            raise ValueError
        if year < 2012 or year > 2021:
            raise Exception
        
    except ValueError:
        return 'Year must be a digit!'
    except Exception:
        return 'Please Input a year between 2021 and 2012(Both inclusive)'
    
    else:
        sql = "SELECT * FROM Allocations WHERE year = %s"
        year = (year,)
        cursor.execute(sql, year)
        res = cursor.fetchall()
        print(res)
        row = res[0]
        return Allocation_request_template.format(row[0], row[0], row[1], row[2], row[3], row[4], row[0])



def get_revenue(year=2021):
    """
    Get the revenue sources for the specified year
        - params: year(date)
        - range: 2012 to 2021
    """

    try:
        if not isinstance(year,  int):
            raise ValueError
        if year < 2012 or year > 2021:
            raise Exception
        
    except ValueError:
        return 'Year must be a digit!'
    except Exception:
        return 'Please Input a year between 2021 and 2012(Both inclusive)'
    
    else:
        sql = "SELECT * FROM Revenues WHERE year = %s"
        year = (year,)
        cursor.execute(sql, year)
        res = cursor.fetchall()
        row = res[0]
        return Revenue_request_template.format(row[0], row[0], row[1], row[2], row[3], row[4])

if __name__ == '__main__':
    print('Budget Submodule')
