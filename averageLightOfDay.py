import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
file_path = 'light.csv'
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'], dayfirst=True)

# Extract the hour from the timestamp
df['Hour'] = df['Time'].dt.hour

# Calculate the average light intensity for each hour
avg_light_per_hour = df.groupby('Hour')['Temp'].mean()

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(avg_light_per_hour.index, avg_light_per_hour.values, marker='o', linestyle='-', color='orange')

# Add titles and labels
plt.title('Average Light Intensity Per Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Light Intensity')
plt.xticks(range(0, 24))  # Ensure all hours are shown on the x-axis
plt.grid(True)

# Show the plot
plt.show()
