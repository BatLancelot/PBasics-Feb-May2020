import math

num_bees = int(input())
num_flowers = int(input())

total_honey = num_bees * num_flowers * 0.21
honeycombs = total_honey / 100
honey_left = total_honey % 100

print(f"{math.floor(honeycombs)} honeycombs filled.")
print(f"{honey_left:.2f} grams of honey left.")

