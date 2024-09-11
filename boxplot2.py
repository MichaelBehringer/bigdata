import pandas as pd
import matplotlib.pyplot as plt

# Load the light data
light_df = pd.read_csv('light.csv', sep=';', header=None, names=['Timestamp', 'Light Intensity'])
# Clean the light data by stripping any whitespace in column names
light_df['Timestamp'] = pd.to_datetime(light_df['Timestamp'], format='%d.%m.%Y %H:%M')

# Load the temperature data
temp_df = pd.read_csv('temp.csv', sep=';', header=None, names=['Timestamp', 'Temperature'])
# Clean the temperature data by stripping any whitespace in column names
temp_df['Timestamp'] = pd.to_datetime(temp_df['Timestamp'].str.strip(), format='%Y-%m-%d %H:%M:%S')

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Box plot for Light Intensity
ax1.boxplot(light_df['Light Intensity'])
ax1.set_title('Box Plot of Light Intensity')
ax1.set_ylabel('Light Intensity (0-1023)')
ax1.grid(True)

# Box plot for Temperature
ax2.boxplot(temp_df['Temperature'])
ax2.set_title('Box Plot of Temperature')
ax2.set_ylabel('Temperature (°C)')
ax2.grid(True)

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
