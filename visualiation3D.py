'https://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#toolkit-mplot3d-tutorial'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x=np.abs(np.random.standard_normal(10**6)*100)
y=np.abs(np.random.standard_normal(10**6)*50)
z=np.random.uniform(low=0.,high=100,size=10**6)

def denssityColor(x,y):
    with np.errstate(divide='ignore'):
        xe,ye=np.linspace(min(x),max(x),100),np.linspace(min(y),max(y),100)
        h,xe,ye=np.histogram2d(x,y,(xe,ye))
        xidx=np.clip(np.digitize(x,xe),0,h.shape[0]-1)
        yidx=np.clip(np.digitize(y,ye),0,h.shape[1]-1)
        c=h[xidx,yidx]
        norm=matplotlib.colors.LogNorm(vmin=10**0,vmax=10**3)
        #norm=matplotlib.colors.Normalize(vmin=0,vmax=100)
        cmap=plt.cm.get_cmap('RdYlBu_r')
        #sc=plt.scatter(x,y,c=c,norm=matplotlib.colors.LogNorm(vmin=10**0,vmax=10**4),cmap=plt.cm.get_cmap('RdYlBu_r'),ec=None,alpha=0.6,s=1)
        return c,norm,cmap

fig = plt.figure()
ax = fig.gca(projection='3d')
c,norm,cmap=denssityColor(x[(z>0)&(z<10)],y[(z>0)&(z<10)])
ax.scatter(x[(z>0)&(z<10)],y[(z>0)&(z<10)],[5]*len(y[(z>0)&(z<10)]),c=c,norm=norm,cmap=cmap,s=1)
c1,norm1,cmap1=denssityColor(x[(z>40)&(z<50)],y[(z>40)&(z<50)])
ax.scatter(x[(z>40)&(z<50)],y[(z>40)&(z<50)],[45]*len(y[(z>40)&(z<50)]),c=c1,norm=norm1,cmap=cmap1,s=1)
#ax.plot_trisurf(x[(z>5)&(z<10)], y[(z>5)&(z<10)], z[(z>5)&(z<10)], cmap=cm.jet, linewidth=0.2)
#ax.plot_trisurf(x[(z>50)&(z<60)], y[(z>50)&(z<60)], z[(z>50)&(z<60)], cmap=cm.jet, linewidth=0.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()