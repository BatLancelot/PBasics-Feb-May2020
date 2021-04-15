first_num = int(input())
second_num = int(input())
third_num = int(input())

total_time = first_num + second_num + third_num

total_min = total_time // 60
total_sec = total_time % 60

if total_sec < 10:
    print(f'{total_min}:{total_sec:0>2d}')
else:
    print(f'{total_min}:{total_sec}')
