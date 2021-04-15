age = int(input())
washing_machine = float(input())
toy_price = int(input())

money_sum = 0
amount_per_year = 10
toy_qty = 0

for _ in range(1, age + 1):
    if _ % 2 == 0:
        money_sum += amount_per_year
        amount_per_year += 10
        money_sum -= 1
    else:
        toy_qty += 1

toy_price_sum = toy_qty * toy_price
final_sum = toy_price_sum + money_sum

if final_sum >= washing_machine:
    money_left = final_sum - washing_machine
    print(f'Yes! {money_left:.2f}')
else:
    diff = abs(final_sum - washing_machine)
    print(f'No! {diff:.2f}')
