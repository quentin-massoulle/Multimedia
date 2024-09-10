import numpy as np
import matplotlib.pyplot as plt

# Fonction pour résoudre une équation du second degré
def solve_quadratic(a, b, c):
    # Calcul du discriminant
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Deux solutions réelles
        x1 = (-b - np.sqrt(delta)) / (2*a)
        x2 = (-b + np.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        # Une solution double
        x1 = x2 = -b / (2*a)
        return x1, x2
    else:
        # Pas de solution réelle
        return None, None

# Fonction pour tracer l'équation du second degré et afficher les solutions
def plot_quadratic(a, b, c):
    # Résoudre l'équation
    x1, x2 = solve_quadratic(a, b, c)

    # Créer une gamme de valeurs x pour tracer la courbe
    x_vals = np.linspace(-5, 5, 400)
    y_vals = a * x_vals**2 + b * x_vals + c

    # Tracer la courbe
    plt.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x + {c}')
    
    # Afficher les solutions, si elles existent
    if x1 is not None and x2 is not None:
        plt.scatter([x1, x2], [0, 0], color='red', zorder=5)  # Mettre en évidence les solutions
        plt.text(x1, 0, f'  x1 = {x1:.2f}', fontsize=12, verticalalignment='bottom')
        plt.text(x2, 0, f'  x2 = {x2:.2f}', fontsize=12, verticalalignment='bottom')
    
    # Ajouter des labels et légendes
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Courbe de l\'équation du second degré')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemple d'utilisation
a = 1
b = -3
c = 2
plot_quadratic(a, b, c)
