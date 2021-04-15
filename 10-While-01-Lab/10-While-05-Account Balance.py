transaction_qty = int(input())
transaction_counter = 0

balance = 0
while transaction_counter < transaction_qty:
    amount = float(input())
    if amount <= 0:
        print(f'Invalid operation!')
        break
    balance += amount
    print(f'Increase: {amount:.2f}')
    transaction_counter += 1

print(f'Total: {balance:.2f}')
