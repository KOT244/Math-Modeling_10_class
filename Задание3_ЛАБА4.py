def polnmehenerg(m,v,g,h):
    E = m*g*h+m*v**2/2
    return E
from myconst import UskSvPad as g
m = 1
v = 1
h = 1
tab = polnmehenerg(m,v,g,h)
print(tab)

