starting_population = int(input())
years = int(input())

for i in range(1, years + 1):
    if i == 1:
        population = starting_population
    else:
        population = total_year
    if i % 5 != 0:
        more = population // 10 * 2
        population += more
        less = population // 20 * 2
        population -= less
    elif i % 5 == 0:
        more = population // 10 * 2
        population += more
        migration = population // 50 * 5
        population -= migration
        less = population // 20 * 2
        population -= less

    total_year = population

    if i > years:
        break

print(f'Beehive population: {population}')
