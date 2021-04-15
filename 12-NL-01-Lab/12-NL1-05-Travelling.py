destination = input()
while destination != 'End':
    budget = float(input())
    savings = 0
    while savings < budget:
        savings += float(input())
    print(f'Going to {destination}!')
    destination = input()
