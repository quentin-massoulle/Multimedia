import cv2  # Importation de la bibliothèque OpenCV pour le traitement d'image
import numpy as np  # Importation de NumPy pour la manipulation de tableaux
from PIL import Image  # Importation de PIL pour l'affichage et la sauvegarde des images

def Mosaique_Image(image1_path, image2_path, output_path):
    """
    Aligne et fusionne deux images en utilisant des techniques de traitement d'image
    telles que la détection de points clés et l'homographie.

    :param image1_path: Chemin vers la première image
    :param image2_path: Chemin vers la deuxième image
    :param output_path: Chemin pour sauvegarder l'image fusionnée
    """

    # Lire les images à partir des chemins fournis
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convertir les images en niveaux de gris pour faciliter la détection des caractéristiques
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Détection des points clés et des descripteurs avec l'algorithme ORB
    # ORB est rapide et efficace pour des applications en temps réel
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Correspondance des descripteurs à l'aide du matcher de BruteForce
    # NORM_HAMMING est utilisé pour les descripteurs binaires d'ORB
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    # Trier les correspondances par distance croissante (meilleures premières)
    matches = sorted(matches, key=lambda x: x.distance)

    # Extraire les points des correspondances en utilisant les index des correspondances
    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Calculer la matrice d'homographie pour aligner l'image1 avec l'image2
    # RANSAC est utilisé pour estimer la matrice en éliminant les correspondances aberrantes
    matrix, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    # Obtenir les dimensions des deux images (hauteur et largeur)
    h1, w1 = image1.shape[:2]
    h2, w2 = image2.shape[:2]

    # Déterminer les coins des images après transformation
    # Cela permet de savoir où l'image transformée sera placée dans l'espace de l'image fusionnée
    corners1 = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    transformed_corners1 = cv2.perspectiveTransform(corners1, matrix)

    # Déterminer les coins de l'image 2 pour le redimensionnement de l'image fusionnée
    corners2 = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    all_corners = np.concatenate((transformed_corners1, corners2), axis=0)

    # Trouver les points extrêmes (min et max) des coins transformés
    # Ceci définit la taille de l'image fusionnée
    [x_min, y_min] = np.int32(all_corners.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(all_corners.max(axis=0).ravel() + 0.5)

    # Calculer la distance de translation nécessaire pour ajuster l'image dans le cadre
    translation_dist = [-x_min, -y_min]
    translation_matrix = np.array([[1, 0, translation_dist[0]], [0, 1, translation_dist[1]], [0, 0, 1]])

    # Appliquer la transformation d'homographie à l'image 1
    # La matrice de translation est combinée avec la matrice d'homographie
    output_size = (x_max - x_min, y_max - y_min)
    aligned_image1 = cv2.warpPerspective(image1, translation_matrix @ matrix, output_size)

    # Créer une image vide de la même taille que l'image alignée pour y placer image2
    aligned_image2 = np.zeros_like(aligned_image1)
    # Positionner image2 dans l'image vide, en tenant compte de la translation
    aligned_image2[translation_dist[1]:translation_dist[1] + h2, translation_dist[0]:translation_dist[0] + w2] = image2

    # Fusionner les deux images en utilisant np.maximum
    # Cela permet de garder le pixel ayant la valeur maximale à chaque position
    fused_image = np.maximum(aligned_image1, aligned_image2)

    # Sauvegarder l'image fusionnée 
    cv2.imwrite(output_path, fused_image)
    # Ouvrir et afficher l'image 
    fused_pil_image = Image.open(output_path)
    fused_pil_image.show()


Mosaique_Image("I1.jpg", "I2.jpg", "merged_mosaic.jpg")
