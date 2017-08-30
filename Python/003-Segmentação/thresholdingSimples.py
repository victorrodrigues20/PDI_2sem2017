import cv2
import numpy as np

# Lendo imagem
image = cv2.imread('../../imagens/CapaLivro.jpg', 0)

# Mostrar imagem original
cv2.imshow('Original', image)
cv2.waitKey(0)

# Aplicação do Threshold
# Os valor abaixo de 127 tornam-se 0 (preto)
# Os valor acima de 127 tornam-se 255 (branco)
ret,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.waitKey(0)