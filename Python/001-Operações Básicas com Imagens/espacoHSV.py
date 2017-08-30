import cv2
import numpy as np

# Lê imagem
image = cv2.imread('../../imagens/urso.jpg')

# Converte imagem lida de RGB pra HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Exibe informações da imagem (comprimento, altura, quantidade de canais)
print(hsv_image.shape)

# Exibe imagem HSV
cv2.imshow('HSV image', hsv_image)
# Exibe apenas canal H
cv2.imshow('Hue channel', hsv_image[:, :, 0])
# Exibe apenas canal S
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
# Exibe apenas canal V
cv2.imshow('Value channel', hsv_image[:, :, 2])

cv2.waitKey()
cv2.destroyAllWindows()

