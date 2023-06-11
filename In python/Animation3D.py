import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from scipy.integrate import odeint

sigma = 10
beta = 8/3
rho = 1

def ele(k, t):
    x, y, z = k
    dydt = [sigma*(y - x), rho*x - x*z - y, x*y - beta*z]
    return dydt

T=200
N=5000

t = np.linspace(0,T, N)

init = [10, 10, 10]
sol = odeint(ele, init, t)

x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]

fig = plt.figure(1)
ax = fig.gca(projection='3d')

ax.set_xlim(np.min(x)-0.1,np.max(x)+0.1)
ax.set_ylim(np.min(y)-0.1,np.max(y)+0.1)
ax.set_zlim(np.min(z)-0.1,np.max(z)+0.1)
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
ax.set_ylabel('Z(t)')
plt.grid()

dot, = plt.plot([], [], [],'ro')
line, =plt.plot([], [], [],'b-')

def animate(i):
    dot.set_data_3d(x[i],y[i], z[i])
    line.set_data_3d(x[:i],y[:i], z[:i])
    return line, dot

anim = animation.FuncAnimation(fig, animate, frames=N, interval=1, blit=True, repeat=True)

#anim.save('Curve di lissajous 3d .mp4', fps=100, extra_args=['-vcodec', 'libx264'])
plt.show()