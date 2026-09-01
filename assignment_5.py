import numpy as np

# 1
arr = np.array([10, 20, 30, 40, 50])

print(arr + 2)
print(arr * 3)
print(arr / 2)


# 2
arr = np.array([1, 2, 3, 6, 4, 5])
print(arr[::-1])

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
freq_x = np.bincount(x)
most_frequent_x = np.argmax(freq_x)
indices_x = np.where(x == most_frequent_x)[0]

print(most_frequent_x)
print(indices_x)

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
freq_y = np.bincount(y)
most_frequent_y = np.argmax(freq_y)
indices_y = np.where(y == most_frequent_y)[0]

print(most_frequent_y)
print(indices_y)


# 3
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0, 1])
print(arr[2, 0])


# 4
Agrim = np.linspace(10, 100, 25)

print(Agrim.ndim)
print(Agrim.shape)
print(Agrim.size)
print(Agrim.dtype)
print(Agrim.nbytes)

transpose = Agrim.reshape(25, 1)
print(transpose)

print(Agrim.T)


# 5
ucs420_Agrim = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print(np.mean(ucs420_Agrim))
print(np.median(ucs420_Agrim))
print(np.max(ucs420_Agrim))
print(np.min(ucs420_Agrim))
print(np.unique(ucs420_Agrim))

reshaped_ucs420_Agrim = ucs420_Agrim.reshape(4, 3)
print(reshaped_ucs420_Agrim)

resized_ucs420_Agrim = np.resize(ucs420_Agrim, (2, 3))
print(resized_ucs420_Agrim)
