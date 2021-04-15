tries = int(input())

left_sum = 0
for _ in range(tries):
    number = int(input())
    left_sum += number

right_sum = 0
for _ in range(tries):
    number = int(input())
    right_sum += number


if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
