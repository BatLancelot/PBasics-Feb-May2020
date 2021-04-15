fuel = input()
liters = float(input())

if fuel == 'Diesel' or fuel == 'Gasoline' or fuel == 'Gas':
    if 25 <= liters:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')
