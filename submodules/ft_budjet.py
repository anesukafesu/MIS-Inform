def create_budget():
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

    return annual_budget