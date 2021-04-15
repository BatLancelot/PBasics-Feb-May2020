from math import pi

figure = input()

if figure == 'square':
    x_side = float(input())
    result = x_side * x_side
elif figure == 'rectangle':
    x_side = float(input())
    y_side = float(input())
    result = x_side * y_side
elif figure == 'circle':
    radius = float(input())
    result = pi * radius ** 2
elif figure == 'triangle':
    x_side = float(input())
    h_height = float(input())
    result = x_side * h_height / 2
print(f'{result:.3f}')
