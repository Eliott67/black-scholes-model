import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
T = 1.0        # Time horizon
N = 1000       # Number of time steps
dt = T / N     # Time step size
num_paths = 50 # Number of paths to simulate
t = np.linspace(0, T, N + 1)

# Generate Brownian increments: dW ~ N(0, sqrt(dt))
np.random.seed(42) 
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, N))

# Compute the Brownian paths W_t (starting at 0)
W = np.zeros((num_paths, N + 1))
W[:, 1:] = np.cumsum(dW, axis=1)

# Plotting
plt.figure(figsize=(10, 6))
for i in range(num_paths):
    plt.plot(t, W[i, :], linewidth=0.8, alpha=0.7)


plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

plt.savefig('brownian_motion.png')
plt.show()
