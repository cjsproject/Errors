import numpy as np
from matplotlib import pyplot as plt
from math import exp, factorial

"""
f(x) = (e^x - e^-x)/(2x)
"""

x = np.linspace(-0.25, 0.25, num=20)
# a value close to 0; f(0) not defined
a = 0.25


def f(t):
  return (1/(2*t))*(exp(t)-exp(-t))

  
# generalized derivative: (dy/dx)^n?
def dydx(v, degree):
  h = exp(-5)
  if degree == 0: 
    return f(v)
  elif degree > 1:
    return dydx((f(v+h) - f(v))/(h), degree-1)
  
  return (f(v+h) - f(v))/(h)

# Finds nth taylor polynomial
def nth_tayl(n):
  if n >= 0:
    summation = np.zeros(len(x))
    for i in range(n+1):
      for j in range(len(x)):
        summation[j] += (dydx(a, i)*pow((x[j]-a), i))/factorial(i)
  return summation

# array of domain values for Pn(x)
p = []

#similar to the main matlab code
for n in range(1, 5):
  p.append(nth_tayl(n))

fx = [f(i) for i in x]

fig, ax = plt.subplots()

#ax.set_aspect('equal')
ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

ax.plot(x, fx, 'k', label='f(x)')
# has the same behaviour as y=f'(a)
ax.plot(x, p[0], 'r--', label='P1(x)')
ax.plot(x, p[1], 'g--', label='P2(x)')
ax.plot(x, p[2], 'b--', label='P3(x)')
ax.plot(x, p[3], 'y--', label='P4(x)')

# take note of the very small range of y
# this allows us to see the curvature 
# more obviously. also helps check the
# polynomial outputs
ax.set_ylim(ymin=0.965, ymax=1.015)

ax.legend()
plt.title("f(x) = (e^x - e^-x)/(2x)")
#plt.savefig("q6_c.png")

plt.show()