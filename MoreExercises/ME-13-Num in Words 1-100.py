ones_list = ["zero", "one", "two", "three", "four", "five", "six",
                            "seven", "eight", "nine"]
tens_list = [0, 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']
zero_list = [0, "ten", "twenty", 'thirty', 'forty', 'fifty',
                'sixty', 'seventy', 'eighty', 'ninety']

number = int(input())

for_tens = number % 10
for_ones = number // 10

if number == 100:
    print('One Hundred')

elif for_tens == 0 and number >= 10:
    print(zero_list[for_ones].capitalize())

elif 21 <= number <= 99:
    print(f"{zero_list[for_ones].capitalize()} {ones_list[for_tens].capitalize()}")

elif 11 <= number <= 19:
    print(tens_list[for_tens].capitalize())

elif number <= 9:
    print(ones_list[number].capitalize())
