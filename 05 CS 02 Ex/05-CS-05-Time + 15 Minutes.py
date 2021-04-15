hour = int(input())
minutes = int(input())

hour = hour * 60
minutes = minutes + 15

time_after_x_min = hour + minutes

hour_after = time_after_x_min // 60
minutes_after = time_after_x_min % 60

if hour_after == 24:
    hour_after = 0

if minutes_after < 10:
    print(f'{hour_after}:{minutes_after:0>2d}')
else:
    print(f'{hour_after}:{minutes_after}')
