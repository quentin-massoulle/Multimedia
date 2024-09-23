import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


# Amplitude
A = 1
# Fréquence  
f = 1
# Déphasage   
phi = 0

B = 0.2

x = np.linspace(0, 100000, 500000)

y = A * np.exp(-B * x)
y2 = np.sin(2 * np.pi * f * x + phi)
y3 = A * np.exp(-B * x) * np.sin(2 * np.pi * f * x + phi)

# Paramètres pour générer le son
sample_rate = 44100  # Taux d'échantillonnage (samples per second)
duration = 5  # Durée du son en secondes

# Générer un tableau de temps
t = np.linspace(0, duration, 500000)

A = 1
f = 400

# Générer le signal sinusoïdal amorti pour le son
y_sound = A * np.exp(-B * t) * np.sin(2 * np.pi * f * t + phi)

# Jouer le son généré
sd.play(y_sound, samplerate=sample_rate)


plt.plot(x, y, label=f'y(x) = A.exp(-Bx)', color="green")
plt.plot(x, y2, label=f'y(x) = sin(2pi*f*x+phi)', color="red")
plt.plot(x, y3, label=f'y(x) = A.exp(-Bx) * sin(2pi*f*x+phi)', color="blue")
plt.axhline(0, color='red', linewidth=0.5)  
plt.axvline(0, color='green', linewidth=0.5)  
plt.grid(True, linestyle='--', alpha=0.6)

plt.title('Graphique sinus amorti')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()