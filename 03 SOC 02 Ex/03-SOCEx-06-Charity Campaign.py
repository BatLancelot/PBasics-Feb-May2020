days = int(input())
cooks = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_sum = cakes * 45
print(cakes_sum)
waffles_sum = waffles * 5.80
print(waffles_sum)
pancakes_sum = pancakes * 3.20
print(pancakes_sum)

day_sum =  cooks * (cakes_sum + waffles_sum + pancakes_sum)
print(day_sum)

campain = day_sum * days
print(campain)

for_charity = campain - (campain * 1/8)

print(f'{for_charity:.2f}')







