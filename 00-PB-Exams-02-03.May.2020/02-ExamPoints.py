exercise = int(input())
points = int(input())
cource = input()

total_points = 0

if cource  == 'Basics':
    if exercise == 1:
        points *= 0.08
        total_points = points * 0.8
    elif exercise == 2 or exercise == 3:
        total_points = points * 0.09
    else:
        total_points = points * 0.10

if cource  == 'Fundamentals':
    if exercise == 1 or exercise == 2:
        total_points = points * 0.11
    elif exercise == 3:
        total_points = points * 0.12
    else:
        total_points = points * 0.13

if cource  == 'Advanced':
    if exercise == 1 or exercise == 2:
        points *= 0.14
        total_points = points * 1.20
    elif exercise == 3:
        points *= 0.15
        total_points = points * 1.20
    else:
        points *= 0.16
        total_points = points * 1.20

print(f'Total points: {total_points:.2f}')
