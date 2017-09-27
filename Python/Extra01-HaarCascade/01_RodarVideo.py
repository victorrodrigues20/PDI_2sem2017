import sys
import cv2
import time
import numpy as np

# Inicializar o vídeo
cap = cv2.VideoCapture('../../imagens/cars.avi')

# Loop para o vídeo carregado
while cap.isOpened():

    # Velocidade da exibição do vídeo
    time.sleep(.05)

    # Ler o frame atual
    ret, frame = cap.read()

    # Mostrar frame
    cv2.imshow('Carros', frame)

    # Se for digitado ESC ou ENTER, finaliza a exibição do vídeo
    k = cv2.waitKey(1)
    if k == 27 or k == 13:
        break

cap.release()
cv2.destroyAllWindows()