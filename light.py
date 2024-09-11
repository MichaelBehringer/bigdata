import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
file_path = 'light.csv'
df = pd.read_csv(file_path, delimiter=';', parse_dates=['Time'], dayfirst=True)

# Define the bin edges (intervals of 50 units)
bins = range(0, 1075, 50)  # 1075 to include the last value up to 1023

# Bin the light intensity values
df['Binned_Temp'] = pd.cut(df['Temp'], bins=bins, right=False)

# Count the frequency of each bin
bin_counts = df['Binned_Temp'].value_counts().sort_index()

# Create the bar chart
plt.figure(figsize=(12, 6))
bin_counts.plot(kind='bar', color='orange', edgecolor='black')

# Add titles and labels
plt.title('Frequency of Light Intensity Binned by 50 Units')
plt.xlabel('Light Intensity Range')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')  # Rotate x labels for better readability

# Show the bar chart
plt.show()
