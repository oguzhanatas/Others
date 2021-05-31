'this code plot 3D figure with count density profile layer by layer'
'you can change the all functions what you need.'
'https://matplotlib.org/1.3.1/mpl_toolkits/mplot3d/tutorial.html#toolkit-mplot3d-tutorial'
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x=np.abs(np.random.standard_normal(10**6)*100)
y=np.abs(np.random.standard_normal(10**6)*50)
z=np.random.uniform(low=0.,high=100,size=10**6)

def densityColor(x,y,lognorm=True):
    with np.errstate(divide='ignore'):
        xe,ye=np.linspace(min(x),max(x),100),np.linspace(min(y),max(y),100)
        h,xe,ye=np.histogram2d(x,y,(xe,ye))
        xidx,yidx=np.clip(np.digitize(x,xe),0,h.shape[0]-1),np.clip(np.digitize(y,ye),0,h.shape[1]-1)
        c=h[xidx,yidx]
        if lognorm==True:
            vmin,vmax=10**0,10**2
            norm=matplotlib.colors.LogNorm(vmin=vmin,vmax=vmax)
        else:
            vmin,vmax=0,100
            norm=matplotlib.colors.Normalize(vmin=vmin,vmax=vmax)
        cmap=plt.cm.get_cmap('RdYlBu_r')
        return c,norm,cmap

fig = plt.figure()
ax = fig.gca(projection='3d')

'plotting x-y plane for each mean z axis'
#1st layer
mask=(z>0)&(z<10)
c,norm,cmap=densityColor(x[mask],y[mask],lognorm=False)
ax.scatter(x[mask],y[mask],[np.mean(z[mask])]*len(x[mask]),c=c,norm=norm,cmap=cmap,s=1)
#2nd layer
mask2=(z>20)&(z<30)
c2,norm2,cmap2=densityColor(x[mask2],y[mask2])
ax.scatter(x[mask2],y[mask2],[np.mean(z[mask2])]*len(x[mask2]),c=c2,norm=norm2,cmap=cmap2,s=1)
#3rd layer
mask3=(z>50)&(z<60)
c3,norm3,cmap3=densityColor(x[mask3],y[mask3])
ax.scatter(x[mask3],y[mask3],[np.mean(z[mask3])]*len(x[mask3]),c=c3,norm=norm3,cmap=cmap3,s=1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()