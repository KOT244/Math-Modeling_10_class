from numpy import pi, tan, cos
from myconst import UskSvPad as g
a = pi/3
b = 30
h = 100
v = (g*h*((1/tan(b))**2/2*(cos(a))**2*(1-1/tan(b)*1/tan(a))))**0.5
print('v = ',v)

from numpy import e, pi
from myconst import Boltsman as k, Plank as h
T = 200
s = 300
N = (2/(pi)**0.5)*(h/(k*T)**1.5)*e**(-s/k*T)*e**(T/2)
print('N = ',N)
