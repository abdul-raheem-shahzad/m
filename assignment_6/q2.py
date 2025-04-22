import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Data setup ---
days = np.array([0, 1, 2, 3, 4, 5, 6])
occurrences = np.array([200, 150, 200, 200, 150, 50, 50])
N = occurrences.sum()

# --- 2. Compute probabilities ---
p = occurrences / N
F = np.cumsum(p)

# --- 3. Compute summary statistics ---
E_X = np.sum(days * p)
E_X2 = np.sum(days**2 * p)
Var_X = E_X2 - E_X**2
Std_X = np.sqrt(Var_X)

print(f"Mean E[X]        = {E_X:.2f} days")
print(f"Variance Var[X]  = {Var_X:.2f}")
print(f"Std. deviation σ = {Std_X:.2f} days\n")

# --- 4. Display as a table ---
df = pd.DataFrame({
    'Days (k)':      days,
    'Frequency':     occurrences,
    'P(X=k)':        p.round(2),
    'F_X(k)':        F.round(2)
})
print(df.to_string(index=False))

# --- 5. Plot the PMF ---
plt.figure(figsize=(6,4))
plt.bar(days, p, edgecolor='black')
plt.xlabel('Days willing to wait before cancelling (k)')
plt.ylabel('Probability P(X = k)')
plt.title('Probability Mass Function')
plt.xticks(days)
plt.ylim(0, max(p)*1.1)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('pmf_waiting_time.png', dpi=150)
plt.show()

# --- 6. Plot the CDF ---
plt.figure(figsize=(6,4))
# extend the last step to 7 so the plateau at 1.00 is visible
x_step = np.append(days, days[-1] + 1)
y_step = np.append(F, F[-1])
plt.step(x_step, y_step, where='post')
plt.xlabel('Days willing to wait before cancelling (k)')
plt.ylabel('Cumulative Probability F_X(k)')
plt.title('Cumulative Distribution Function')
plt.xticks(days)
plt.ylim(0,1.05)
plt.grid(linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('cdf_waiting_time.png', dpi=150)
plt.show()
