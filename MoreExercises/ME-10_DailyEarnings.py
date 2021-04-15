work_days = int(input())
money_per_day = float(input())
usd_rate = float(input())

monthly_salary = work_days * money_per_day
bonus = monthly_salary * 2.5
year_income = monthly_salary * 12 + bonus
taxes = year_income * 0.25

profit_per_year = year_income - taxes
profit_per_day = (profit_per_year / 365) * usd_rate

print(f'{profit_per_day:.2f}')
