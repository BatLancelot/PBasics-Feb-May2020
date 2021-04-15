amount = float(input())
first = input()
second = input()
from_curr = first.lower()
to_curr = second.lower()

rate_bgn = 1
rate_usd = 1.79549
rate_eur = 1.95583
rate_gbp = 2.53405

if from_curr == 'bgn':
    if to_curr == 'usd':
        conversion = amount * (rate_bgn / rate_usd)
        print(f'{conversion:.2f} USD')
    elif to_curr == 'eur':
        conversion = amount * (rate_bgn / rate_eur)
        print(f'{conversion:.2f} EUR')
    elif to_curr == 'gbp':
        conversion = amount * (rate_bgn / rate_gbp)
        print(f'{conversion:.2f} GBP')

if from_curr == 'usd':
    if to_curr == 'bgn':
        conversion = amount * (rate_usd / rate_bgn)
        print(f'{conversion:.2f} BGN')
    elif to_curr == 'eur':
        conversion = amount * (rate_usd / rate_eur)
        print(f'{conversion:.2f} EUR')
    elif to_curr == 'gbp':
        conversion = amount * (rate_usd / rate_gbp)
        print(f'{conversion:.2f} GBP')

if from_curr == 'eur':
    if to_curr == 'bgn':
        conversion = amount * (rate_eur / rate_bgn)
        print(f'{conversion:.2f} BGN')
    elif to_curr == 'usd':
        conversion = amount * (rate_eur / rate_usd)
        print(f'{conversion:.2f} USD')
    elif to_curr == 'gbp':
        conversion = amount * (rate_eur / rate_gbp)
        print(f'{conversion:.2f} GBP')

if from_curr == 'gbp':
    if to_curr == 'bgn':
        conversion = amount * (rate_gbp / rate_bgn)
        print(f'{conversion:.2f} BGN')
    elif to_curr == 'usd':
        conversion = amount * (rate_gbp / rate_usd)
        print(f'{conversion:.2f} USD')
    elif to_curr == 'eur':
        conversion = amount * (rate_gbp / rate_eur)
        print(f'{conversion:.2f} EUR')

#  else:
#  print('Wrong Currency!')
