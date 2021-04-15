skumria_price_kg = float(input())
caca_price_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price_kg = skumria_price_kg * 1.6
safrid_price_kg = caca_price_kg * 1.8
midi_price = 7.5

total_money = palamud_price_kg * palamud_kg + safrid_price_kg * safrid_kg + midi_price * midi_kg

print(f'{total_money:.2f}')
