import math

vineyard_sqm = int(input())
grape_per_sqm = float(input())
liters_needed = int(input())
workers = int(input())

vineyard_sqm_wine_part = (vineyard_sqm / 100) * 40
total_grape_kg = grape_per_sqm * vineyard_sqm_wine_part
total_liters_of_wine = total_grape_kg / 2.5

# difference = math.fabs(total_liters_of_wine - liters_needed)   # with math.fabs() from - to +
difference = abs(liters_needed - total_liters_of_wine)
liters_per_worker = difference / workers

if total_liters_of_wine < liters_needed:
    print(f'It will be a tough winter! More {math.floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(total_liters_of_wine)} liters.')
    print(f'{math.ceil(difference)} liters left -> {math.ceil(liters_per_worker)} liters per person.')
