import numpy as np

# Define file path
file_path = "C:\\temp\\IN300_Dataset2.txt"

# Load data from text file assuming one value per line
try:
  data = np.loadtxt(file_path)
except FileNotFoundError:
  print(f"Error: File not found at {file_path}")
  exit()

if len(data) > 2500:
  print(f"Warning: Data length ({len(data)}) exceeds expected rows (2500).")
  print(f"Truncating data to the first 2500 elements.")
  data = data[:2500]

# Reshape data into a 2D array
data = data.reshape(2500, 1)

# Create 3D array
three_dim_array = data.reshape(250, 10, 1)

# Slice 2D array
sliced_array = data[2:5:10]

# Print original arrays and sliced array
print("Original 2D Array (first 5 rows):")
print(data[:5])

print("\nOriginal 3D Array (first element of the first sub-array):")
print(three_dim_array[0, 0, :])  # Print the first sub-array

print("\nSliced 2D Array:")
print(sliced_array)
