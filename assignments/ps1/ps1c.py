# 假设您想设定一个特定目标，例如能够在三年内负担得起首付。您每个月应该储蓄多少钱才能实现这一目标？

start_salary = float(input("Enter the starting salary: "))
annual_salary = start_salary
total_cost = 1000000
portion_down_payment = 0.25  # 首付
down_payment = total_cost * portion_down_payment  # 首付金额
semi_annual_raise = 0.07  # 每半年加薪一次
r = 0.04  # annual return
monthly_salary = annual_salary / 12
month = 36


# 定义一个函数针对每次猜测的portion_saved值计算3年积蓄总额
def simulate_savings(portion_saved):
    # 每次猜测前记得把上一次算的积蓄清零，并让年薪和月薪重置为初始值
    current_savings = 0.0
    annual_salary = start_salary
    monthly_salary = annual_salary / 12
    for i in range(1, month + 1):
        current_savings += current_savings * r / 12 + monthly_salary * portion_saved / 10000.0
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    return current_savings


# 对于某些工资来说，一年半内可能无法存下首付
if simulate_savings(10000) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    # 使用 0 到 10000 的原因是为了在 0% 到 100% 的范围内多保留两位小数，并且搜索的数字是有限个
    steps = 0  # 统计bisection search的步数
    low = 0
    high = 10000
    epsilon = 10  # 设定一个足够小的值，以确保我们能找到正确的答案
    portion_saved = (high + low) / 2.0
    while abs(simulate_savings(portion_saved) - down_payment) >= epsilon:
        if simulate_savings(portion_saved) < down_payment:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high + low) / 2.0
        steps += 1
    print("Best savings rate: ", portion_saved / 10000)
    print("Steps in bisection search: ", steps)
