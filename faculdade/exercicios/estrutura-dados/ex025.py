import numpy as np

valores = np.array([
    [10, 2000],
    [20, 3000],
    [30, 4000],
    [40, 5000]
])

print(valores.shape[0])
print(valores.shape[1])
print(np.mean(valores[:,1]))
print(np.max(valores[:,0]))