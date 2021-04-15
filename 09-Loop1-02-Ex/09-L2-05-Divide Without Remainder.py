n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, n + 1):
    number = float(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1_per = p1 / n * 100
p2_per = p2 / n * 100
p3_per = p3 / n * 100

print(f'{p1_per:.2f}%')
print(f'{p2_per:.2f}%')
print(f'{p3_per:.2f}%')
