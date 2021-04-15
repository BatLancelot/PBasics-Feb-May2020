flower_type = input() # "Sunflower", "Daisy", "Lavender", "Mint"
flower_number = int(input())
season = input() #  "Spring", "Summer", "Autumn"

if flower_type == 'Sunflower':
    if season == 'Spring':  # Ако сезонът е "Spring", цветовете на "Daisy" и "Mint" дават 10% повече.
        honey = flower_number * 10
    elif season == 'Summer':  # Ако сезонът е "Summer", кошерът произвежда 10% повече мед.
        honey = (flower_number * 8) * 1.10
    elif season == 'Autumn':  #Ако сезонът е "Autumn", кошерът произвежда 5% по-малко мед.
        honey = (flower_number * 12) * 0.95

if flower_type == 'Daisy':
    if season == 'Spring':  # Ако сезонът е "Spring", цветовете на "Daisy" и "Mint" дават 10% повече.
        honey = (flower_number * 12) * 1.10
    elif season == 'Summer':  # Ако сезонът е "Summer", кошерът произвежда 10% повече мед.
        honey = (flower_number * 8) * 1.10
    elif season == 'Autumn':  #Ако сезонът е "Autumn", кошерът произвежда 5% по-малко мед.
        honey = (flower_number * 6) * 0.95

if flower_type == 'Lavender':
    if season == 'Spring':  # Ако сезонът е "Spring", цветовете на "Daisy" и "Mint" дават 10% повече.
        honey = flower_number * 12
    elif season == 'Summer':  # Ако сезонът е "Summer", кошерът произвежда 10% повече мед.
        honey = (flower_number * 8) * 1.10
    elif season == 'Autumn':  #Ако сезонът е "Autumn", кошерът произвежда 5% по-малко мед.
        honey = (flower_number * 6) * 0.95

if flower_type == 'Mint':
    if season == 'Spring':  # Ако сезонът е "Spring", цветовете на "Daisy" и "Mint" дават 10% повече.
        honey = (flower_number * 10) * 1.10
    elif season == 'Summer':  # Ако сезонът е "Summer", кошерът произвежда 10% повече мед.
        honey = (flower_number * 12) * 1.10
    elif season == 'Autumn':  # Ако сезонът е "Autumn", кошерът произвежда 5% по-малко мед.
        honey = (flower_number * 6) * 0.95

print(f'Total honey harvested: {honey:.2f}')
