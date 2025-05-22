monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 * 1.05  # 5% interest on total savings after a year
print(f"Projected savings after one year, with interest, is: {projected_savings:.2f}")