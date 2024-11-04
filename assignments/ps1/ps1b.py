annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi_annual_raise, as a decimal: "))
portion_down_payment = 0.25  #首付
monthly_salary = annual_salary/12
r = 0.04
current_savings = 0
month = 0
while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings*r/12 + monthly_salary*portion_saved
    month += 1
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary/12
print("Number of months: ", month)
