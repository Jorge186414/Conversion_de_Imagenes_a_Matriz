from PIL import Image
import numpy as np

imagen = Image.open('one-piece-luffy-ocean-explorer-desktop-wallpaper-preview.jpg')

imagen_blanco_negro = imagen.convert('L')

matriz_blanco_negro = np.array(imagen_blanco_negro)

print(matriz_blanco_negro)