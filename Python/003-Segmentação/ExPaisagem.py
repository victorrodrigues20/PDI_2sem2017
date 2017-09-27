import cv2
import numpy as np

# Lendo imagem
image = cv2.imread('../../imagens/paisagem1.jpg')

# Mostrar imagem original
cv2.imshow('Original', image)

#Converte para HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Limites da mascara
lower_blue = np.array([84,0,0])
upper_blue = np.array([135,255,255])

#Cria mascara
mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

#Aplica mascara na imagem original
res = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Imagem', res)

cv2.waitKey(0)