# Exercício: Combinar duas imagens diferentes existentes na pasta de imagens

import cv2
import numpy as np

imageA = cv2.imread('../../imagens/gato.jpg')
imageB = cv2.imread('../../imagens/tigre.jpg')

# Deixar o tamanho da imagem B igual ao da A
height, width, _ = imageA.shape
imageB_resize = cv2.resize(imageB, (width, height), interpolation = cv2.INTER_AREA)

print(imageA.shape)
print(imageB_resize.shape)

# Mostrar imagens A e B após o ajuste
cv2.imshow("Input A", imageA)
cv2.imshow("Input B", imageB_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()