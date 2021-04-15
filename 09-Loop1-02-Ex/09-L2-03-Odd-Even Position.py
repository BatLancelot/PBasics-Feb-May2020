import sys

n = int(input())

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 ==0:
        even_sum += number
        if even_max < number:
            even_max = number
        if even_min > number:
            even_min = number
    else:
        odd_sum += number
        if odd_max < number:
            odd_max = number
        if odd_min > number:
            odd_min = number

print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
