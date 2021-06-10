"""
Animation of Elastic collisions with Gravity

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!

modified by oguzhanatas
"""
import numpy as np
from numpy.core.fromnumeric import size
from scipy.spatial.distance import pdist, squareform

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

class ParticleBox:
    """Orbits class
    
    init_state is an [N x 4] array, where N is the number of particles:
       [[x1, y1, vx1, vy1],
        [x2, y2, vx2, vy2],
        ...               ]

    bounds is the size of the box: [xmin, xmax, ymin, ymax]
    """
    def __init__(self,
                 init_state = [[0.7, 1.5, 0, -1],
                               [1.2, 1.5, 0.5, 0.5],
                               [1.4, 1.9, -0.5, 0.5]],
                 bounds = [0, 2, 0, 2],
                 size = 0.03,
                 M = 1,
                 G = 9.8):
        self.init_state = np.asarray(init_state, dtype=float)
        self.M = M * np.ones(self.init_state.shape[0])
        self.size = size
        self.state = self.init_state.copy()
        self.time_elapsed = 0
        self.bounds = bounds
        self.G = G
        #print(self.state)
        
    def energy(self):
        """compute the energy of the current state"""
        count,u,k=len(self.M),[],[]
        for i in range(count):
            u.append(self.M[i]*self.G*self.state[i,1])
            k.append(0.5*self.M[i]*(self.state[0,2]**2+self.state[0,3]**2))
        tot=sum(u)+sum(k)
        return tot



    def step(self, dt):
        """step once by dt seconds"""
        self.time_elapsed += dt
        
        # update positions
        self.state[:, :2] += dt * self.state[:, 2:]

        # find pairs of particles undergoing a collision
        D = squareform(pdist(self.state[:, :2]))
        ind1, ind2 = np.where(D < 2 * self.size)
        unique = (ind1 < ind2)
        ind1 = ind1[unique]
        ind2 = ind2[unique]

        # update velocities of colliding pairs
        for i1, i2 in zip(ind1, ind2):
            # mass
            m1 = self.M[i1]
            m2 = self.M[i2]

            # location vector
            r1 = self.state[i1, :2]
            r2 = self.state[i2, :2]

            # velocity vector
            v1 = self.state[i1, 2:]
            v2 = self.state[i2, 2:]

            # relative location & velocity vectors
            r_rel = r1 - r2
            v_rel = v1 - v2

            # momentum vector of the center of mass
            v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)

            # collisions of spheres reflect v_rel over r_rel
            rr_rel = np.dot(r_rel, r_rel)
            vr_rel = np.dot(v_rel, r_rel)
            v_rel = 2 * r_rel * vr_rel / rr_rel - v_rel

            # assign new velocities
            self.state[i1, 2:] = v_cm + v_rel * m2 / (m1 + m2)
            self.state[i2, 2:] = v_cm - v_rel * m1 / (m1 + m2) 



        # check for crossing boundary
        crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
        crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
        crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
        crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)

        self.state[crossed_x1, 0] = self.bounds[0] + self.size
        self.state[crossed_x2, 0] = self.bounds[1] - self.size

        self.state[crossed_y1, 1] = self.bounds[2] + self.size
        self.state[crossed_y2, 1] = self.bounds[3] - self.size

        self.state[crossed_x1 | crossed_x2, 2] *= -1
        self.state[crossed_y1 | crossed_y2, 3] *= -1

        # add gravity
        self.state[:, 3] -= self.M * self.G * dt
    
        


#------------------------------------------------------------
# set up initial state
np.random.seed(0)
init_state = 0.1 + np.random.random((int(input('enter the number of particles (exp. 3): ')), 4))
init_state[:, :2] *= 3.1
ss=float(input('enter the size of particles in m (exp. 0.03): '))
mm=float(input('enter the mass of particles in kg (exp. 1): '))
box = ParticleBox(init_state,size=ss,M=mm)
#box=ParticleBox()
dt = 1. / 30 # 30fps


#------------------------------------------------------------
# set up figure and animation
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0.1, top=0.9)
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-0.2, 2.2), ylim=(-0.2, 2.2))

# particles holds the locations of the particles
particles, = ax.plot([], [], 'r.')
#print(particles)


# rect is the box edge
rect = plt.Rectangle(box.bounds[::2],
                     box.bounds[1] - box.bounds[0],
                     box.bounds[3] - box.bounds[2],
                     ec='none', lw=2, fc='none')
ax.add_patch(rect)
time_text = ax.text(0.1, 0.875, '',color='red', transform=ax.transAxes)
energy_text = ax.text(0.1, 0.825, 'green', transform=ax.transAxes)
def init():
    """initialize animation"""
    global box, rect
    particles.set_data([], [])
    particles.set_alpha(0.6)
    particles.set_markeredgecolor('k')
    rect.set_edgecolor('none')
    time_text.set_text('')
    energy_text.set_text('')
    return particles, rect, time_text, energy_text

def animate(i):
    """perform animation step"""
    global box, rect, dt, ax, fig
    box.step(dt)

    ms = int(fig.dpi * 2 * box.size * fig.get_figwidth()
             / np.diff(ax.get_xbound())[0])
    
    # update pieces of the animation
    rect.set_edgecolor('k')
    particles.set_data(box.state[:, 0], box.state[:, 1])
    particles.set_markersize(ms)
    time_text.set_text('time = %.1f' % box.time_elapsed)
    energy_text.set_text('E$_{tot}$ = %.3f J' % box.energy())
    return particles, rect, time_text, energy_text

# choose the interval based on dt and the time to animate one step

ani = animation.FuncAnimation(fig, animate, frames=600,
                              interval=10, blit=True, init_func=init)


# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('./fig_output/'+'particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#ani.save('./fig_output/'+'particle_box.gif', writer='PillowWriter', fps=30)

plt.show()
