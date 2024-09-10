import numpy as np
import matplotlib.pyplot as plt

# Fonction pour lire les valeurs de x et y à partir d'un fichier
def lire_valeurs_du_fichier(fichier):
    x_values = []
    y_values = []
    with open(fichier, 'r') as file:
        for line in file:
            # Séparer les valeurs x et y par la virgule
            x, y = line.strip().split(',')
            x_values.append(float(x))
            y_values.append(float(y))
    return np.array(x_values), np.array(y_values)

# Lire les valeurs à partir du fichier 'valeurs_xy.txt'
fichier = 'math.txt'
x_values, y_values = lire_valeurs_du_fichier(fichier)

# Transformation logarithmique de y
log_y_values = np.log(y_values)

# Régression linéaire pour estimer ln(a) et b
A = np.vstack([x_values, np.ones(len(x_values))]).T
slope, intercept = np.linalg.lstsq(A, log_y_values, rcond=None)[0]

# Calcul des paramètres estimés
b_estimated = slope  # La pente donne b
ln_a_estimated = intercept  # L'ordonnée à l'origine donne ln(a)
a_estimated = np.exp(ln_a_estimated)  # a = e^(ln(a))

# Affichage des résultats
print(f"Valeur estimée de a : {a_estimated}")
print(f"Valeur estimée de b : {b_estimated}")

# Générer des points pour la courbe ajustée
x_fit = np.linspace(min(x_values), max(x_values), 100)
y_fit = a_estimated * np.exp(b_estimated * x_fit)

# Tracer les données originales et la courbe ajustée
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='blue', label='Données originales')
plt.plot(x_fit, y_fit, color='red', label=f'Ajustement exponentiel: y = {a_estimated:.2f} * e^({b_estimated:.2f} * x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajustement exponentiel des points à partir du fichier')
plt.legend()
plt.grid(True)
plt.show()
