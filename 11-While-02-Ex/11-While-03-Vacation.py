money_for_excursion = float(input())
savings = float(input())

days_counter = 0
spend_counter = 0

while savings < money_for_excursion:
    spend_save = input()
    days_counter += 1

    if spend_save == 'spend':
        amount = float(input())
        savings -= amount
        spend_counter += 1
        if savings < 0:
            savings = 0
    else:
        amount = float(input())
        savings += amount
        spend_counter = 0

    if spend_counter == 5:
        print('You can\'t save the money.')
        print(f'{days_counter}')
        break

if savings >= money_for_excursion:
    print(f'You saved the money for {days_counter} days.')
