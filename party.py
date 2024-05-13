import matplotlib.pyplot as plt
import numpy as np

ll = np.random.randint(100, size = (100))
kk = np.random.randint(100, size = (100))
size = 10* np.random.randint(100, size = (100))
col = np.random.randint(100, size = (100))

plt.title("Party")
plt.scatter( ll, kk, s = size, c = col, alpha = 0.4, cmap = 'plasma')
plt.colorbar()
plt.show()