import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint
import sympy as sym

T=2*np.pi
N=5000
trail = 99

h = sym.symbols('h', cls=sym.Function)
q, p = sym.symbols('q, p')
h = p**2 + q**2 + q**(4)

fx = sym.lambdify([q, p], h.diff(p), "numpy")
fy = sym.lambdify([q, p], -h.diff(q), "numpy")

def ele(y, t):
    a, b = y
    dydt = [fx(a, b), fy(a, b)]
    return dydt

y0 = [1, 1]
t = np.linspace(0, T, N)

sol = odeint(ele, y0, t)

def fx(t):
    return np.exp(-t)*np.cos(t)

def fy(t):
    return np.exp(-t)*np.sin(t)


x = sol[:, 0]
y = sol[:, 1]


fig, ax = plt.subplots(1)
ax.set_xlim(np.min(x)-0.1,np.max(x)+0.1)
ax.set_ylim(np.min(y)-0.1,np.max(y)+0.1)
ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
plt.grid()

dot, = plt.plot([], [],'ro')
line, = plt.plot([], [],'b-')

def animate(i, trail=20):
    dot.set_data(x[i],y[i])
    line.set_data(x[:i],y[:i])
    #trail
    #line.set_data(x[i - trail:i],y[i - trail:i])
    return dot, line

anim = animation.FuncAnimation(fig, animate, frames=N, interval=1, blit=True, repeat=True)

#anim.save('Curve di lissajous.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


plt.show()