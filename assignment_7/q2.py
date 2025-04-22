import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data: Height (in inches) and corresponding Weight (in lbs)
height = np.array([60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                   71, 72, 73, 74, 75, 76, 77, 78, 79, 80])
weight = np.array([132, 136, 141, 145, 150, 155, 160, 165, 170, 175, 180, 
                   185, 190, 195, 201, 206, 212, 218, 223, 229, 234])

# Linear Regression Model (Weight vs. Height)
X_linear = height.reshape(-1, 1)
model_linear = LinearRegression()
model_linear.fit(X_linear, weight)
y_pred_linear = model_linear.predict(X_linear)
residuals_linear = weight - y_pred_linear

# Cubic Regression Model (Weight vs. Height^3)
X_cubic = (height ** 3).reshape(-1, 1)
model_cubic = LinearRegression()
model_cubic.fit(X_cubic, weight)
y_pred_cubic = model_cubic.predict(X_cubic)
residuals_cubic = weight - y_pred_cubic

# Plot and Save Residual Plot for Linear Model
plt.figure(figsize=(7, 5))
plt.scatter(height, residuals_linear, color='blue')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs. Height (Linear Model)")
plt.xlabel("Height (inches)")
plt.ylabel("Residuals")
plt.tight_layout()
plt.savefig("residuals_linear.png")
plt.close()

# Plot and Save Residual Plot for Cubic Model
plt.figure(figsize=(7, 5))
plt.scatter(height, residuals_cubic, color='green')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs. Height (Cubic Model)")
plt.xlabel("Height (inches)")
plt.ylabel("Residuals")
plt.tight_layout()
plt.savefig("residuals_cubic.png")
plt.close()
