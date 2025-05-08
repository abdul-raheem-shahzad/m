import numpy as np
import pandas as pd

# Given data points (V, P)
V = np.array([2.27, 2.76, 3.27, 3.31, 3.70, 3.85, 4.31, 4.39, 4.42, 
              4.81, 4.90, 5.05, 5.21, 5.62, 5.88])
P = np.array([2500, 365, 23700, 5491, 14000, 78200, 70700, 138000, 304500,
              341948, 49375, 260200, 867023, 1340000, 1092759])

# Using the power-law model P = a * V^b
a = 0.797
b = 8.006

# Compute model predictions
P_pred = a * V**b

# Compute deviations
deviations = P - P_pred

# Compute sum of squared deviations
sum_squared_deviations = np.sum(deviations**2)

# Compute D (mean absolute deviation)
D = np.mean(np.abs(deviations))

# Compute d_max (maximum absolute deviation)
d_max = np.max(np.abs(deviations))

# Output results
print(f"Mean Absolute Deviation (D): {D}")
print(f"Maximum Absolute Deviation (d_max): {d_max}")
print(f"Sum of Squared Deviations: {sum_squared_deviations}")
