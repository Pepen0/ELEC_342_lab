import numpy as np

# Define parameters
K0 = 9  # Period
Omega_0 = 2 * np.pi / K0  # Fundamental angular frequency

# Define x[k] over one period (0 to 8)
x_k = [1, 1, 1, 0.5, 0.5, 0.5, 0, 0, 0]

# Compute DTFS coefficients for 0 <= n <= 9
n_values = np.arange(0, 10)
D_n = []

for n in n_values:
    # DTFS coefficient computation
    Dn = (1 / K0) * sum(x_k[k] * np.exp(-1j * n * Omega_0 * k) for k in range(K0))
    D_n.append(Dn)

# Compute magnitude and phase of D_n
magnitudes = np.abs(D_n)
phases = np.angle(D_n)

# Results in a structured form
results = {
    "n": n_values,
    "|D_n| (magnitude)": magnitudes,
    "∠D_n (phase in radians)": phases
}

import pandas as pd
df_results = pd.DataFrame(results)
print(df_results)