num1 = int(input())
num2 = int(input())

for d1 in range(1, num1):
    for d2 in range(1, num1):
        for d3 in range(97, num2 + 97):
            for d4 in range(97, num2 + 97):
                for d5 in range(1, num1 + 1):
                    if d5 > d1 and d5 > d2:
                        print(f'{d1}{d2}{chr(d3)}{chr(d4)}{d5}', end=' ')










#  Символ 1: цифра от 1 до n;
#  Символ 2: цифра от 1 до n;
#  Символ 3: малка буква измежду първите l букви на латинската азбука;
#  Символ 4: малка буква измежду първите l букви на латинската азбука;
#  Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
