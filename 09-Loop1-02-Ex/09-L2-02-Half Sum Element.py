n = int(input())

max_num = -500000000
sum_numbers = 0

for i in range(0, n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum_numbers += number

sum_numbers = sum_numbers - max_num

if max_num == sum_numbers:
    print(f'Yes\nSum= {sum_numbers}')
else:
    print(f'No\nDiff= {abs(max_num - sum_numbers)}')
