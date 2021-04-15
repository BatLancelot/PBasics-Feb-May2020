num_of_bees = int(input())
bear_health = int(input())
bear_attack = int(input())

bee_health = 1
bee_attack = 5

for y in range(num_of_bees):
    bear_current_attack = num_of_bees - bear_attack
    num_of_bees = bear_current_attack

    if num_of_bees <= 100:
        if num_of_bees < 0:
            num_of_bees = 0
        print(f"The bear stole the honey! Bees left {num_of_bees}.")
        break

    bee_current_attack = bear_health - (num_of_bees * 5)
    bear_health = bee_current_attack

    if bear_health <= 0:
        print(f"Beehive won! Bees left {num_of_bees}.")
        break



