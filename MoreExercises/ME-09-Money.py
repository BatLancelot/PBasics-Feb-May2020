bitcoin = int(input())
yuans = float(input())
commision = float(input()) /100

bitcoin_to_bgn = 1168
yuan_to_usd = 0.15
usd_to_bgn = 1.76
bgn_to_eur = 1.95

bitcoin_total = bitcoin * bitcoin_to_bgn
yuans_total = (yuans * yuan_to_usd) * usd_to_bgn
total_eur = ((bitcoin_total + yuans_total) / bgn_to_eur)
commision_eur = total_eur * commision

grand_total = total_eur - commision_eur

print(f'{grand_total:.2f}')
