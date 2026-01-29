import numpy as np
import matplotlib.pyplot as plt

# Parameters for the SDE
S0 = 100  # Initial asset price
r = 0.05  # Risk-free rate
T = 1.0   # Time horizon (1 year)
N = 252   # Number of time steps (daily steps for 1 year)
dt = T / N # Time step

# Number of simulation paths
num_paths = 5

# --- 1. Constant Volatility ---
sigma_const = 0.2  # Constant volatility

def simulate_gbm_const_vol(S0, r, sigma, dt, N, num_paths):
    S = np.zeros((N + 1, num_paths))
    S[0] = S0
    for t in range(1, N + 1):
        dW = np.random.normal(0, np.sqrt(dt), num_paths)
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * dW)
    return S

# Simulate paths
paths_const_vol = simulate_gbm_const_vol(S0, r, sigma_const, dt, N, num_paths)

# --- 2. Time-Dependent Volatility ---
# Example: a sinusoidal volatility that varies between 10% and 30%
def sigma_time_dependent(t, T):
    # Volatility starts at 0.2, dips, and then goes up
    return 0.2 + 0.1 * np.sin(2 * np.pi * t / T) 
    # Ensure volatility remains positive
    # return max(0.05, 0.2 + 0.1 * np.sin(2 * np.pi * t / T)) 


def simulate_gbm_time_dependent_vol(S0, r, sigma_func, dt, N, num_paths, T_total):
    S = np.zeros((N + 1, num_paths))
    S[0] = S0
    time_points = np.linspace(0, T_total, N + 1)
    
    for t_idx in range(1, N + 1):
        current_t = time_points[t_idx-1]
        current_sigma = sigma_func(current_t, T_total)
        dW = np.random.normal(0, np.sqrt(dt), num_paths)
        S[t_idx] = S[t_idx-1] * np.exp((r - 0.5 * current_sigma**2) * dt + current_sigma * dW)
    return S

# Simulate paths
paths_time_dep_vol = simulate_gbm_time_dependent_vol(S0, r, sigma_time_dependent, dt, N, num_paths, T)

# --- Plotting ---
time = np.linspace(0, T, N + 1)

plt.figure(figsize=(14, 7))

# Plot for Constant Volatility
plt.subplot(1, 2, 1)
plt.plot(time, paths_const_vol)
plt.title(f'Asset Price Paths with Constant Volatility ($\sigma={sigma_const:.2f}$)', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Asset Price ($X_t$)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim([S0 * 0.5, S0 * 2]) # Consistent y-axis for comparison

# Plot for Time-Dependent Volatility
plt.subplot(1, 2, 2)
plt.plot(time, paths_time_dep_vol)
plt.title('Asset Price Paths with Time-Dependent Volatility ($\sigma_t = 0.2 + 0.1 \sin(2\pi t)$)', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Asset Price ($X_t$)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim([S0 * 0.5, S0 * 2]) # Consistent y-axis for comparison

plt.tight_layout()
plt.savefig('asset_price_paths_volatility_comparison.png')
plt.show()

print(f"Graph saved as asset_price_paths_volatility_comparison.png")