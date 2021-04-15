fruit = input()
day = input()
amount = float(input())

entry_is_valid = True

price = 0

if day == 'Monday' or day == 'Tuesday'\
        or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = amount * 2.5
    elif fruit == 'apple':
        price = amount * 1.2
    elif fruit == 'orange':
        price = amount * 0.85
    elif fruit == 'grapefruit':
        price = amount * 1.45
    elif fruit == 'kiwi':
        price = amount * 2.70
    elif fruit == 'pineapple':
        price = amount * 5.5
    elif fruit == 'grapes':
        price = amount * 3.85
    else:
        entry_is_valid = False
        print('error')

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = amount * 2.7
    elif fruit == 'apple':
        price = amount * 1.25
    elif fruit == 'orange':
        price = amount * 0.9
    elif fruit == 'grapefruit':
        price = amount * 1.60
    elif fruit == 'kiwi':
        price = amount * 3
    elif fruit == 'pineapple':
        price = amount * 5.6
    elif fruit == 'grapes':
        price = amount * 4.2
    else:
        entry_is_valid = False
        print('error')
else:
    entry_is_valid = False
    print('error')

if entry_is_valid:
    print(f'{price:.2f}')
