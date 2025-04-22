import matplotlib.pyplot as plt

# Component reliabilities
R_power_1 = 0.993
R_power_2 = 0.998

# Communication: 2 radios in parallel
R_comm = 1 - (1 - 0.995)**2

# Landing gear
# Alternative 1: two legs in series (R_pair), third leg in parallel
R_leg_pair = 0.99 * 0.999
R_landing_1 = 1 - (1 - R_leg_pair) * (1 - 0.998)

# Alternative 2: three legs all in parallel
R_landing_2 = 1 - (1 - 0.99) * (1 - 0.999) * (1 - 0.998)

# Sample arm (same for both)
R_sample = 0.98

# Rockets (descent + ascent)
# Alternative 1: two rockets in series per stage, two stages in parallel
R_rocket_pair = 0.99**2
R_rockets_1 = 1 - (1 - R_rocket_pair)**2

# Alternative 2: four rockets all in parallel
R_rockets_2 = 1 - (1 - 0.99)**4

# Total mission reliability
R_total_1 = R_power_1 * R_comm * R_landing_1 * R_sample * R_rockets_1
R_total_2 = R_power_2 * R_comm * R_landing_2 * R_sample * R_rockets_2

# Print results
print(f"Total Reliability of Alternative 1: {R_total_1:.6f}")
print(f"Total Reliability of Alternative 2: {R_total_2:.6f}")

# Plot comparison
labels = ['Alternative 1', 'Alternative 2']
reliabilities = [R_total_1, R_total_2]

plt.figure(figsize=(6, 4))
plt.bar(labels, reliabilities)
plt.ylabel('Mission Reliability')
plt.ylim(0.97, 1.0)
plt.title('Comparison of Mars Lander Mission Reliabilities')
plt.grid(axis='y', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
