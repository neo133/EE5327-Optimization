import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import meshgrid
import matplotlib.pyplot as plt
x1 = np.arange(-10,10,0.01)
x2 = np.arange(-10,10,0.01)
X1,X2 = meshgrid(x1, x2)
#Z = np.sin(2*np.abs(X-0.3)+2*np.sin(5*Y))
f=X1*X2   
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X1, X2, f)

plt.show()