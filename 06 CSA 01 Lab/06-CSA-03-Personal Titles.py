age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print('Mr.')
    elif age < 16:
        print('Master')
    else:
        pass
elif gender == 'f':
    if age >= 16:
        print('Ms.')
    elif age < 16:
        print('Miss')
    else:
        pass
