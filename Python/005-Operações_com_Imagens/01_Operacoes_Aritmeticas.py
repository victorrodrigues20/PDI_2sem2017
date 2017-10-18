import cv2
import numpy as np

image = cv2.imread('../../imagens/elefante.jpg')

cv2.imshow("Input", image)

M = np.ones(image.shape, dtype = "uint8") * 3

cv2.imshow("Ones", M)

cv2.waitKey(0)
cv2.destroyAllWindows()

added = cv2.add(image, M)
cv2.imshow("Adicao", added)

subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracao", subtracted)

multipl = cv2.multiply(image, M)
cv2.imshow("Multiplicacao", multipl)

divisao = cv2.divide(image, M)
cv2.imshow("Divisao", divisao)

cv2.waitKey(0)
cv2.destroyAllWindows()