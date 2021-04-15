flower_type = input()
flower_qty = int(input())
budget = int(input())

price = 0.00

if flower_type == 'Roses':
    price = 5
    if flower_qty > 80:
        price *= 0.90
elif flower_type == 'Dahlias':
    price = 3.80
    if flower_qty > 90:
        price *= 0.85
elif flower_type == 'Tulips':
    price = 2.80
    if flower_qty > 80:
        price *= 0.85
elif flower_type == 'Narcissus':
    price = 3
    if flower_qty < 120:
        price += price * 0.15
elif flower_type == 'Gladiolus':
    price = 2.50
    if flower_qty < 80:
        price += price * 0.20

total_price = price * flower_qty
money_left = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_qty} {flower_type} and {money_left:.2f} leva left.')
else:
    print(f'Not enough money, you need {money_left:.2f} leva more.')
