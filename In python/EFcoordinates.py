import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

rs = 3

#%% inward light rays

def drdx(x, r):
    return (r - rs)/(r + rs)

r0 = 2.8

x = np.linspace(0, 13, 100)

sol = odeint(drdx, y0=r0, t=x, tfirst=True)

rsol = sol.T[0]

plt.plot(rsol, x)
plt.plot(np.ones(len(x)) * rs, x, color='k')
plt.show()

#%% outward light rays

def drdx(x, r):
    return -(r - rs)/(r + rs)

r0 = 0.8

x = np.linspace(0, 13, 100)

sol = odeint(drdx, y0=r0, t=x, tfirst=True)

rsol = sol.T[0]

plt.plot(rsol, x)
plt.plot(np.ones(len(x)) * rs, x, color='k')
plt.show()