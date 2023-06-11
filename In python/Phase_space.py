from pylab import *

g = 4
w = 2
N = 5

x, y = meshgrid(arange(-N, N, 0.1), arange(-N, N, 0.1))

xdot = y
ydot = -g*y - w**2*x

streamplot(x, y, xdot, ydot)
show()