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
#rectangle(-5, 5, 10000, -math.pi/2, 3*math.pi/2)
#rectangle2(-5, 5, 10000, -math.pi/2, 3*math.pi/2)

#plt.grid(True)
#plt.show()


# Fonction exponentielle
def plot_exponential(a,b,x):
    # Créer une gamme de valeurs x
    x = np.linspace(x, 10, 400)
    
    # Calculer l'exponentielle de chaque point
    y = a * np.exp(x * b)
    
    # Tracer la courbe
    plt.plot(x, y, label="y = e^x")
    
    # Ajouter des labels et légendes
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Courbe de la fonction exponentielle')
    plt.legend()
    plt.grid(True)
    plt.show()
    with open('valeurs_a_et_b.txt', 'w') as file:
        file.write(f'Valeur de a : {a}\n')
        file.write(f'Valeur de b : {b}\n')

a=-0.5
b=0.7
x=2
# Exemple d'utilisation
plot_exponential(a,b,x)
