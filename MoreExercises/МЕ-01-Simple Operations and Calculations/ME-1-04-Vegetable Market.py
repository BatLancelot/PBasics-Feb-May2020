price_veg = float(input())
price_fru = float(input())
vol_veg = float(input())
vol_fru = float(input())

vegetables = price_veg * vol_veg
fruits = price_fru * vol_fru

price_eur = (vegetables + fruits) / 1.94

print(f'{price_eur:.2f}')
