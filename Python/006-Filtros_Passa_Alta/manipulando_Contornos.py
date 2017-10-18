import cv2
import numpy as np

image = cv2.imread('../../imagens/shapes.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

bordas = cv2.Canny(gray, 30, 200)
#cv2.imshow('Canny Edges', bordas)
#cv2.waitKey(0)

# Finding Contours
_, contornos, hierarquia = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print("Figuras Encontradas = " + str(len(contornos)))

# Desenhar todos os contornos
# Usar '-1' no 3o. parametro para desenhar todos
cv2.drawContours(image, contornos, -1, (0,255,0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()