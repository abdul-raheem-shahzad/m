import numpy as np
import matplotlib.pyplot as plt

# Parameters (from the problem statement)
I = 0.3513    # Daily intake of mercury (mg/day)
r = 0.9901    # Reduction factor per day
num_days = 200  # Number of days to simulate

M = np.zeros(num_days + 1)  # M[n] = mercury on day n
# M[0] = 0

for n in range(num_days):
    M[n+1] = r * M[n] + I

print(f"Mercury on day {num_days}: {M[-1]:.4f} mg")

M_infinity = I / (1 - r)
print(f"Long-term maximum: {M_infinity:.4f} mg")

# Plot
plt.figure(figsize=(8,5))
plt.plot(M, label='Mercury (M[n])')
plt.axhline(M_infinity, color='r', linestyle='--', label='Limit')
plt.xlabel('Day n')
plt.ylabel('Mercury (mg)')
plt.title('Mercury Accumulation')
plt.legend()
plt.show()
