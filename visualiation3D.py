'https://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#toolkit-mplot3d-tutorial'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

x=np.random.uniform(low=0.,high=1000,size=1000)
y=np.random.uniform(low=0.,high=500,size=1000)
z=np.random.uniform(low=0.,high=100,size=1000)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x[(z>5)&(z<10)], y[(z>5)&(z<10)], z[(z>5)&(z<10)], cmap=cm.jet, linewidth=0.2)
ax.plot_trisurf(x[(z>50)&(z<60)], y[(z>50)&(z<60)], z[(z>50)&(z<60)], cmap=cm.jet, linewidth=0.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()