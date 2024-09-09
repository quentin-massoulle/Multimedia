import numpy as np
import matplotlib.pyplot as plt
def afichage(x):
    d=np.linspace(-1000,1000,x)
    y = np.sin(d)/d
    plt.plot(d, y)

tab=[20,50,200,400,2000]

for i in tab :
    afichage(i)
plt.grid(True)
plt.show()