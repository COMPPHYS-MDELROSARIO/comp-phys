'''
HW03
Matthew del Rosario
Matthew Español


Takes the function Psi and finds the probability density of it.
Finally it plots both the function psi and its probability density.
'''

#%matplotlib osx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d


def psi(x1, x2, n1 = 1, n2 = 2, a = 1.0):
    return 2/a*(np.sin(n1*x1*np.pi/a) * np.sin(n2*x2*np.pi/a) - np.sin(n1*x2*np.pi/a) * np.sin(n2*x1*np.pi/a))

def prob_density(p):
    return p**2

def antisym(x1, x2, n1 = 1, n2 = 2, a = 1.0):
    density = prob_density(psi(x1, x2, n1, n2, a))
    return density


fig = plt.figure()
plt.suptitle('Antisymmetric Spatial Wave Function', fontsize=14, fontweight='bold')
fig.subplots_adjust(top=0.85) #Without this, you won't be able to see the plot #Moves plots down so title fits

ax = fig.add_subplot(121, projection='3d')
x = y = np.linspace(-1, 1, 100)
xv, yv = np.meshgrid(x,y)
z = psi(xv, yv)
plt.title('Wave Function')
#ax.plot_wireframe(xv, yv, z, rstride=4, cstride=4, linewidth=1)
ax.plot_surface(xv, yv, z, rstride =1, cstride =1, cmap=cm.nipy_spectral, linewidth=0)


ax = fig.add_subplot(122, projection='3d')
x = y = np.linspace(-1, 1, 100)
xv, yv = np.meshgrid(x,y)
z = antisym(xv, yv)
plt.title('Probability Density')
#ax.plot_wireframe(xv, yv, z, rstride=4, cstride=4, linewidth=1)
ax.plot_surface(xv, yv, z, rstride =1, cstride =1, cmap=cm.nipy_spectral, linewidth=0)
plt.show()