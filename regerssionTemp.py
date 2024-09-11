import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load the CSV data into a pandas DataFrame
file_path = 'temp.csv'
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'], dayfirst=True)

# Convert the timestamp to a numerical format (e.g., number of days since the start)
df['Day'] = (df['Time'] - df['Time'].min()).dt.days

# Prepare data for regression
X = df[['Day']]
y = df['Temp']

# Fit linear regression model
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)

# Fit quadratic regression model
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
quadratic_model = LinearRegression()
quadratic_model.fit(X_poly, y)
y_pred_quadratic = quadratic_model.predict(X_poly)

# Create the plot
plt.figure(figsize=(14, 8))

# Plot real temperature data
plt.scatter(df['Day'], y, color='blue', label='Real Temperature')

# Plot linear regression line
plt.plot(df['Day'], y_pred_linear, color='red', label='Linear Regression', linewidth=2)

# Plot quadratic regression line
sorted_days = np.sort(df['Day'])
sorted_days_poly = poly.transform(sorted_days.reshape(-1, 1))
y_pred_quadratic_sorted = quadratic_model.predict(sorted_days_poly)
plt.plot(sorted_days, y_pred_quadratic_sorted, color='green', label='Quadratic Regression', linewidth=2)

# Add titles and labels
plt.title('Temperature with Linear and Quadratic Regression')
plt.xlabel('Days Since Start')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
