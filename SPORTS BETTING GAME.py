
import numpy as np
import matplotlib.pyplot as plt


# Sports Betting Game
# Prior
P_win = 0.6
P_lose = 1 - P_win

# Likelihoods
P_injury_given_win = 0.3
P_injury_given_lose = 0.6

# Evidence
P_injury = (
    P_injury_given_win * P_win +
    P_injury_given_lose * P_lose
)

# Posterior
P_win_given_injury = (
    P_injury_given_win * P_win
) / P_injury

# Plot
plt.bar(['Lose', 'Win'],
        [1 - P_win_given_injury, P_win_given_injury],
        color=['orange', 'green'])
plt.title('Posterior Probability (Player Injury)')
plt.ylabel('Probability')
plt.ylim(0, 1)
plt.grid(True, axis='y')
plt.show()
