import pandas as pd
import matplotlib.pyplot as plt

# Load temperature data from CSV
data = pd.read_csv('temp.csv', sep=';', header=None, names=['Timestamp', 'Temperature'])

# Convert the temperature column to float (if necessary)
data['Temperature'] = data['Temperature'].astype(float)

# Create a histogram of the temperature values
plt.figure(figsize=(10, 6))
plt.hist(data['Temperature'], bins=30, color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Temperature Values', fontsize=16)
plt.xlabel('Temperature (°C)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.grid(True)
plt.show()
