import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

T=20
N=5000
trail = 99
g = np.sqrt(8) - 0.1
A = 10


def ele(z, t):
    x, y = z
    dydt = [x - 2*y - x*(x**2 + y**2), 2*x + y - y*(x**2 + y**2)]
    return dydt

y0 = [0.25, -0.1]
t = np.linspace(0, T, N)

sol = odeint(ele, y0, t)

x = sol[:, 0]
y = sol[:, 1]


fig, ax = plt.subplots(1)
ax.set_xlim(np.min(x)-0.1,np.max(x)+0.1)
ax.set_ylim(np.min(y)-0.1,np.max(y)+0.1)
ax.set_xlabel('q(t)')
ax.set_ylabel('p(t)')
plt.grid()

dot, = plt.plot([], [],'ro')
line, = plt.plot([], [],'b-')

def animate(i, trail=20):
    dot.set_data(x[i],y[i])
    line.set_data(x[:i],y[:i])
    #trail
    #line.set_data(x[i - trail:i],y[i - trail:i])
    return dot, line

anim = animation.FuncAnimation(fig, animate, frames=N, interval=1, blit=True, repeat=False)



#anim.save('Hamiltoniana di Lorenzo.mp4', writer='imagemagick')

plt.show()
