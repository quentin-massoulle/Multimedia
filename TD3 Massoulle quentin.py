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
            x_values.append(float(x))  # Ajouter la valeur de x à la liste
            y_values.append(float(y))  # Ajouter la valeur de y à la liste
    return np.array(x_values), np.array(y_values)  # Retourner les listes sous forme de tableaux NumPy

# Lire les valeurs à partir du fichier 'math.txt'
fichier = 'points_x_y.txt'  # Nom du fichier contenant les données
x_values, y_values = lire_valeurs_du_fichier(fichier)  # Appel de la fonction pour lire les données du fichier


def regretion(x_values,y_values):
    # Transformation logarithmique de y
    log_y_values = np.log(y_values)  # Appliquer le logarithme naturel aux valeurs de y (linéariser la relation exponentielle)

    # Régression linéaire pour estimer ln(a) et b
    A = np.vstack([x_values, np.ones(len(x_values))]).T  # Créer la matrice A avec les valeurs de x et une colonne de 1
    # Effectuer la régression linéaire (méthode des moindres carrés) pour trouver la pente (b) et l'ordonnée à l'origine (ln(a))
    slope, intercept = np.linalg.lstsq(A, log_y_values, rcond=None)[0]  

    # Calcul des paramètres estimés
    b_estimated = slope  # La pente de la régression linéaire est le paramètre b
    ln_a_estimated = intercept  # L'ordonnée à l'origine est ln(a)
    a_estimated = np.exp(ln_a_estimated)  # Calculer a en prenant l'exponentielle de ln(a)

    # Affichage des résultats
    print(f"Valeur estimée de a par regretion linaiaire : {a_estimated}")  # Afficher la valeur estimée de a
    print(f"Valeur estimée de b par regretion linaiaire : {b_estimated}")  # Afficher la valeur estimée de b




def matriceille(x_values, y_values):
    logY = np.log(y_values)  # Prendre le logarithme naturel des y_values

    # Créer la matrice A avec les premières et dernières valeurs de x_values
    matriceA = [[1, x_values[0]], [1, x_values[-1]]]
    # Créer la matrice B avec le logarithme des premières et dernières valeurs de y_values
    matriceB = [logY[0], logY[-1]]

    # Calculer l'inverse de la matrice A
    inverseA = np.linalg.inv(matriceA)

    # Résoudre le système d'équations en multipliant inverseA par matriceB
    resultat = np.dot(inverseA, matriceB)

    # Calculer les valeurs de a et b estimées
    a_estimated, b_estimated = np.exp(resultat[0]), resultat[1]

    # Afficher les résultats
    print(f"Valeur estimée de a par régression matricielle : {a_estimated}")
    print(f"Valeur estimée de b par régression matricielle : {b_estimated}")

def matriceMultiCouple(x_values,y_values):
    logY = np.log(y_values)  # Prendre le logarithme naturel des y_values

    # Créer la matrice A avec une colonne de 1 et une colonne avec les valeurs de x_values
    matriceA = np.vstack([np.ones(len(x_values)), x_values]).T
    
    # Créer la matrice B avec le logarithme des y_values
    matriceB = logY

    # Résoudre le système d'équations avec la méthode des moindres carrés
    resultat, _, _, _ = np.linalg.lstsq(matriceA, matriceB, rcond=None)

    # Calculer les valeurs de a et b estimées
    a_estimated, b_estimated = np.exp(resultat[0]), resultat[1]

    # Afficher les résultats
    print(f"Valeur estimée de a par régression matricielle Multi Couple : {a_estimated}")
    print(f"Valeur estimée de b par régression matricielle Multi Couple : {b_estimated}")


def perturber_y(y_values):
    """Ajoute du bruit aléatoire à y_values avec une amplitude aléatoire entre 0 et 1."""
    # perturbation ave n nombre entre 0 et 1
    perturbation = np.random.random()
    
    decalage = perturbation * np.random.randn(len(y_values))
    
    yb_values = y_values + decalage
    return yb_values


def superposer_courbes(x_values, y_values, yb_values):
    """Superpose les courbes de y et yb"""
    plt.plot(x_values, y_values, label='Courbe y (originale)', color='blue')
    plt.plot(x_values, yb_values, label='Courbe yb (perturbée)', color='red', linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y / yb')
    plt.title('Superposition des courbes y et yb')
    plt.legend()
    plt.show()

def calculer_a_b(x_values, y_values):
    """Calcule les paramètres a et b en utilisant la méthode des moindres carrés"""
    logY = np.log(y_values)
    matriceA = np.vstack([np.ones(len(x_values)), x_values]).T
    resultat, _, _, _ = np.linalg.lstsq(matriceA, logY, rcond=None)
    a_estimated, b_estimated = np.exp(resultat[0]), resultat[1]
    return a_estimated, b_estimated
matriceMultiCouple(x_values,y_values)
matriceille(x_values, y_values)
regretion(x_values,y_values)


# 1. Perturber les valeurs de y (Question 3)
yb_values = perturber_y(y_values)

# 2. Superposer les courbes de y et yb (Question 4)
superposer_courbes(x_values, y_values, yb_values)

# 3. Calculer a et b avec les couples (x_i, yb_i) (Question 5)
a_estimated_yb, b_estimated_yb = calculer_a_b(x_values, yb_values)

# Afficher les résultats pour yb
print(f"Valeur estimée de a avec yb (perturbé) : {a_estimated_yb}")
print(f"Valeur estimée de b avec yb (perturbé) : {b_estimated_yb}")

# 4. Calculer a et b avec les données originales (Question 6)
a_estimated_y, b_estimated_y = calculer_a_b(x_values, y_values)

# Afficher les résultats pour les données originales
print(f"Valeur estimée de a avec y (original) : {a_estimated_y}")
print(f"Valeur estimée de b avec y (original) : {b_estimated_y}")

# Comparaison et interprétation des résultats
print("\n--- Comparaison des paramètres estimés ---")
print(f"Différence de a : {a_estimated_yb - a_estimated_y}")
print(f"Différence de b : {b_estimated_yb - b_estimated_y}")




# Exemples de valeurs x et y perturbées
x1_values = x_values[:10] # Valeurs de x
yb1_values = perturber_y(y_values[:10])  # Valeurs y perturbées

# Calcul de p et q à partir des couples (x, yb)
p_estime, q_estime = calculer_a_b(x1_values, yb_values)

print(f"p estimé : {p_estime}, q estimé : {q_estime}")
p_estime, q_estime = calculer_a_b(x_values, yb_values)

print(f"p estimé : {p_estime}, q estimé : {q_estime}")


