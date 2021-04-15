days = int(input())
room = input()
score = input()

nights = days - 1
price = 0

if room == 'room for one person':
    price = nights * 18
elif room == 'apartment':
    if days < 10:
        price = (nights * 25) * 0.70
    elif 10 < days < 15:
        price = (nights * 25) * 0.65
    elif days > 15:
        price = (nights * 25) * 0.5
elif room == 'president apartment':
    if days < 10:
        price = (nights * 35) * 0.9
    elif 10 < days < 15:
        price = (nights * 35) * 0.85
    elif days > 15:
        price = (nights * 35) * 0.8
else:
    print('wrong room type')

if score == 'positive' and room != 'room for one person':
    price = price * 1.25
else:
    price = price * 0.9

print(f'{price:.2f}')
