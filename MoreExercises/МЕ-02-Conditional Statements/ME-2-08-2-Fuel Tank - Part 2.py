fuel = input()
liters = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93
liters_disc = 0


if fuel == 'Gasoline':
    if club_card == 'Yes':
        club_card_disc = gasoline - 0.18
        if 20 <= liters <= 25:
            liters_disc = club_card_disc - club_card_disc * 0.08
        elif liters > 25:
            liters_disc = club_card_disc - club_card_disc * 0.10
        else:
            liters_disc = club_card_disc
    else:
        if 20 <= liters <= 25:
            liters_disc = gasoline - gasoline * 0.08
        elif liters > 25:
            liters_disc = gasoline - gasoline * 0.10
        else:
            liters_disc = gasoline

if fuel == 'Diesel':
    if club_card == 'Yes':
        club_card_disc = diesel - 0.12
        if 20 <= liters <= 25:
            liters_disc = club_card_disc - club_card_disc * 0.08
        elif liters > 25:
            liters_disc = club_card_disc - club_card_disc * 0.10
        else:
            liters_disc = club_card_disc
    else:
        if 20 <= liters <= 25:
            liters_disc = diesel - diesel * 0.08
        elif liters > 25:
            liters_disc = diesel - diesel * 0.10
        else:
            liters_disc = diesel

if fuel == 'Gas':
    if club_card == 'Yes':
        club_card_disc = gas - 0.08
        if 20 <= liters <= 25:
            liters_disc = club_card_disc - club_card_disc * 0.08
        elif liters > 25:
            liters_disc = club_card_disc - club_card_disc * 0.10
        else:
            liters_disc = club_card_disc
    else:
        if 20 <= liters <= 25:
            liters_disc = gas - gas * 0.08
        elif liters > 25:
            liters_disc = gas - gas * 0.10
        else:
            liters_disc = gas

final_cost = liters * liters_disc

print(f'{final_cost:.2f} lv.')

# TODO it with FOR loop
