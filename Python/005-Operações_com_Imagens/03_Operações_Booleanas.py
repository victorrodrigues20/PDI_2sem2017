import cv2
import numpy as np

# Criando Imagem com um Quadrado
quadrado = np.zeros((300, 300), np.uint8)
cv2.rectangle(quadrado, (50, 50), (250, 250), 255, -2)
cv2.imshow("Quadrado", quadrado)

# Criando Imagem com uma Elipse
elipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(elipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Elipse", elipse)


cv2.waitKey(0)
#cv2.destroyAllWindows()


# Operação AND
And = cv2.bitwise_and(quadrado, elipse)
cv2.imshow("AND", And)

# Operação OR 
bitwiseOr = cv2.bitwise_or(quadrado, elipse)
cv2.imshow("OR", bitwiseOr)

# Operação XOR
bitwiseXor = cv2.bitwise_xor(quadrado, elipse)
cv2.imshow("XOR", bitwiseXor)

# Operação Not
bitwiseNot_sq = cv2.bitwise_not(quadrado)
cv2.imshow("NOT Quadrado", bitwiseNot_sq)


cv2.waitKey(0)
cv2.destroyAllWindows()