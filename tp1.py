import math
import matplotlib.pyplot as plt

def solution(a,b,c):
    delta= b**2 -(4*a*c)
    if (delta<0):
        return "aucune solution"
    else:
        if (a!=0):
            x1= (-b-math.sqrt(delta))/(2*a)
            x2= (-b+math.sqrt(delta))/(2*a)
            plt.plot(x1,x2)
            plt.show()
            return x1,x2

print (solution(1,10,3))