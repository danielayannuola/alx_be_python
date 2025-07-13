monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input ("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses
Annual_savings = monthly_savings * 12 
interest = Annual_savings * 0.05
projected_savings = Annual_savings + interest

print(f"Your monthly savings are ${monthly_savings}.")
print(f"projected savings after one year, with interest, is: ${projected_savings}.")