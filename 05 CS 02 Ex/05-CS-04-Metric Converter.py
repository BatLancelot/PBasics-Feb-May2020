unit = float(input())
unit_a = input()
unit_b = input()

if unit_a == 'mm':
    if unit_b == 'cm':
        result = unit / 10
    elif unit_b == 'm':
        result = unit / 1000

if unit_a == 'cm':
    if unit_b == 'm':
        result = unit / 100
    elif unit_b == 'mm':
        result = unit * 10

if unit_a == 'm':
    if unit_b == 'mm':
        result = unit * 1000
    elif unit_b == 'cm':
        result = unit * 100

print(f'{result:.3f}')
