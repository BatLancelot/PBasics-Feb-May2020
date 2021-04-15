tries = int(input())

even_sum = 0
odd_sum = 0

for _ in range(tries):
    number = int(input())
    if _ % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print(f'Yes\n'
          f'Sum = {even_sum}')
else:
    diff = abs(even_sum - odd_sum)
    print(f'No\n'
          f'Diff = {diff}')
