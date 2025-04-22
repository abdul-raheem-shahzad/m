import matplotlib.pyplot as plt

# Define LCG function
def lcg(a, b, c, n, seed=0):
    x = seed
    seq = []
    for _ in range(n):
        x = (a * x + b) % c
        seq.append(x)
    return seq

# Function to plot LCG sequences
def plot_lcg_sequence(a, b, c, n, seed=0, color='blue', label=''):
    seq = lcg(a, b, c, n, seed)
    plt.plot(seq, marker='o', linestyle='-', markersize=5, label=label, color=color)
    plt.title(f"LCG Sequence (a={a}, b={b}, c={c}, n={n})")
    plt.xlabel('Index (k)')
    plt.ylabel('Generated Value (X_k)')
    plt.grid(True)

# Plot for Case A (c = 8, n = 10)
plt.figure(figsize=(12, 6))
plot_lcg_sequence(5, 1, 8, 10, 0, 'blue', 'Case A (c = 8)')

# Plot for Case B (c = 10, n = 15)
plot_lcg_sequence(1, 7, 10, 15, 0, 'orange', 'Case B (c = 10)')

# Plot for Case C (c = 16, n = 20)
plot_lcg_sequence(5, 3, 16, 20, 0, 'green', 'Case C (c = 16)')

# Add legend and show plot
plt.legend()
plt.tight_layout()
plt.show()
