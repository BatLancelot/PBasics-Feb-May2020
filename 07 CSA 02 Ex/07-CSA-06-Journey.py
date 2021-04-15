budget = float(input())
season = input()  # „summer” или “winter”

destination = ''
vacation = ''

if season == 'summer':
    if budget <= 100:
        destination = 'Bulgaria'
        vacation = 'Camp'
        budget *= 0.3
    elif budget <= 1000:
        destination = 'Balkans'
        vacation = 'Camp'
        budget *= 0.4
    elif budget > 1000:
        destination = 'Europe'
        vacation = 'Hotel'
        budget *= 0.9
else:
    if budget <= 100:
        destination = 'Bulgaria'
        vacation = 'Hotel'
        budget *= 0.7
    elif budget <= 1000:
        destination = 'Balkans'
        vacation = 'Hotel'
        budget *= 0.8
    elif budget > 1000:
        destination = 'Europe'
        vacation = 'Hotel'
        budget *= 0.9

print(f'Somewhere in {destination}\n'
      f'{vacation} - {budget:.2f}')
