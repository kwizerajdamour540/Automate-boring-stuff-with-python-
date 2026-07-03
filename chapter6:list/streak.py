import random

number_of_streaks = 0

for experiment in range(10000):  # Run 10,000 experiments
    # Code that creates a list of 100 'heads' or 'tails' values
    coin_flips = []
    for i in range(100):
        z = random.randint(0, 1)  # 0 is head, 1 is tail
        if z == 0:
            coin_flips.append('H')
        else:
            coin_flips.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(95):  # Checks blocks of 6 up to index 100
        if coin_flips[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H'] or coin_flips[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            number_of_streaks += 1
            break #because is chance per loop 

print('Chance of streak: %s%%' % (number_of_streaks / 100))

