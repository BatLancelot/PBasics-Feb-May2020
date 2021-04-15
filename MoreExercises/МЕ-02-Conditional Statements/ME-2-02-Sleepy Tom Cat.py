import math

days_off = int(input())

toms_norm = 30000
min_work = 63
min_day_off = 127
year = 365

work_days = year - days_off
total_play_minutes = work_days * min_work + days_off * min_day_off

norm_difference = math.fabs(total_play_minutes - toms_norm)
hours = math.floor(norm_difference / 60)
minutes = math.floor(norm_difference % 60)

if total_play_minutes > toms_norm:
    print('Tom will run away')
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
