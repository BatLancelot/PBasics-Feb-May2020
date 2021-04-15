product = input()
city = input()
amount = float(input())

if city == 'Sofia':
    if product == 'coffee':
        price = amount * 0.5
    elif product == 'water':
        price = amount * 0.8
    elif product == 'beer':
        price = amount * 1.2
    elif product == 'sweets':
        price = amount * 1.45
    elif product == 'peanuts':
        price = amount * 1.60
    else:
        pass

elif city == 'Plovdiv':
    if product == 'coffee':
        price = amount * 0.4
    elif product == 'water':
        price = amount * 0.7
    elif product == 'beer':
        price = amount * 1.15
    elif product == 'sweets':
        price = amount * 1.3
    elif product == 'peanuts':
        price = amount * 1.50
    else:
        pass

elif city == 'Varna':
    if product == 'coffee':
        price = amount * 0.45
    elif product == 'water':
        price = amount * 0.7
    elif product == 'beer':
        price = amount * 1.1
    elif product == 'sweets':
        price = amount * 1.35
    elif product == 'peanuts':
        price = amount * 1.55
    else:
        pass

print(f'{price:.2f}')
