budget = float(input())
category = input()
group_num = int(input())

ticket_price = 0
difference = 0

if category == 'VIP':
    ticket_price = 499.99  * group_num
    if 1 <= group_num <= 4:
        budget -= budget * 0.75
    elif 5 <= group_num <= 9:
        budget -= budget * 0.60
    elif 10 <= group_num <= 24:
        budget -= budget * 0.50
    elif 25 <= group_num <= 49:
        budget -= budget * 0.40
    elif 50 <= group_num:
        budget -= budget * 0.25
elif category == 'Normal':
    ticket_price = 249.99 * group_num
    if 1 <= group_num <= 4:
        budget -= budget * 0.75
    elif 5 <= group_num <= 9:
        budget -= budget * 0.60
    elif 10 <= group_num <= 24:
        budget -= budget * 0.50
    elif 25 <= group_num <= 49:
        budget -= budget * 0.40
    elif 50 <= group_num:
        budget -= budget * 0.25

difference = abs(budget - ticket_price)

if ticket_price < budget:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
