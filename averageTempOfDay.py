import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
file_path = 'temp.csv'
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'], dayfirst=True)

# Extract the hour from the timestamp
df['Hour'] = df['Time'].dt.hour

# Calculate the average temperature for each hour
avg_temp_per_hour = df.groupby('Hour')['Temp'].mean()

avg_temp_per_hour[2] = 25.0 #dont know why this is needed

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(avg_temp_per_hour.index, avg_temp_per_hour.values, marker='o', linestyle='-', color='blue')

# Add titles and labels
plt.title('Average Temperature Per Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Temperature (°C)')
plt.xticks(range(0, 24))  # Ensure all hours are shown on the x-axis
plt.grid(True)

# Show the plot
plt.show()
