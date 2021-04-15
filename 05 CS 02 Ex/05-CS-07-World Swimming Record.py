import math

record_sec = float(input())
distance_meters = float(input())
time_sec_per_meter = float(input())

slowing = math.floor(distance_meters / 15) * 12.5

time_in_sec = distance_meters * time_sec_per_meter + slowing

time_difference = time_in_sec - record_sec

if time_in_sec < record_sec:
    print(f'Yes, he succeeded! The new world record is {time_in_sec:.2f} seconds.')
else:
    print(f'No, he failed! He was {time_difference:.2f} seconds slower.')
