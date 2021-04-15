import math

hours = int(input())
days = int(input())
workers = int(input())

real_working_hours = (days * 0.9) * 8
overtime = workers * (days * 2)

total_working_hours = math.floor(real_working_hours + overtime)
difference = abs(hours - total_working_hours)

if hours <= total_working_hours:
    print(f'Yes!{difference} hours left.')
else:
    print(f'Not enough time!{difference} hours needed.')
