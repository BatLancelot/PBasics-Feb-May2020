num_tables = int(input())
length_tables = float(input())
width_tables = float(input())

table_cover_rec = num_tables * (length_tables + 0.60) * (width_tables + 0.60)
table_cover_sq = num_tables * (length_tables / 2) * (length_tables / 2)

cover_price_usd = (table_cover_rec * 7) + (table_cover_sq * 9)
cover_price_bgn = cover_price_usd * 1.85

print(f'{cover_price_usd:.2f} USD')
print(f'{cover_price_bgn:.2f} BGN')
