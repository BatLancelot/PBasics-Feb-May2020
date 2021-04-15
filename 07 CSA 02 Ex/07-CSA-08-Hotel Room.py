month = input()
nights = int(input())

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
    elif nights > 7:
        studio_price *= 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.90

total_studio = studio_price * nights
total_apartment = apartment_price * nights

print(f'Apartment: {total_apartment:.2f} lv.\n'
      f'Studio: {total_studio:.2f} lv.')
