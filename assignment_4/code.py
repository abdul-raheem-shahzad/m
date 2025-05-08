import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data from the table provided
locations = ["Brno, Czechoslovakia", "Prague, Czechoslovakia", "Corte, Corsica", "Bastia, France", 
    "Munich, Germany", "Psyhcro, Crete", "Itea, Greece", "Iraklion, Greece", "Athens, Greece", 
    "Safed, Israel", "Dimona, Israel", "Netanya, Israel", "Jerusalem, Israel", "New Haven, U.S.A.", "Brooklyn, U.S.A."]

population = [341948, 1092759, 5491, 49375, 1340000, 365, 2500, 78300, 867023, 14000, 23700, 70700, 304500, 138000, 2602000]

mean_velocity = [4.81, 5.88, 3.31, 4.90, 5.62, 2.76, 2.27, 3.85, 5.21, 3.70, 3.27, 4.31, 4.42, 4.39, 5.05]

# Calculate log(P) and log(V) for the model
log_population = np.log(population)
log_velocity = np.log(mean_velocity)

# Create a dataframe
data = pd.DataFrame({
    "Location": locations,
    "Population": population,
    "Mean Velocity": mean_velocity,
    "log(P)": log_population,
    "log(V)": log_velocity
})

# Scatter plot of log(P) vs log(V)
plt.figure(figsize=(8, 6))
plt.scatter(data["log(P)"], data["log(V)"], color='blue')
plt.title('Log-Log Plot of Population vs Mean Velocity')
plt.xlabel('log(P) - Log of Population')
plt.ylabel('log(V) - Log of Mean Velocity')
plt.grid(True)
plt.savefig('log_log_plot.png')  # Save the plot as a PNG image
plt.show()
