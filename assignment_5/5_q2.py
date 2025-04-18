import numpy as np
import matplotlib.pyplot as plt

# Data for Problem 7 (Ponderosa pine diameter and volume)
X_data = np.array([17, 19, 20, 22, 23, 25, 31, 32, 33, 36, 37, 38, 39, 41])
Y_data = np.array([19, 25, 32, 51, 57, 71, 141, 123, 187, 192, 205, 252, 248, 294])

# Scatterplot of the data
plt.figure(figsize=(8, 6))
plt.scatter(X_data, Y_data, color='blue', label='Data Points')
plt.xlabel('Diameter of Ponderosa Pine (X)')
plt.ylabel('Volume (Y)')
plt.title('Scatterplot of Diameter vs. Volume for Ponderosa Pine')
plt.legend()
plt.grid(True)
plt.show()

# Fit a 2nd-degree polynomial (quadratic) and 13th-degree polynomial
low_degree_poly = np.polyfit(X_data, Y_data, 2)
high_degree_poly = np.polyfit(X_data, Y_data, 13)

# Create polynomial functions
low_degree_function = np.poly1d(low_degree_poly)
high_degree_function = np.poly1d(high_degree_poly)

# Generate X values for plotting the fitted polynomials
X_fit = np.linspace(min(X_data), max(X_data), 1000)
Y_low_fit = low_degree_function(X_fit)
Y_high_fit = high_degree_function(X_fit)

# Plot the data and the fitted polynomials
plt.figure(figsize=(8, 6))
plt.scatter(X_data, Y_data, color='blue', label='Data Points')
plt.plot(X_fit, Y_low_fit, color='red', label='2nd-degree Polynomial Fit')
plt.plot(X_fit, Y_high_fit, color='green', label='13th-degree Polynomial Fit')
plt.xlabel('Diameter of Ponderosa Pine (X)')
plt.ylabel('Volume (Y)')
plt.title('Data and Polynomial Fits')
plt.legend()
plt.grid(True)
plt.show()
