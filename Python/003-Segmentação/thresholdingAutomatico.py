import cv2
import numpy as np

# Leitura da imagem
image = cv2.imread('../../imagens/CapaLivro.jpg', 0)

# É uma boa prática borrar a imagem e remover alguns ruídos
# Aplicando a técnica do Filtro Gaussiano
image = cv2.GaussianBlur(image, (3, 3), 0)

# Utilização adaptiveThreshold
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 3, 5)
cv2.imshow("Adaptive Mean Thresholding", thresh)
cv2.waitKey(0)

# Utilização Otsu's thresholding
_, th2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu's Thresholding", thresh)
cv2.waitKey(0)

# Otsu's thresholding depois de outra aplicação do Filtro Gaussiano
blur = cv2.GaussianBlur(image, (5,5), 0)
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Guassian Otsu's Thresholding", thresh)
cv2.waitKey(0)

cv2.destroyAllWindows()