"""
BUDGET SUBMODULE:
    FEATURES:
        1 - Yearly Budget of the Rwandan Government.
        2 - Yearly Allocation and Expenditure of the Rwandan Government.
        3 - Yearly Revenues of the Rwandan Government
"""

from submodules.database import create_cursor

cursor, db = create_cursor()

def budget():
    year = input('Enter the a year ')
    return """
                                OVERVIEW
        The Rwandan Government makes her annual budgets around essential pillars
        of the nation according to the priorities for each year. 
        Budgets are mainly structured around Economic recovery, Human Development, 
        Strategic Intervention for growth, Educatiion, Health, Infrastructural
        Development, Good governance, Agriculture, etc.
        Each year budget of the Rwandan Government majorly aim to promote sustainable 
        economic growth and, improve the well-being of the Rwandan citizens.
         
    """

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