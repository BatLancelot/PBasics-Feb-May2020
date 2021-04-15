from math import floor

year_type = input()
holidays = int(input())
weekends = int(input())

sofia_games = (48 - weekends) * 3/4
holiday_games = holidays * 2/3
total_games = sofia_games + holiday_games + weekends

if year_type == 'leap':
    total_games *= 1.15
    print(floor(total_games))
else:
    print(floor(total_games))
