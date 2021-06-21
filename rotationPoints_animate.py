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
t = 50

fig = plt.figure()
ax = fig.gca(projection = 'polar')
fig.canvas.set_window_title('Doppler')
print(r,t)

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_ylim(0,1.02*t)
#ax.scatter(r,t,c='y',s=15,zorder=1)
line0, =ax.plot(r, 0., color ='y', marker = 'o', markersize = '20', zorder=1)#star location
line1, = ax.plot([0, 0],[0,t], 'bo', linewidth = 1, markersize=5, zorder=0)#planet1 location
line2, = ax.plot([0, 0],[0,t-10], 'go', linewidth = 1, markersize=4, zorder=0)#planet2 location
line3, = ax.plot([0, 0],[0,t-20], 'ro', linewidth = 1, markersize=4, zorder=0)#planet3 location


def update(angle):
    #print(angle)
    line1.set_data([angle, angle],[0,t])#[0,t] where '0' is focus point and 't' is animating point
    line2.set_data([angle, angle+1],[0,t-10])
    line3.set_data([angle, angle+1.5],[0,t-20])
    line0.set_zorder('1')
    line1.set_zorder('0')
    line2.set_zorder('0')
    line3.set_zorder('0')
    return line0, line1, line2, line3

frames = np.linspace(0,2*np.pi,120)

fig.canvas.draw()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=10)
#ani.save('./fig_output/'+'rotationPoints_animate.gif', writer='PillowWriter', fps=30)
plt.show()