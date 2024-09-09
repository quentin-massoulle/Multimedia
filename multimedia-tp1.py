import numpy as np
import matplotlib.pyplot as plt
#exo 1
# Définir l'intervalle de x
#x = np.linspace(-4, 4)

# Calculer les valeurs de y = sin(x)
#y = np.sin(x)

# Tracer la fonction
#plt.figure(figsize=(8, 6))
#plt.plot(x, y, label='y = sin(x)', color='blue')

#exo 2 
# Paramètres de la fonction
A = 5     # Amplitude
f =50   # Fréquence
phi = 0    # Phase (en radians)

# Définir l'intervalle de x
x = np.linspace(0,5,100000)

# Calculer les valeurs de y = A * sin(2 * Pi * f * x + phi)
y = A * np.sin(2 * np.pi * f * x + phi)

# Tracer la fonction
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$y = A \cdot \sin(2\pi f x + \phi)$', color='b')
# Ajouter des étiquettes et un titre
plt.title('Tracé de la fonction y(x) = sin(x)') 
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='red', linewidth=1)
plt.axvline(0, color='green', linewidth=1)
plt.grid(True)
plt.legend()

# Afficher le graphique
plt.show()
