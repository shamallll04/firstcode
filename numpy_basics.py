# numpy_basics.py
# Day 6 – NumPy Basics for AI

import numpy as np

print("=== NumPy Basics ===")

# Create array
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# Array operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# 2D Array (Matrix)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(matrix)

# Shape of array
print("Shape:", matrix.shape)

# Multiply array
print("Array * 2:", arr * 2)

# Conditional filtering
print("Values greater than 25:", arr[arr > 25])
