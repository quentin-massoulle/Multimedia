import numpy as np
import matplotlib.pyplot as plt

# Valeurs données de y pour x allant de 1 à 10
y_values = [
    60.912469803517354,
    742.0657955128829,
    9040.212072280312,
    110132.32897403352,
    1341686.4326043716,
    16345086.862360539,
    199123921.98788095,
    2425825977.048949,
    29552610315.11642,
    360024496686.92883
]

# Correspondance des valeurs x (1 à 10)
x_values = np.arange(1, 11)

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

# Tracer les données et la courbe ajustée
x_fit = np.linspace(1, 10, 100)
y_fit = a_estimated * np.exp(b_estimated * x_fit)

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='blue', label='Données originales')
plt.plot(x_fit, y_fit, color='red', label=f'Ajustement exponentiel: y = {a_estimated:.2f} * e^({b_estimated:.2f} * x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajustement exponentiel des 10 points')
plt.legend()
plt.grid(True)
plt.show()
