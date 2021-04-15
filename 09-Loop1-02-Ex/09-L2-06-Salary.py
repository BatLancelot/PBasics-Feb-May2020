n = int(input())
salary = int(input())

tabs_sum = 0

for i in range(0, n):
    tabs = input()
    if tabs == 'Facebook':
        tabs_sum += 150
    elif tabs == 'Instagram':
        tabs_sum += 100
    elif tabs == 'Reddit':
        tabs_sum += 50
    if tabs_sum >= salary:
        print('You have lost your salary.')
        break

salary = salary - tabs_sum
if salary > 0:
    print(f'{salary}')
