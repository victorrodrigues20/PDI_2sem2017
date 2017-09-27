import sys
import cv2
import time
import numpy as np

# Caminho da imagem
pathImagem = '../../imagens/rodovia.jpg'

# Carregar Imagem (direto do frame do vídeo)
cap = cv2.VideoCapture('../../imagens/cars.avi')

while cap.isOpened():
    ret, frame = cap.read()
    break

# Informações da imagem
print(frame.shape)

# Cor
azul = (0, 0, 255)

# Linha diagonal :
# cv2.line(canvas, (0, 0), (400, 300), azul)

# Linha Imaginária
cv2.line(frame, (0, 75), (320, 75), azul, 2)

posX1 = 208
posY1 = 70
posX2 = 285
posY2 = 147

# Retangulo imaginario
cv2.rectangle(frame, (posX1, posY1), (posX2, posY2), (0, 255, 255), 2)

if ( posY1 <= 75 and posY2 >= 75 ):
    print("Passei pela linha")

cv2.imshow("Imagem ", frame)
cv2.waitKey(0)