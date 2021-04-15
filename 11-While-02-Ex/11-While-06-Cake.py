cake_width = int(input())
cake_length = int(input())

cake_pcs = cake_length * cake_width
taken_psc = 0
guest_takes = ''

while guest_takes != 'STOP':
    guest_takes = input()

    if guest_takes == 'STOP':
        pcs_left = cake_pcs - taken_psc
        print(f'{pcs_left} pieces are left.')
        break

    taken_psc += int(guest_takes)

    if cake_pcs < taken_psc:
        pcs_needed = taken_psc - cake_pcs
        print(f'No more cake left! You need {pcs_needed} pieces more.')
        break
