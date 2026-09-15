import numpy as np

# Q1. Sensor Readings

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

# a. Add 2°C to every reading
corrected_temperature = temperature + 2
print("Q1(a):", corrected_temperature)

# b. Convert Celsius to Fahrenheit
fahrenheit = (9 / 5) * corrected_temperature + 32
print("Q1(b):", fahrenheit)

# c. Readings greater than 32°C
readings_greater_32 = corrected_temperature[corrected_temperature > 32]
print("Q1(c):", readings_greater_32)

# d. Count readings greater than 32°C
count_greater_32 = np.sum(corrected_temperature > 32)
print("Q1(d):", count_greater_32)

# e. Explanation:
# Vectorization performs operations on the whole NumPy array
# without explicitly using a for loop, making processing faster.
# Boolean indexing creates a condition-based mask and directly
# selects the required elements.

# Q2. Daily Steps

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

# a. Total steps
print("\nQ2(a):", np.sum(steps))

# b. Mean steps
print("Q2(b):", np.mean(steps))

# c. Maximum and minimum
print("Q2(c) Maximum:", np.max(steps))
print("     Minimum:", np.min(steps))

# d. Total steps for each day
print("Q2(d):", np.sum(steps, axis=0))

# e. Total steps for each user
print("Q2(e):", np.sum(steps, axis=1))

# f. Position of maximum value
position = np.unravel_index(np.argmax(steps), steps.shape)
print("Q2(f) Position:", position)


# Q3. NumPy Slicing

# a. Create array
original = np.array([1, 2, 3, 4, 5, 6])

# b. Slice index 1 to 4
subset = original[1:5]

# c. Modify subset
subset[0] = 999

print("\nQ3(c) Original:", original)
print("Q3(c) Subset:", subset)

# d. Slice using copy()
copied_array = original[1:5].copy()
copied_array[0] = 500

print("Q3(d) Original:", original)
print("Q3(d) Copied:", copied_array)

# e. Create 3 x 4 matrix
matrix = np.arange(1, 13).reshape(3, 4)
print("\nQ3(e):\n", matrix)

# f. Indexing and slicing
print("Q3(f) First row:", matrix[0])
print("Q3(f) Last row:", matrix[-1])
print("Q3(f) Second column:", matrix[:, 1])
print("Q3(f) Rows 1-2, Columns 2-3:\n", matrix[0:2, 1:3])

# g. flatten() and ravel()
flattened = matrix.flatten()
ravelled = matrix.ravel()

print("\nQ3(g) flatten():", flattened)
print("Q3(g) ravel():", ravelled)

# h. Modify ravel()
ravelled[0] = 1000

print("Q3(h) Matrix after ravel modification:\n", matrix)

# i. Modify flatten()
flattened[1] = 2000

print("Q3(i) Matrix after flatten modification:\n", matrix)

# j. Shape, dimensions, size and dtype
print("\nQ3(j) Shape:", matrix.shape)
print("Q3(j) ndim:", matrix.ndim)
print("Q3(j) Size:", matrix.size)
print("Q3(j) dtype:", matrix.dtype)

# Q4. Ordinary Least Squares

X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

# a. Shape and dimensions
print("\nQ4(a) Shape:", X.shape)
print("Q4(a) Dimensions:", X.ndim)

# b. Transpose
X_T = X.T
print("Q4(b) X.T:\n", X_T)

# c. X.T @ X
XTX = X.T @ X
print("Q4(c) X.T @ X:\n", XTX)

# d. Inverse
XTX_inverse = np.linalg.inv(XTX)
print("Q4(d) Inverse:\n", XTX_inverse)

# e. OLS equation
# beta = (X.T X)^(-1) X.T y
beta = XTX_inverse @ X.T @ y

print("Q4(e) Beta:", beta)

# f. Coefficients
print("\nQ4(f)")
print("Sleep coefficient:", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient:", beta[2])

# g. Prediction for new user
new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nQ4(g) New user:", new_user)
print("Predicted assistance score:", predicted_score)
