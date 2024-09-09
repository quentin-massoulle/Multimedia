import numpy as np
import math
import matplotlib.pyplot as plt
def afichage(x):
    d=np.linspace(-1000,1000,x)
    y = np.sin(d)/d
    plt.plot(d, y)

tab=[20,50,200,400,2000]

#for i in tab :
    #afichage(i)
#plt.grid(True)
#plt.show()


#exo 2 

def rectangle(a,b,c):
      x=np.linspace(a,b,c)
      y=np.where((x<= math.pi)&(x>= -math.pi),1,0)
      plt.plot(x,y)

rectangle(-5,5,10000)
plt.grid(True)
plt.show()