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
from numpy.core.fromnumeric import repeat

r = 90  * (np.pi/180)
t = 250#circle radius
psize = 10#points multiplier

fig = plt.figure()
ax = fig.gca(projection = 'polar')
#fig.canvas.set_window_title('Doppler')

ax.set_theta_zero_location('N')#N,W,E,S
ax.set_theta_direction(-1)
ax.set_thetagrids([0,90,180,270])
ax.set_ylim(0,1.02*t)
ax.set_yticks([0.45*150,0.72*150,150,1.52*150])
ax.set_yticklabels([0.45*150,0.72*150,150,1.52*150],fontsize=7)
#ax.scatter(r,t,c='y',s=15,zorder=1)
line0, = ax.plot(r, 0., color ='y', marker = 'o', markersize = 10, zorder=1)#star location
ax.text(-1,15,'Sun',color='orange',fontsize=10,zorder=2)
line1, = ax.plot([],[], color='blue', marker='o', linewidth = 1, markersize=1*psize, zorder=0)#earth distance from sun
line2, = ax.plot([],[], color='yellow', marker='o', linewidth = 1, markersize=0.949*psize, zorder=0)#venus distance from sun
line3, = ax.plot([],[], color='darkgrey', marker='o', linewidth = 1, markersize=0.383*psize, zorder=0)#mercury distance from sun
line4, = ax.plot([],[], color='red', marker='o', linewidth = 1, markersize=0.532*psize, zorder=0)#mars distance from sun
#line5, = ax.plot([],[], color='orange', marker='o', linewidth = 1, markersize=2*psize, zorder=0)#jupiter distance from sun


def update(angle):
    #print(angle)
    #https://public.nrao.edu/ask/which-planet-orbits-our-sun-the-fastest/
    line1.set_data([angle*0.6],[150])#[0,t] where '0' is center point and 't' is distance from center
    line2.set_data([angle*0.73],[150*0.72])
    line3.set_data([angle],[150*0.45])
    line4.set_data([angle*0.5],[150*1.52])
    #line5.set_data([angle*0.27],[150*5.18])
    #line0.set_alpha(0.5)
    #line0.set_zorder('1')
    return line0, line1, line2, line3, line4, #line5

frames = np.linspace(0,10*np.pi,1000,endpoint=False)#'n*pi' where n is cycle count

#fig.canvas.draw()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, blit=True, repeat=True, interval=15)
ani.save('./fig_output/'+'rotationPoints_animate.gif', writer='PillowWriter', fps=30)
plt.show()