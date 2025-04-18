import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data from the table
locations = [
    "Brno, Czechoslovakia", "Prague, Czechoslovakia", "Corte, Corsica", "Bastia, France", 
    "Munich, Germany", "Psychro, Crete", "Itea, Greece", "Iraklion, Greece", "Athens, Greece", 
    "Safed, Israel", "Dimona, Israel", "Netanya, Israel", "Jerusalem, Israel", 
    "New Haven, U.S.A.", "Brooklyn, U.S.A."
]
population = [
    341948, 1092759, 5491, 49375, 1340000, 365, 2500, 78200, 867023, 14000, 
    23700, 70700, 304500, 138000, 2602000
]
mean_velocity = [
    4.81, 5.88, 3.31, 4.90, 5.62, 2.76, 2.27, 3.85, 5.21, 3.70, 3.27, 4.31, 4.42, 4.39, 5.05
]

# Convert the data to a DataFrame
df = pd.DataFrame({
    'Location': locations,
    'Population': population,
    'Mean Velocity': mean_velocity
})

# Apply the logarithm to Population and Mean Velocity
df['logP'] = np.log(df['Population'])
df['logV'] = np.log(df['Mean Velocity'])

# Perform linear regression to find a and logC
X = df[['logP']].values  # logP as the independent variable
y = df['logV'].values    # logV as the dependent variable

# Linear regression model
model = LinearRegression()
model.fit(X, y)

# Extract the parameters
a = model.coef_[0]  # Slope
log_C = model.intercept_  # Intercept

# Calculate C
C = np.exp(log_C)

# Prepare the results
equation = f"V = {C:.4f} * P^{a:.4f}"

# Generate the table for logP vs logV
logP_logV_table = df[['logP', 'logV']].round(4)

# Save the log-log scatter plot with fitted line
plt.figure(figsize=(8, 6))
plt.scatter(df['logP'], df['logV'], color='blue', label='Data Points')
plt.plot(df['logP'], model.predict(X), color='red', label=f'Fitted Line: V = {C:.4f} * P^{a:.4f}')
plt.xlabel('log(Population)')
plt.ylabel('log(Mean Velocity)')
plt.title('Log-Log Scatter Plot of Population vs. Mean Velocity')
plt.legend()
plt.grid(True)
loglog_image_path = 'loglog_scatterplot.png'
plt.savefig(loglog_image_path)

# Calculate the predicted values of V using the fitted model (V = 1.3970 * P^0.0960)
predicted_velocity = C * np.array(population) ** a

# Save the original data with fitted model plot
plt.figure(figsize=(8, 6))
plt.scatter(population, mean_velocity, color='blue', label='Data Points')
plt.plot(population, predicted_velocity, color='red', label=f'Fitted Model: V = {C:.4f} * P^{a:.4f}')
plt.xlabel('Population')
plt.ylabel('Mean Velocity (ft/sec)')
plt.title('Original Data with Fitted Model')
plt.legend()
plt.grid(True)
original_fitted_image_path = 'original_fitted_model.png'
plt.savefig(original_fitted_image_path)

# Show results
print(f"Fitted Model Equation: V = {C:.4f} * P^{a:.4f}")
print(logP_logV_table.head())  # Show the first few rows of the table

# Output the paths for the images
loglog_image_path, original_fitted_image_path
