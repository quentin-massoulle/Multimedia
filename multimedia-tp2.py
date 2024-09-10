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
def plot_exponential(a, b, start_x):
    # Créer une gamme de valeurs x de start_x à 10
    x = np.linspace(start_x, 10, 400)
    
    # Calculer l'exponentielle de chaque point
    y = a * np.exp(x * b)
    
    # Tracer la courbe
    plt.plot(x, y, label=f'y = {a} * e^({b} * x)')
    
    # Ajouter des labels et légendes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Courbe de la fonction exponentielle')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Enregistrer les valeurs x et y dans un fichier texte
    with open('points_x_y.txt', 'w') as file:
        file.write('x, y\n')  # En-tête
        # Sélectionner les 10 premiers points
        for X, Y in zip(x[:10], y[:10]):
            file.write(f'{X:.2f}, {Y:.2f}\n')  # Formatage avec 2 décimales

a = 10
b = 7
start_x = 2

# Exemple d'utilisation
plot_exponential(a, b, start_x)
