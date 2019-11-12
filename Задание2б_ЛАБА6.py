import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
R = 4
t = np.arange(-2*np.pi,2*np.pi,0.1)
x = R*(np.cos(t)**3)
y = R*(np.sin(t)**3)
fig,ax = plt.subplots()
anim_object, = plt.plot([],[],'o')
xdata, ydata = [],[]
ax.set_xlim(-5,5)
ax.set_ylim(-6,6)
def update(frame):
    xdata.append(R*(np.cos(frame)**3))
    ydata.append(R*(np.sin(frame)**3))
    anim_object.set_data(xdata,ydata)
    
ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(-2*np.pi,2*np.pi,0.1),
                    interval=300)
plt.plot(x,y)

ani.save('ani.gif')