"""
Matplotlib Animation Example

author: Oguz Han ATAS
email: oguz.atas@ogr.iu.edu.tr
website: http://oguzhanatas.github.com
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
text = ax.text(-4, 4, '',color='red')
line, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    line2.set_data([], [])
    text.set_text('')
    return text, line, line2,

# animation function.  This is called sequentially
def animate(i):
    
    x = np.linspace(-5, 5, 1000)
    x2 = np.linspace(-5, 5, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    y2 = np.sin(2 * np.pi * (x2 + 0.01 * i))
    text.set_text('time = %.1f' % i)#where 'i' is frame count
    

    line.set_data(x, y)
    line2.set_data(x2, y2)
    return text, line, line2,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=300, interval=10, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#anim.save('./fig_output/'+'particle_box.gif', writer='PillowWriter', fps=30)

plt.show()
