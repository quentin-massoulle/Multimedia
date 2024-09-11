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
def matriceille(y_values,X_values):
        
    # Transformation logarithmique de y_values
    Y = np.log(y_values)
    # -> Nous prenons le logarithme naturel des valeurs de y pour transformer
    # l'équation exponentielle y = a * exp(b * x) en une équation linéaire :
    # ln(y) = ln(a) + b * x
    # Cela nous permet d'utiliser une régression linéaire pour estimer les paramètres a et b.

    # Étape 2 : Construction de la matrice X
    # Ajouter une colonne de 1 pour l'ordonnée à l'origine (biais)
    X = np.column_stack((x_values, np.ones(len(x_values))))
    # -> Ici, on crée une matrice X avec deux colonnes : la première est constituée des valeurs de x,
    # et la deuxième est une colonne de 1 qui permet de représenter l'ordonnée à l'origine ln(a).
    # Cela modélise l'équation linéaire : Y = b * x + ln(a)

    # Étape 3 : Calcul des coefficients de régression
    # Calcul de beta = (X^T X)^{-1} X^T Y
    XtX = np.dot(X.T, X)
    XtY = np.dot(X.T, Y)
    beta = np.linalg.inv(XtX).dot(XtY)
    # -> XtX est le produit matriciel de la transposée de X avec X.
    # -> XtY est le produit matriciel de la transposée de X avec Y.
    # -> Nous utilisons l'inverse de XtX et le produit avec XtY pour résoudre l'équation linéaire et trouver les coefficients de régression.
    # beta contient les coefficients estimés : [b, ln(a)].

    # Extraction des coefficients
    b_estimated = beta[0]  # Pente (b)
    ln_a_estimated = beta[1]  # Ordonnée à l'origine (ln(a))
    a_estimated = np.exp(ln_a_estimated)  # Calcul de a en exponentiant ln(a)
    # -> Nous récupérons la pente (b) et l'ordonnée à l'origine (ln(a)) à partir du vecteur beta.
    # -> a est calculé en prenant l'exponentielle de ln(a).

    # Affichage des résultats
    print(f"Valeur estimée de a par matricielle  : {a_estimated}")
    print(f"Valeur estimée de b par matricielle: {b_estimated}")
    # Génération des points pour la courbe ajustée
matriceille(y_values,x_values)
regretion(x_values,y_values)