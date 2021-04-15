type_of = input()
rows = int(input())
columns = int(input())
price = 0

if type_of == 'Premiere':
    price = rows * columns * 12.00
elif type_of == 'Normal':
    price = rows * columns * 7.50
elif type_of == 'Discount':
    price = rows * columns * 5.00
print(f'{price:.2f}')
