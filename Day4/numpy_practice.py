import numpy as np
array1=np.array([1, 2, 3, 4, 5, 6]) #1D array
array2=np.array([[1, 2, 3], [4, 5, 6]]) #2D array

#Indexing and slicing
print("1D Array:")
print(array1[0])        # 1 (first element)
print(array1[-1])         # 6 (last element)
print(array1[1:4])        # [2, 3, 4]

print("\n2D Array:")
print(array2[0, 1])     # 2  (row 0, col 1)
print(array2[:, 1])     # [2, 5]  (entire column 1)
print(array2[1, :])     # [4, 5, 6]  (entire row 1)

# array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nArray Operations:")
print("Add:", a + b)   # [5, 7, 9]
print("Subtract:", a - b)   # [-3, -3, -3]
print("Multiply:", a * b)   # [4, 10, 18]
print("Divide:", a / b)   # [0.25, 0.4, 0.5]

#aggregate functions
arr=np.array([2,4,6,7,9,15])

print("\nAggregate Functions:")
print("Max:", arr.max())  # 15
print("Min:", arr.min())  # 2
print("Sum:", arr.sum())  # 43
print("Mean:", arr.mean())  # 7.166666666666667
print("Std:", arr.std()) # 4.183300132670378

#reshaping
arr = np.arange(12)          # [0, 1, 2, ..., 11]
reshaped = arr.reshape(3, 4) # 3 rows, 4 columns
flattened = reshaped.flatten()
print("\nReshaping:")
print("Original:", arr) 
print("Reshaped:\n", reshaped)
print("Flattened:", flattened)
print("Shape of reshaped array:", reshaped.shape)  # (3, 4)