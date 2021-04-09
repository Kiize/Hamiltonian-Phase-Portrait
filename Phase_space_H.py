#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

p, q = sp.symbols('p q')
H = p**2/2 - 1/q + 1/2 * q**(-2)


fig = plt.figure(figsize=(10, 8), dpi=80)

x,y = np.meshgrid(np.linspace(-10,10,30),np.linspace(-10,10,30))

print(sp.diff(H, p), ',', -sp.diff(H, q))

pdot = sp.lambdify(q, -sp.diff(H, q), 'numpy')
qdot = sp.lambdify(p, sp.diff(H, p), 'numpy')

u = qdot(y)
v = pdot(x)

E = sp.lambdify([p, q], H, 'numpy')

plt.streamplot(x,y,u,v, color = E(x, y), cmap = 'autumn')
plt.savefig('H Pendolo1.pdf')
plt.show()

