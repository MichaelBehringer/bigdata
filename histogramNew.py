import pandas as pd
import matplotlib.pyplot as plt

# Load the light data
light_df = pd.read_csv('light.csv', sep=';', header=None, names=['Timestamp', 'Light Intensity'])
light_df['Timestamp'] = pd.to_datetime(light_df['Timestamp'], format='%d.%m.%Y %H:%M')

# Load the temperature data
temp_df = pd.read_csv('temp.csv', sep=';', header=None, names=['Timestamp', 'Temperature'])
temp_df['Timestamp'] = pd.to_datetime(temp_df['Timestamp'].str.strip(), format='%Y-%m-%d %H:%M:%S')

# Plot and save the light intensity histogram
plt.figure(figsize=(6, 6))
plt.hist(light_df['Light Intensity'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Light Intensity')
plt.xlabel('Light Intensity (0-1023)')
plt.ylabel('Frequency')
plt.grid(True)

# Save the light intensity histogram
plt.savefig('light_intensity_histogram.png')
plt.show()

# Plot and save the temperature histogram
plt.figure(figsize=(6, 6))
plt.hist(temp_df['Temperature'], bins=20, color='lightcoral', edgecolor='black')
plt.title('Histogram of Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)

# Save the temperature histogram
plt.savefig('temperature_histogram.png')
plt.show()
