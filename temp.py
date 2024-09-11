import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
file_path = 'temp.csv'
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'])

# Round the temperature values to the nearest integer
df['Rounded_Temp'] = df['Temp'].round()

# Count the frequency of each rounded temperature
temp_counts = df['Rounded_Temp'].value_counts().sort_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
temp_counts.plot(kind='bar', color='blue', edgecolor='black')

# Add titles and labels
plt.title('Frequency of Each Rounded Temperature')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Show the bar chart
plt.show()
