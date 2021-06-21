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
line0, =ax.plot(r, 0., color ='y', marker = 'o', markersize = '20', zorder=1)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_ylim(0,1.02*t)
#ax.scatter(r,t,c='y',s=15,zorder=1)
line1, = ax.plot([0, 0],[0,t], 'bo', linewidth = 1, markersize=5, zorder=0)
line2, = ax.plot([0, 0],[10,t-10], 'ro', linewidth = 1, markersize=4, zorder=0)


def update(angle):
    line1.set_data([angle, angle],[0,t])#[0,t] where '0' is focus point and 't' is animating point
    line2.set_data([angle, angle],[0,t-10])
    line1.set_zorder('0')
    line2.set_zorder('0')
    line0.set_zorder('1')
    return line0, line1, line2

frames = np.linspace(0,2*np.pi,120)

fig.canvas.draw()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=10)

plt.show()