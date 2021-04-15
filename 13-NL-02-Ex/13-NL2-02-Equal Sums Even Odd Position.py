start_num = int(input())
end_num = int(input())

for n in range(start_num, end_num + 1):
    number = n

    if n % 2 == 1:
        is_odd = True
    else:
        is_odd = False

    sum_odd = 0
    sum_even = 0

    while n != 0:

        if is_odd:
            sum_odd += n % 10

        else:
            sum_even += n % 10

        is_odd = not is_odd

        n //= 10

    if sum_odd == sum_even:
        print(str(number), end=' ')
