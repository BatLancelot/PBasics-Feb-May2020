
budget = float(input())
extras = int(input())
cloth_price = float(input())

set = budget * 0.1

if extras > 150:
    cloth_price *= 0.9

total_cloth_price = extras * cloth_price

expenses = set + total_cloth_price
money_left = abs(budget -expenses)

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
