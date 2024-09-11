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
fichier = 'math.txt'  # Nom du fichier contenant les données
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


def matriceille(x1, x2, y1, y2) :
    b = (np.log(y1) - np.log(y2)) / (x1 - x2)
    log_a = np.log(y1) - b * x1
    a = np.exp(log_a)
    print(f"Valeur estimée de a par regretion matriceille : {a}")  # Afficher la valeur estimée de a
    print(f"Valeur estimée de b par regretion matriceille : {b}")  # Afficher la valeur estimée de b

matriceille(x_values[0], x_values[1], y_values[0], y_values[1])
regretion(x_values,y_values)