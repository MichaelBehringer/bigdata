import pandas as pd
import matplotlib.pyplot as plt

# Load the light data
light_df = pd.read_csv('light.csv', sep=';', header=None, names=['Timestamp', 'Light Intensity'])
# Clean the light data by converting the timestamp column to datetime (optional for the box plot)
light_df['Timestamp'] = pd.to_datetime(light_df['Timestamp'], format='%d.%m.%Y %H:%M')

# Create the box plot for light intensity
plt.figure(figsize=(6, 6))
plt.boxplot(light_df['Light Intensity'])

# Add title and labels
plt.title('Box Plot of Light Intensity')
plt.ylabel('Light Intensity (0-1023)')
plt.grid(True)

# Show the plot
plt.show()
