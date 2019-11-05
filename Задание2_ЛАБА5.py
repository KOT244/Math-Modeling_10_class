import matplotlib.pyplot as plt
import numpy as np
def graphicscnd(x=np.arange(1,2,0.1),X=np.arange(1,11,1),X1=np.arange(-11,11,1)):
    " " " Функция рисует параболу и гиперболу в одной координатной плоскости " " "
    y = x**2
    Y = 1/X
    Y1 = 1/X1
    plt.plot (x,y,label='my graphics',color='k')
    plt.plot (X,Y,label='my graphics',color='r')
    plt.plot (X1,Y1,label='my graphics',color='r')
    plt.show()
c=graphicscnd()
print(c)