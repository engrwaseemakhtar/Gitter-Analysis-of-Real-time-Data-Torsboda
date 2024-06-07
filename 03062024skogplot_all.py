import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('./20240507-1106.csv', header=None, names=['Timestamp'])

# Convert timestamps to human-readable format
data['Human_Readable'] = data['Timestamp'].apply(lambda x: datetime.utcfromtimestamp(float(x)).strftime('%Y-%m-%d %H:%M:%S'))

# Calculate time differences (in seconds) between consecutive timestamps
data['Timestamp'] = data['Timestamp'].astype(float)
data['Time_Diff'] = data['Timestamp'].diff().dropna()  # Drop the first NaN value created by diff()

# Plot the jitter (variation in time differences)
plt.figure(figsize=(10, 6))
plt.plot(data['Time_Diff'], marker='o')
plt.xlabel('Sample Index')
plt.ylabel('Time Difference (s)')
plt.title('Jitter (Time Difference Between Consecutive Timestamps)')
plt.grid(True)
plt.show()

# Plot the histogram of the time differences
plt.figure(figsize=(10, 6))
plt.hist(data['Time_Diff'], bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Time Difference (s)')
plt.ylabel('Frequency')
plt.title('Histogram of Time Differences')
plt.grid(True)
plt.show()

# Plot the ECDF of the time differences
sorted_data = np.sort(data['Time_Diff'])
ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

plt.figure(figsize=(10, 6))
plt.plot(sorted_data, ecdf, marker='.', linestyle='none')
plt.xlabel('Time Difference (s)')
plt.ylabel('ECDF')
plt.title('Empirical Cumulative Distribution Function (ECDF) of Time Differences')
plt.grid(True)
plt.show()

# Print the human-readable dates and time differences
print(data[['Human_Readable', 'Time_Diff']])

# Save the human-readable dates and time differences to a new CSV file
data.to_csv('./20240507-1106_Human_Readable_With_Jitter.csv', index=False)

