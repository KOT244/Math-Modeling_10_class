import matplotlib.pyplot as plt
import numpy as np
def graphicscnd(a=4,b=3):
    x=np.arange(-1,1,0.1)
    X=np.arange(-4,10,0.1)
    y=np.arange(-1,1,0.1)
    Y=np.arange(-4,10,0.1)
    x,y = np.meshgrid(x,y)
    fxy = x**2+y**2
    X,Y=np.meshgrid(X,Y)
    FXY = X**2/a+Y**2/b
    plt.contour(x,y,fxy,levels=[0.25])
    plt.contour(X,Y,FXY,levels=[1])
    plt.show()
c=graphicscnd()
print(c)
