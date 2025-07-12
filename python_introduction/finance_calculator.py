monthly_income = float (input("Enter your monthly income:"))
monthly_expenses = float (input("Enter your monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses

projected_saving =monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly saving are $", monthly_savings)
print("Projected saving after one year, with interest, is $", projected_saving)
