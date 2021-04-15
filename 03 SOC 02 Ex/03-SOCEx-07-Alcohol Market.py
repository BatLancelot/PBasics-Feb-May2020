whiskey_price = float(input())
beer_vol = float(input())
wine_vol = float(input())
rakia_vol = float(input())
whiskey_vol = float(input())

whiskey_sum = whiskey_price * whiskey_vol

rakia_price = whiskey_price * 0.5
rakia_sum = rakia_price * rakia_vol

wine_price = rakia_price * 0.6
wine_sum = wine_price * wine_vol

beer_price = rakia_price * 0.2
beer_sum = beer_price * beer_vol

total_sum = rakia_sum + wine_sum + beer_sum + whiskey_sum

print(f'{total_sum:.2f}')
