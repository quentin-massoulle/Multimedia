from PIL import Image
import numpy as np

def fusionImage(I1_path, I2_path, x1, y1, x2, y2, alpha=0.5):
    # Ouvrir les deux images
    I1 = Image.open(I1_path)
    I2 = Image.open(I2_path)
    
    
    
    # Créer une image vide de dimensions doublées en largeur et en hauteur (comparé à I1 et I2)
    largeur, hauteur = I1.size
    I12 = Image.new(I1.mode, (2 * largeur, 2 * hauteur))
    
    # Calculer les positions pour centrer I1 et I2 dans I12 avec de l'espace vide autour
    x_offset = (I12.width - I1.width) // 2
    y_offset = (I12.height - I1.height) // 2
    
    # Placer I1 dans la nouvelle image (I12) au centre
    I12.paste(I1, (x_offset, y_offset))
    
    # Placer I2 dans la nouvelle image (I12) avec translation relative
    I12.paste(I2, (x_offset + (x1 - x2), y_offset + (y1 - y2)), mask=Image.new('L', I2.size, int(255 * alpha)))
    
    return I12

# Exemple d'utilisation
I1_path = "I2.jpg"
I2_path = "I1.jpg"
x1, y1 = 79, 174   # cordonner X du pixel du point haut gauche de la feuille sur l'image 
x2, y2 = 75, 57    # cordonner Y du pixel du point haut gauche de la feuille sur l'image 


#translation en fonction d'un element pris manuelement exemple un coint de l'image


i12=fusionImage(I1_path,I2_path,x1,y1,x2,y2)

i12.show()




# Créer et afficher l'image résultante avec superposition et espace vide




