import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
S0 = 100
sigma = 0.2
T = 5.0      # Longer maturity to emphasize the drift impact
N = 500
dt = T / N
t = np.linspace(0, T, N+1)

# 1. Constant interest rate (Standard Black-Scholes)
r_const = 0.05

# 2. Time-dependent interest rate
# The rate fluctuates between 1% and 9% using a sinusoidal function
def r_func(t):
    return 0.05 + 0.04 * np.sin(2 * np.pi * t / T)

# Path simulation (using the same seed and Brownian motion for direct comparison)
np.random.seed(42)
dW = np.random.normal(0, np.sqrt(dt), N)
W = np.insert(np.cumsum(dW), 0, 0)

# Calculate paths under the risk-neutral measure Q
# Constant rate case
S_const = S0 * np.exp((r_const - 0.5 * sigma**2) * t + sigma * W)

# Variable rate case (numerical integration of the rate function)
r_values = r_func(t)
r_integral = np.cumsum(r_values) * dt 
S_variable = S0 * np.exp(r_integral - 0.5 * sigma**2 * t + sigma * W)

# Visualization
plt.figure(figsize=(10, 6))
plt.plot(t, S_const, label=f'Constant Rate ($r={r_const*100:.0f}\%$)')
plt.plot(t, S_variable, label='$r(t) = 0.05 + 0.04 \sin(2\pi t / T)$', linewidth=2)

plt.title('Impact of Interest Rate Dynamics on Asset Price ($X_t$)', fontsize=14)
plt.xlabel('Time (Years)', fontsize=12)
plt.ylabel('Asset Price', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

# Save the plot for the LaTeX report
plt.savefig('interest_rate_impact.png')
plt.show()

print(f"Graph saved as interest_rate_impact.png")
