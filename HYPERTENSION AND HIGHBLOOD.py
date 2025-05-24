import numpy as np
import matplotlib.pyplot as plt


# Blood Pressure and Hypertension
# Priors
P_hypertension = 0.30
P_no_hypertension = 1 - P_hypertension

# Likelihoods
P_high_bp_given_hypertension = 0.85
P_high_bp_given_no_hypertension = 0.10

# Evidence
P_high_bp = (
    P_high_bp_given_hypertension * P_hypertension +
    P_high_bp_given_no_hypertension * P_no_hypertension
)

# Posterior
P_hypertension_given_high_bp = (
    P_high_bp_given_hypertension * P_hypertension
) / P_high_bp

# Plot
plt.bar(['No Hypertension', 'Hypertension'],
        [1 - P_hypertension_given_high_bp, P_hypertension_given_high_bp],
        color=['green', 'darkblue'])
plt.title('Posterior Probability (High BP Reading)')
plt.ylabel('Probability')
plt.ylim(0, 1)
plt.grid(True, axis='y')
plt.show()
