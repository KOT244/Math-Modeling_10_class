import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
R = 1
def circle_func(x_centre_point,
                y_centre_point,
                R,
                N):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(0,N,1):
        alpha = np.linspace(0,2*np.pi,N)
        x[i] = x_centre_point + R*np.cos(alpha[i])
        y[i] = y_centre_point + R*np.sin(alpha[i])
    return x,y

x_centre_move = np.linspace(-5,5,100)
y_centre_move = np.zeros(100)
for i in range(0,N,1):
    y_centre_move = x_centre_move**2 + x_centre_move
anim_list = []
N = 100
for i in range(0,N,1):
    x,y = circle_func(x_centre_move[i],
                      y_centre_move[i],
                      R=R,
                      N=N)
    circle, = plt.plot(x,y,'g-',lw = 2)
    anim_list.append([circle])

ani = ArtistAnimation(fig, anim_list, interval = 50)
plt.axes().set_aspect( 'equal')
ani.save('ani.gif')
    
