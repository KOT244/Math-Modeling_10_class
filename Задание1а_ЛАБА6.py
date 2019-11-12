import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-2*np.pi,2*np.pi,0.1)
R = 4
x = R*(t-np.sin(t))
y = R*(1-np.cos(t))
plt.plot(x,y)
plt.show
