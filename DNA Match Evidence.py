# -*- coding: utf-8 -*-
"""
Created on Sat May 24 22:04:17 2025

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

# DNA Evidence 

# Prior probabilities
P_guilty = 1 / 1_000_000
P_innocent = 1 - P_guilty

# Likelihoods
P_match_given_guilty = 1.0
P_match_given_innocent = 2/ 1_000_000

# Evidence
P_match = (P_match_given_guilty * P_guilty) + (P_match_given_innocent * P_innocent)

# Posterior
P_guilty_given_match = (P_match_given_guilty * P_guilty) / P_match

# Plot
plt.bar(['Innocent', 'Guilty'], [1 - P_guilty_given_match, P_guilty_given_match], color=['gray', 'red'])
plt.title('Posterior Probability (DNA Match)')
plt.ylabel('Probability')
plt.ylim(0, 1)
plt.grid(True, axis='y')
plt.show()