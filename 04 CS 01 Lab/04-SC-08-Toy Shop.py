excursion_price = float(input())
puzzle_num = int(input())
dolls_num = int(input())
bears_num = int(input())
minions_num = int(input())
trucks_num = int(input())

puzzle = puzzle_num * 2.60
doll = dolls_num * 3
bear = bears_num * 4.10
minion = minions_num * 8.20
truck = trucks_num * 2

total_order = puzzle + doll + bear + minion + truck
total_toys = puzzle_num + dolls_num + bears_num + minions_num + trucks_num

if total_toys >= 50:
    total_order = total_order * 0.75

total_order = total_order * 0.9

if total_order >= excursion_price:
    money_left = total_order - excursion_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = total_order - excursion_price
    print(f'Not enough money! {abs(money_left):.2f} lv needed.')
