#!/usr/bin/python3
from database import create_cursor


def economy(economic_data):
    cursor, db = create_cursor()
    cursor.execute('SELECT * FROM economy')
    # define economic information as a dictionary
    economic_data = {
        "gdp": "$18bn",
        "gdp_per_capita": "$2,200",
        "inflation": 9.85,
        "unemployment": 13.1,
        "interest_rate": 2.75,
        "stock_market": 3450,
        "gdp_growth": 10.88,
        "inflation_forecast": 9.5,
        "debt": "$2.8bn",
        "gdp_ppp": "$30.14bn",
        "exchange": "$9.13bn",
        "credit_rating": "B+",
        "industrial_growth": 13.8,
        "labor": "6.7 million",
        "poverty": 38.2,
        "family_income": 43.7,
        "account_balance": "$-1.20bn",
        "exports": "$2.1bn",
        "imports": "$3.8bn",
        "reserves": "$1.89bn",
    }


    while True:
        # display economic information to user
        print(f"GDP: {economic_data['gdp']}")
        print(f"Inflation: {economic_data['inflation']}")
        print(f"Unemployment: {economic_data['unemployment']}")
        print(f"GDP PPP: {economic_data['gdp_ppp']}")
        print(f"GDP per capita: {economic_data['gdp_per_capita']}")
        print(f"Exchange rates: {economic_data['exchange']}")

    # prompt user for more information or to quit
        choice = input(
        "Enter 'm' for more detailed information, 'p' for projections, or 'q' to quit: "
    )

        # based on user input, display more information or projections or quit
        if choice == "m":
            # display more detailed information
            print(f"Interest rate: {economic_data['interest_rate']}")
            print(f"Stock market: {economic_data['stock_market']}")
            print(f"Debt(external):{economic_data['debt']}")
            print(f"Family Income Distribution: {economic_data['family_income']}")
            print(f"Imports: {economic_data['imports']}")
            print(f"Exports: {economic_data['exports']}")
            print(f"Foreign Reserves: {economic_data['reserves']}")
            print(f"Poverty: {economic_data['poverty']}")
            print(f"Credit Rating: {economic_data['credit_rating']}")
            print(f"Industrial Growth: {economic_data['industrial_growth']}")
            print(f"Laborforce: {economic_data['labor']}")
            print(f"Account balance: {economic_data['account_balance']}")
        elif choice == "p":
            # display projections
            print(f"GDP growth forecast: {economic_data['gdp_growth']}")
            print(f"Inflation forecast: {economic_data['inflation_forecast']}")
            print(f"Unemployment Projections: -0.35")
        elif choice == "q":
            # quit and go back to main page
            break
        else:
            # handle invalid input
            print("Invalid input. Please enter 'm', 'p', or 'q'.")

print("Back to the main page.")
