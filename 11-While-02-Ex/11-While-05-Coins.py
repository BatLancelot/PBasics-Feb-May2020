amount = float(input())

coins = round(amount * 100)
coin_counter = 0

while coins > 0:
    if coins >= 200:
        coins -= 200
        coin_counter += 1
    elif coins >= 100:
        coins -= 100
        coin_counter += 1
    elif coins >= 50:
        coins -= 50
        coin_counter += 1
    elif coins >= 20:
        coins -= 20
        coin_counter += 1
    elif coins >= 10:
        coins -= 10
        coin_counter += 1
    elif coins >= 5:
        coins -= 5
        coin_counter += 1
    elif coins >= 2:
        coins -= 2
        coin_counter += 1
    elif coins >= 1:
        coins -= 1
        coin_counter += 1

print(coin_counter)
