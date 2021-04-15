first_num = int(input())
second_num = int(input())
operator = input()  # "+", "-", "*", "/", "%".

result = 0
even_odd = 0
if operator == '+':
    result = first_num + second_num
    even_odd = result % 2
    if even_odd == 0:
        even_odd = 'even'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
elif operator == '-':
    result = first_num - second_num
    even_odd = result % 2
    if even_odd == 0:
        even_odd = 'even'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
elif operator == '*':
    result = first_num * second_num
    even_odd = result % 2
    if even_odd == 0:
        even_odd = 'even'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
    else:
        even_odd = 'odd'
        print(f'{first_num} {operator} {second_num} = {result} - {even_odd}')
elif operator == '/':
    if second_num == 0:
        print(f'Cannot divide {first_num} by zero')
    else:
        result = first_num / second_num
        print(f'{first_num} / {second_num} = {result:.2f}')
elif operator == '%':
    if second_num == 0:
        print(f'Cannot divide {first_num} by zero')
    else:
        result = first_num % second_num
        print(f'{first_num} % {second_num} = {result}')
