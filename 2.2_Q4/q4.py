from matplotlib import pyplot as plt
import scipy.integrate as integrate
from math import exp, factorial
import numpy as np

x = np.linspace(-1.5, 1.5, num=200)


def f(t):
  return (exp(-1*pow(t,2)))

def t_approx(t):
  return (1 - pow(t, 2) + pow(t,4)/2 - pow(t, 6)/6 + pow(t, 8)/24)

fx = [f(i) for i in x]
px = [t_approx(i) for i in x]

error = [abs(f - p) for f, p in zip(fx, px)]

rel_error = [ abs(f - p)/f for f, p in zip(fx, px)]


print(fx, px, sep='\n')

fig, ax = plt.subplots(2)

ax[0].set_aspect('equal')
ax[0].grid(True, which='both')
ax[1].set_aspect('equal')
ax[1].grid(True, which='both')

ax[0].axhline(y=0, color='k')
ax[0].axvline(x=0, color='k')
ax[1].axhline(y=0, color='k')
ax[1].axvline(x=0, color='k')


ax[0].plot(x, error, 'b--', label='error')
ax[0].plot(x, rel_error, 'r--', label='relative error')
ax[0].plot(x, [max(error) for i in x], 'g--', label='bound')


ax[1].plot(x, fx, 'k', label='f(x)')
ax[1].plot(x, px, 'y--', label='Pn(x)')

ax[0].legend(bbox_to_anchor=(1,1), loc="upper left")
ax[1].legend()

#plt.savefig("e_x_sq.png")

plt.show()