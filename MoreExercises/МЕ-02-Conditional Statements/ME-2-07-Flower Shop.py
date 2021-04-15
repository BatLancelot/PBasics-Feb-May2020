import math

num_magnolii = int(input())
num_zumbuli = int(input())
num_roses = int(input())
num_cactus = int(input())
present_price = float(input())

magnolii = 3.25
zumbuli = 4
roses = 3.5
cactus = 8
taxes = 0.05

order = (num_magnolii * magnolii) + (num_zumbuli * zumbuli) + (num_roses * roses) + (num_cactus * cactus)
income = order - (order * taxes)
money_left = abs(income - present_price)

if present_price <= income:
    print(f'She is left with {math.floor(money_left)} leva.')
else:
    print(f'She will have to borrow {math.ceil(money_left)} leva.')
