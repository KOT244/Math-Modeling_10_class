import numpy as np
import matplotlib.pyplot as plt
t = np.arange(-2*np.pi,2*np.pi,0.1)
R = 4
x = R*(np.cos(t)**3)
y = R*(np.sin(t)**3)
plt.plot(x,y)
plt.show
