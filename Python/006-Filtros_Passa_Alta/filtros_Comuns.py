import cv2
import numpy as np

image = cv2.imread('../../imagens/elefante.jpg')

cv2.imshow('Original', image)
#cv2.waitKey(0)

mascara = [[-1, -1, -1],
           [-1,  8, -1],
           [-1, -1, -1]]

# Nós usamos o cv2.fitler2D para realizar a convolução da
# máscara com a imagem
imgFiltrada = cv2.filter2D(image, -1, np.asarray(mascara))
cv2.imshow('Filtro passa-alta', imgFiltrada)
cv2.waitKey(0)

cv2.destroyAllWindows()