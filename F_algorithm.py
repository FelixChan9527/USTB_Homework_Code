import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.zeros(a.shape)
print(a, b)
b = a
b[2, 2] = 90
print(a, b)