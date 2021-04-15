steps_walked = input()

goal = 10000

while steps_walked != 'Going home':
    steps_walked = int(steps_walked)
    goal -= steps_walked
    if goal <= 0:
        print(f'Goal reached! Good job!')
        break

    steps_walked = input()

    if steps_walked == 'Going home':
        steps_walked = int(input())
        goal -= steps_walked
        if goal <= 0:
            print(f'Goal reached! Good job!')
        else:
            print(f'{goal} more steps to reach goal.')
        break
