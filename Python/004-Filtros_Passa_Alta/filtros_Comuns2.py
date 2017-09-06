import cv2
import numpy as np

image = cv2.imread('../../imagens/elefante.jpg')

# Filtro de Média
blur = cv2.blur(image, (3,3))
cv2.imshow('Média', blur)
cv2.waitKey(0)

# Filtro Gaussiano
Gaussian = cv2.GaussianBlur(image, (7,7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

# Filtro Mediano
median = cv2.medianBlur(image, 5)
cv2.imshow('Filtro Mediano', median)
cv2.waitKey(0)

# Filtro Bilateral
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Filtro Bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()