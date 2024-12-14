import numpy as np

# Define parameters
K0 = 9  # Period
Omega_0 = 2 * np.pi / K0  # Fundamental angular frequency

# Define x[k] over one period (0 to 8)
x_k = [1, 1, 1, 0.5, 0.5, 0.5, 0, 0, 0]

# Compute DTFS coefficients for 0 <= n <= 9
n_values = np.arange(0, 10)
D_n = []
