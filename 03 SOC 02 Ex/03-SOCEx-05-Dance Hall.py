import math

hall_length = float(input())
hall_width = float(input())
wardrobe_side = float(input())

hall_size = hall_length * hall_width
bench_size = hall_size / 10
wardrobe_size = math.pow(wardrobe_side, 2)
free_area = hall_size - bench_size - wardrobe_size
dancer_area = 7040 / math.pow(100, 2)
num_dancers = free_area / dancer_area

print(math.floor(num_dancers))
