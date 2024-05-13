import matplotlib.pyplot as plt
import numpy as np

ll = np.array([32,45,54,67,88,66,89])
kk = np.array([22,43,45,46,67,78,75])
col = np.array([0,10,23,34,45,56,67])

plt.scatter(ll,kk,c = col, cmap = 'viridis')

plt.colorbar()
plt.show()