number = int(input())

sum_Prime = 0
sum_nonPrime = 0

while number != 'stop':
    number = int(number)
    is_prime = True
    if number < 0:
        print('Number is negative.')
    # elif number == 0:
    #     sum_nonPrime += number
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            sum_Prime += number
        else:
            sum_nonPrime += number

    number = input()

print(f"Sum of all prime numbers is: {sum_Prime}")
print(f"Sum of all non prime numbers is: {sum_nonPrime}")
