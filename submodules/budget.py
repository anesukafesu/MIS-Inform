"""
BUDGET SUBMODULE:
    FEATURES:
        1 - Yearly Budget of the Rwandan Government.
        2 - Yearly Allocation and Expenditure of the Rwandan Government.
        3 - Yearly Revenues of the Rwandan Government
"""


def budget():
    sources = ["Taxes", "Loans", "Donations", "Other Sources"]
    amounts = []
    for i in range(len(sources)):
        amount = float(input(f"Enter the amount of {sources[i]}: "))
        amounts.append(amount)

    total_income = sum(amounts)

    expenses = ["Rent", "Utilities", "Salaries", "Supplies", "Other Expenses"]
    expense_amounts = []
    for i in range(len(expenses)):
        amount = float(input(f"Enter the amount of {expenses[i]}: "))
        expense_amounts.append(amount)

    total_expenses = sum(expense_amounts)

    annual_budget = total_income - total_expenses

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    return annual_budget

# GET ALL THE DETAILS BY YEAR
# -> Budgets: Year | Budget | % Increment |
# -> Allocations: Year | Education | Health | Infrastructure development | Agriculture
# -> Revenues: Year | Tax Revenue | Grants and Loans | Non-Tax Revenue


class Budget_Class():
    """
    This class embodies the attributes and features associated with the
    yearly fiscal budget of the Rwandan Government.
    """

    def __init__(self):
        """
        Initializes every instance
        """
        pass

    def get_budget(self, year=2023):
        """
        Get the budget of the Rwandan Govt for the specified year
            - params: year(date)
        """
        return year

    def get_allocations(self, year=2023):
        """
        Get the budget allocations for each sector for the specified year
            - params: year(date)
        """
        return year

    def get_revenues(self, year=2023):
        """
        Get the revenue sources for the specified year
            - params: year(date)
        """
        return year

Budget = Budget_Class()

if __name__ == '__main__':
    print('Budget Submodule')