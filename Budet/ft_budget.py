def create_budget():
    sources = ["Taxes", "Loans", "Donations", "Other Sources"]
    amounts = []
    for i in range(len(sources)):
        amount = float(input(f"Enter the amount of {sources[i]}: "))
        amounts.append(amount)

    total_income = sum(amounts)

  
    return total_income
            