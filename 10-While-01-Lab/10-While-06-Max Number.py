import sys

number_qty = int(input())

counter = 0
number_max = -sys.maxsize

while counter < number_qty:
    number = int(input())
    if number_max < number:
        number_max = number
    counter += 1

print(number_max)
