budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter"
num_fisherman = int(input())

price = 0

if season == 'Spring':
    price = 3000
elif season == 'Winter':
    price = 2600
elif season == 'Summer' or season == 'Autumn':
    price = 4200


if num_fisherman <= 6:
    price *= 0.9
    if num_fisherman % 2 == 0 and season != 'Autumn':
        price *= 0.95
elif 7 < num_fisherman <= 11:
    price *= 0.85
    if num_fisherman % 2 == 0 and season != 'Autumn':
        price *= 0.95
elif num_fisherman > 12:
    price *= 0.75
    if num_fisherman % 2 == 0 and season != 'Autumn':
        price *= 0.95

money_left = abs(budget - price)
if budget >= price:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')
