###############################################
#                  TASK INFO                  #
#                                             #
#  -  The joint is perfectly flat, meaning    #
#   no energy can be passed into the system.  #
#  - The cargo is much less in size than the  #
#             length of the stem.             #
#  ------------------------------------------ #
#  To see the calculation of the differential #
#      equation and the whole logic behind    #
#      solving the case, see the attached     #
#                  .pdf file.                 #
###############################################

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as diff
import matplotlib.animation as animation
import math
from time import time

# initialization
fstopping_force = 1.0
falpha = 60
g = 9.8


class Pendulum:
    def __init__(self,
                 angles=[60, 100],
                 length=1.0,
                 stopping_force=1.0,
                 center=(0, 0)):
        self.angles = np.asarray(angles, dtype='float') * np.pi / 180.
        self.center = center
        self.length = length
        self.stopping_force = stopping_force

        self.time_elapsed = 0
        self.graph_data = [[], [], []]  # time, alpha, ang_vel

    def get_alpha(self):
        return self.angles[0]

    def get_angular_velocity(self):
        return self.angles[1]

    def differential(self, angles, t):
        self.graph_data[0].append(self.time_elapsed)
        self.graph_data[1].append(angles[0])
        self.graph_data[2].append(angles[1])

        return [self.get_angular_velocity(),
                - g / self.length * sin(self.get_alpha()) - self.stopping_force * self.get_angular_velocity()]

    def calculate_position(self):
        x = np.cumsum([self.center[0], self.length * sin(self.get_alpha())])
        y = np.cumsum([self.center[1], - self.length * cos(self.get_alpha())])
        return (x, y)

    def update(self, dt):
        self.angles = diff.odeint(self.differential,
                                  self.angles,
                                  [0, dt])[1]
        self.time_elapsed += dt


# Figures
pendulum_figure = plt.figure(figsize=(12, 8))
pendulum_graph = plt.subplot2grid((2, 2), (0, 0), colspan=1, rowspan=2)
alpha_graph = plt.subplot2grid((2, 2), (0, 1))

pendulum_graph.set_title('Pendulum simulation. Stopping force = {}'.format(fstopping_force))
pendulum_graph.set_xlim(-2, 2)
pendulum_graph.set_ylim(-2, 2)

alpha_graph.set_title('x(t)=l*sin(alpha(t))')
alpha_graph.set_ylabel('d(alpha), rad')
alpha_graph.set_xlim(0, 20)
alpha_graph.set_ylim(-falpha * math.pi / 90, falpha * math.pi / 90)

pendulum_graph.grid()
alpha_graph.grid()
############

pendulum = Pendulum(angles=[60, 100], length=1, stopping_force=1.0, center=(0, 0))
frame = 1. / 30  # 30 fps

############

# legend
line, = pendulum_graph.plot([], [], '-', lw=3, color='b')
line_alpha, = alpha_graph.plot([], [], lw=2)
text_time = pendulum_graph.text(0.02, 0.95, '', transform=pendulum_graph.transAxes)
text_alpha = pendulum_graph.text(0.02, 0.90, '', transform=pendulum_graph.transAxes)


def init():
    # initialize animation details
    line_alpha.set_data([], [])
    line.set_data([], [])
    text_time.set_text('')
    text_alpha.set_text('')
    return line_alpha, line, text_time, text_alpha


def animate(i):
    # one animation frame
    pendulum.update(frame)

    line_alpha.set_data(pendulum.graph_data[0], pendulum.graph_data[1])
    line.set_data(*pendulum.calculate_position())
    text_time.set_text('Time = %.1f' % pendulum.time_elapsed)
    text_alpha.set_text('Alpha = %.3f rad' % pendulum.get_alpha())
    return line_alpha, line, text_time, text_alpha


t0 = time()
animate(0)
t1 = time()
interval = 1000 * frame - (t1 - t0)

anim = animation.FuncAnimation(pendulum_figure, animate, frames=350,
                               interval=interval, blit=True, init_func=init)

anim.save('pendulum_demonstration.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
