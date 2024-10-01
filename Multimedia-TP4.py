import cv2
import numpy as np

# Lire l'image 'objet.jpg'
image = cv2.imread('objet.jpg')

# Vérifier si l'image a été chargée
if image is None:
    print("Erreur : Impossible de charger l'image.")
else:
    # Convertir l'image en niveaux de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dimensions de l'image
    height, width = gray_image.shape

    # Créer une copie de l'image originale pour la modification
    modified_image = image.copy()

    #threshold_sombre = 30
    threshold_sombre = np.mean(gray_image)# calcule la moyenne de liminositer sur la totaliter de tt les pixel 
    print(threshold_sombre)

    non_blue_pixel_count = 0

    for i in range(height):
        for j in range(width):
            if gray_image[i, j] < threshold_sombre:
                modified_image[i, j] = [255, 0, 0]  
            else :
                  modified_image[i, j] = [0,0, 255] 
                  non_blue_pixel_count += 1

              

    print(f"Nombre de pixels non bleus : {non_blue_pixel_count}")

    # Afficher l'image modifiée
    cv2.imshow('Image Modifiée', modified_image)

    # Attendre que l'utilisateur appuie sur une touche pour fermer les fenêtres
    cv2.waitKey(0)
    cv2.destroyAllWindows()
