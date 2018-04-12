import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Interesting example from...
https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
"""

def measure(n): 
    """Measurement model. return two coupled measurements."""
    m1 = stats.norm.rvs(size=n)
    m2 = stats.norm.rvs(scale=0.5, size=n)
    return m1+m2, m1-m2

m1,m2 = measure(2000)
#print(m1.shape)
#print(m2.shape)

xmin=m1.min()
xmax=m1.max()
ymin=m2.min()
ymax=m2.max()

# 100x100 mesh grid for coordinate values
X,Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]

# XY coordinate to all mesh grids
positions = np.vstack([X.ravel(),Y.ravel()])
values = np.vstack([m1,m2])

# stas.gaussian_Kernel Density Estimation! 
kernel = stats.gaussian_kde(values)

# Z as value from estimated kernel to each mesh grid
Z = np.reshape(kernel.evaluate(positions).T, X.shape)

# Plot 
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

# Z as color map image
ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,
    extent=[xmin, xmax, ymin, ymax])
ax.plot(m1,m2,'k.',markersize=2)

ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin,ymax])

plt.show()




