sqm = float(input())

budget = (sqm * 7.61)
discount = budget * 0.18
fin_price = budget - discount

print(f'The final price is: {fin_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')
