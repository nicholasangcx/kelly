from random import random

import matplotlib.pyplot as plt


kelly_capital = intuitive_capital = 100
horses = ('A', 'B', 'C')
odds = (2, 3, 6)
kelly_bet = probabilities = (0.5, 0.25, 0.25)
intuitive_bet = (0.5, 0.17, 0.33)
kelly_plot = []
intuitive_plot = []

for i in range(0, 100):
    # Determine winner of horse race randomly
    rand_num = random()
    winner = -1
    cumulative = 0
    for index, probability in enumerate(probabilities):
        cumulative += probability
        if rand_num < cumulative:
            winner = index
            break

    # Calculate capital after each race
    kelly_capital *= kelly_bet[winner] * odds[winner]
    intuitive_capital *= intuitive_bet[winner] * odds[winner]

    # Add point to the array for plotting of graph
    kelly_plot.append(kelly_capital)
    intuitive_plot.append(intuitive_capital)

x = [i for i in range(1, 101)]
plt.plot(x, kelly_plot, label='Kelly Betting')
plt.plot(x, intuitive_plot, label='Intuitive Betting')
plt.xlabel('Races')
plt.ylabel('Capital')
plt.title('Horse Racing Simulation')

plt.legend()
plt.show()




