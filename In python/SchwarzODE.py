import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

l = 7 #s.t. r**2 * y2 = l
rs = 3  #Schwarzschild radius
delta = 0

#%%
#coordinate tempo osservatore all'infinito
def dSdx(x, S):
    r, phi = S
    return [-(r - rs)/r,
            l/r**2 * (r - rs)/r]

r_0 = 6
phi_0 = 0
S_0 = (r_0, phi_0)

x = np.linspace(0, 30, 1000)

sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)
    

r_sol = sol.T[0]
phi_sol = sol.T[1]

'''
plt.polar(phi_sol, r_sol)
#plt.savefig('schwarzBH', dpi=1000)
plt.show()
'''

#%%
#coordinate parametro affine
l = 3*np.sqrt(3)/2 *rs

def U(r):
    return l**2/r**2 + 1 - r/(r - rs)

def f(r):
    return (1 - delta - U(r))*(r - rs)/r

def dSdx(x, S):
    r, phi = S
    return [-np.sqrt(f(r)),
            l/r**2]

r_0 = 3/2*rs
phi_0 = 0
S_0 = (r_0, phi_0)

x = np.linspace(0, 200, 1000)
t = np.linspace(0, 2*np.pi, 100)



sol = odeint(dSdx, y0=S_0, t=x, tfirst=True)


r_sol = sol.T[0]
phi_sol = sol.T[1]

#plt.polar(phi_sol, r_sol)
plt.plot(r_sol*np.cos(phi_sol), r_sol*np.sin(phi_sol))
plt.plot(rs*np.cos(t), rs*np.sin(t))
#plt.plot(x, r_sol)
plt.show()
