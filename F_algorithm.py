import numpy as np
from numpy.core.numeric import Inf

W = np.array(
    [[0, 6, 1, 3, float("inf"), float("inf")],
     [1, 0, 4, float("inf"), 7, float("inf")], 
     [2, float("inf"), 0, float("inf"), 1, float("inf")], 
     [float("inf"), float("inf"), 5, 0, 2, 7], 
     [float("inf"), 6, 2, 8, 0, 5], 
     [7, float("inf"), 2, float("inf"), 2, 0]]
)

R = np.array(
    [[0, 2, 3, 4, 0, 0], 
     [1, 0, 3, 0, 5, 0], 
     [1, 0, 0, 0, 5, 0], 
     [0, 0, 3, 0, 5, 6], 
     [0, 2, 3, 4, 0, 6], 
     [1, 0, 3, 0, 5, 0]]
)

print("k={}".format(0))
print("W = ")
print(W)
print("R = ")
print(R)

temp_W = np.zeros(W.shape, dtype=float)
temp_R = np.zeros(W.shape, dtype=int)

for k in range(6):
    for i in range(6):
        for j in range(6):
            temp_W[i, j] = min(W[i, j], (W[i, k]+W[k, j]))
            if W[i, j] > W[i, k]+W[k, j]:
                temp_R[i, j] = k+1
            else:
                temp_R[i, j] = R[i, j]
    
    W = temp_W.copy()       # 一定要留意不能直接赋值
    R = temp_R.copy()
    print("k={}".format(k+1))
    print("W = ")
    print(W)
    print("R = ")
    print(R)

x = []
for i in range(6):
    x.append(W[i].sum())

print(x)

