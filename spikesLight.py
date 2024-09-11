import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('light.csv', sep=';', names=['Time', 'Light'])

# Convert the 'Time' column to a datetime object
df['Time'] = pd.to_datetime(df['Time'], format='%d.%m.%Y %H:%M')

# Calculate the absolute difference between consecutive light values
df['Light_diff'] = df['Light'].diff().abs()

# Flag the rows where the difference is greater than 800
anomalies = df[df['Light_diff'] > 800]

# Downsample the dataset for better readability (plot every nth entry, e.g., every 500th point)
df_downsampled = df.iloc[::100, :]

# Plot the downsampled light levels
plt.figure(figsize=(10, 6))
plt.plot(df_downsampled['Time'], df_downsampled['Light'], label='Light Level (Downsampled)', color='blue')

# Highlight anomalies
plt.scatter(anomalies['Time'], anomalies['Light'], color='red', label='Anomalies (Change > 800)', zorder=5)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Light Level')
plt.title('Light Levels with Anomalies (Change > 800)')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
