import sys

number_qty = int(input())

counter = 0
number_min = sys.maxsize

while counter < number_qty:
    number = int(input())
    if number_min > number:
        number_min = number
    counter += 1

print(number_min)
