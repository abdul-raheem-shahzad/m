import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Given data
V = np.array([2.27, 2.76, 3.27, 3.31, 3.70, 3.85, 4.31, 4.39, 4.42, 
              4.81, 4.90, 5.05, 5.21, 5.62, 5.88])
P = np.array([2500, 365, 23700, 5491, 14000, 78200, 70700, 138000, 304500,
              341948, 49375, 260200, 867023, 1340000, 1092759])

# Log-Log transformation for model P = aV^b
log_V = np.log(V)
log_P = np.log(P)

# Linear fit for log-transformed data
slope, intercept, _, _, _ = stats.linregress(log_V, log_P)
a_power = np.exp(intercept)
b_power = slope

# Plot original data
plt.figure(figsize=(6, 5))
plt.scatter(V, P, color='blue', label="Original Data")
plt.xlabel("Mean Walking Velocity (V)")
plt.ylabel("Population Size (P)")
plt.title("Original Data")
plt.legend()
plt.savefig("original_data.png", dpi=300)
plt.close()

# Log-Log Transformation
plt.figure(figsize=(6, 5))
plt.scatter(log_V, log_P, color='red', label="Log-Log Data")
plt.xlabel("log(V)")
plt.ylabel("log(P)")
plt.title("Log-Log Transformation")
plt.legend()
plt.savefig("log_log_transformation.png", dpi=300)
plt.close()

print(f"Power Law Model: P = {a_power:.3f} * V^{b_power:.3f}")
