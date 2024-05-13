import matplotlib.pyplot as pll

import numpy as ny

ll = ny.random.randint(80, size = (80))
kk = ny.random.randint(80, size = (80))
pp = 8*ny.random.randint(80, size = (80))
jj = ny.random.randint(80, size = (80))

pll.title("Soon")

pll.scatter(ll,kk, s = pp, c = jj, alpha = 0.4,cmap ='twilight')

pll.colorbar()
pll.show()