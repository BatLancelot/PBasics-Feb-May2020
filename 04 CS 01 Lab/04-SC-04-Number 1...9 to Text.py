ones_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number = int(input())

if number <= 9:
    print(ones_list[number])
else:
    print('number too big')
