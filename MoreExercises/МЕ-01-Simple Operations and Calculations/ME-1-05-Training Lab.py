import math

lenght_w = float(input())
heigth_h = float(input())

seats_w = lenght_w / 1.2
seats_w_int = math.trunc(seats_w)
seats_h = (heigth_h - 1) / 0.7
seats_h_int = math.trunc(seats_h)
available_seats = seats_w_int * seats_h_int - 3

print(f'{available_seats:.0f}')
