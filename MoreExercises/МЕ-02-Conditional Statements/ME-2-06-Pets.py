import math

num_days = int(input())
food_kg = int(input())
dogs_food_kg = float(input())
cats_food_kg = float(input())
turtle_food_grams = float(input()) / 1000

total_food_needed = (dogs_food_kg + cats_food_kg + turtle_food_grams) * num_days
food_left = abs(food_kg - total_food_needed)

if total_food_needed <= food_kg:
    print(f'{math.floor(food_left)} kilos of food left.')
else:
    print(f'{math.ceil(food_left)} more kilos of food are needed.')
