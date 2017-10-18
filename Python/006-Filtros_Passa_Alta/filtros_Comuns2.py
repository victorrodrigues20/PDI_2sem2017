import cv2
import numpy as np

image = cv2.imread('../../imagens/elefante.jpg')

# Filtro Sobel - Aplicação em X
sobelX = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)  # x
cv2.imshow('Sobel - X', sobelX)
cv2.waitKey(0)

# Filtro Sobel - Aplicação em Y
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)  # y
cv2.imshow('Sobel - Y', sobelY)
cv2.waitKey(0)

# Filtro Mediano
laplacian = cv2.Laplacian(image,cv2.CV_64F)  # y
cv2.imshow('Filtro Laplaciano', laplacian)
cv2.waitKey(0)

# Filtro Canny
canny = cv2.Canny(image,30, 200)
cv2.imshow('Filtro Canny', canny)
cv2.waitKey(0)

# Filtro Canny Imagem Escala Cinza
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cannyCinza = cv2.Canny(gray,30, 200)
cv2.imshow('Filtro Canny - Escala Cinza', cannyCinza)
cv2.waitKey(0)
