import cv2
import numpy as np

image = cv2.imread('../../imagens/elefante.jpg')

cv2.imshow('Original', image)
cv2.waitKey(0)

mascara_3x3 = np.ones((3, 3), np.float32) / 9

#print(mascara_3x3)

# Nós usamos o cv2.fitler2D para realizar a convolução da
# máscara com a imagem
blurred = cv2.filter2D(image, -1, mascara_3x3)
cv2.imshow('3x3 Blurring', blurred)
cv2.waitKey(0)

# Creating our 7 x 7 kernel
mascara_7x7 = np.ones((7, 7), np.float32) / 49

#print(mascara_7x7)

blurred2 = cv2.filter2D(image, -1, mascara_7x7)
cv2.imshow('7x7 Kernel Blurring', blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()