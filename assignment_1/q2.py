import numpy as np
import matplotlib.pyplot as plt

# Model coefficients
alpha = 1.20   # mice growth
beta  = 0.001  # mice predation factor
gamma = 0.70   # owls survival rate
delta = 0.002  # owls growth from predation

n_steps = 50
M = np.zeros(n_steps + 1)
O = np.zeros(n_steps + 1)

M[0] = 200  # initial mice
O[0] = 150  # initial owls

for n in range(n_steps):
    M[n+1] = alpha*M[n] - beta*M[n]*O[n]
    O[n+1] = gamma*O[n] + delta*M[n]*O[n]

# Print table
print("Step\tMice\t\tOwls")
for n in range(n_steps+1):
    print(f"{n}\t{M[n]:.2f}\t\t{O[n]:.2f}")

# Plot
t = np.arange(n_steps + 1)
plt.figure(figsize=(8,5))
plt.plot(t, M, label='Mice')
plt.plot(t, O, label='Owls')
plt.xlabel('Time step n')
plt.ylabel('Population')
plt.title('Discrete-Time Predator–Prey Model')
plt.legend()
plt.show()
