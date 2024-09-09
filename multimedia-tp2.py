import numpy as np
import math
import matplotlib.pyplot as plt

# Fonction pour afficher sin(x)/x
def afichage(n, a, b):
    d = np.linspace(a, b, n)  # 'n' est le nombre de points
    y = np.sin(d) / d
    plt.plot(d, y)

# Fonction pour afficher le signal rectangulaire
def rectangle(val1, val2, echantillon, mPi, pPi):
    x = np.linspace(val1, val2, echantillon)
    y = np.where((x >= mPi) & (x <= pPi), 1, 0)
    plt.plot(x, y)

def rectangle2(val1, val2, echantillon, mPi, pPi):
    x = np.linspace(val1, val2, echantillon)
    y = np.where((x >= mPi) & (x <= pPi), np.sin(pPi*x), 0)
    plt.plot(x, y)


# Affichage d'un signal rectangulaire entre -pi/2 et 3*pi/2
rectangle(-20, 20, 10000, -math.pi/2, 3*math.pi/2)
rectangle2(-20, 20, 10000, -math.pi/2, 3*math.pi/2)

plt.grid(True)
plt.show()
