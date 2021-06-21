"""
Matplotlib Animation Example

author: Oguz Han ATAS
email: oguz.atas@ogr.iu.edu.tr
website: http://oguzhanatas.github.com
Please feel free to use and modify this, but keep the above information. Thanks!
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

r = 90  * (np.pi/180)
t = 160#distance
psize = 10#radius ratio

fig = plt.figure()
ax = fig.gca(projection = 'polar')
#fig.canvas.set_window_title('Doppler')

ax.set_theta_zero_location('N')#N,W,E,S
ax.set_theta_direction(-1)
ax.set_thetagrids([0,90,180,270])
ax.set_ylim(0,1.02*t)
ax.set_yticks([0.45*150,0.72*150,150])
ax.set_yticklabels([0.45*150,0.72*150,150],fontsize=7)
#ax.scatter(r,t,c='y',s=15,zorder=1)
line0, = ax.plot(r, 0., color ='y', marker = 'o', markersize = 10, zorder=1)#star location
ax.text(-1,15,'Sun',color='orange',fontsize=10,zorder=2)
line1, = ax.plot([0, 0],[0,t], 'bo', linewidth = 1, markersize=1*psize, zorder=0)#earth distance from sun
line2, = ax.plot([0, 0],[0,t*0.72], 'go', linewidth = 1, markersize=0.949*psize, zorder=0)#venus distance from sun
line3, = ax.plot([0, 0],[0,t*0.45], 'ro', linewidth = 1, markersize=0.383*psize, zorder=0)#mercury distance from sun


def update(angle):
    #print(angle)
    line1.set_data([angle, angle],[0,150])#[0,t] where '0' is focus point and 't' is animating point
    line2.set_data([angle, angle+1],[0,150*0.72])
    line3.set_data([angle, angle+1.5],[0,150*0.45])
    #line0.set_alpha(0.5)
    #line0.set_zorder('1')
    return line0, line1, line2, line3

frames = np.linspace(0,2*np.pi,120)

#fig.canvas.draw()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=15)
ani.save('./fig_output/'+'rotationPoints_animate.gif', writer='PillowWriter', fps=30)
plt.show()