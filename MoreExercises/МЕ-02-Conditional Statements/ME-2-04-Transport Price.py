distance = int(input())
day_or_night = input()

taxi_start_tax = 0.70
taxi_rate_day = 0.79
taxi_rate_night = 0.90
taxi_rate = 0.00
bus_rate = 0.09  # minimum 20km dist
train_rate = 0.06  # minimum 100km dist

price = 0.00

if day_or_night == 'day':
    taxi_rate = taxi_rate_day
else:
    taxi_rate = taxi_rate_night

if distance < 20:
    price = taxi_start_tax + taxi_rate * distance
elif distance < 100:
    price = bus_rate * distance
else:
    price = train_rate * distance

print(f'{price:.2f}')
