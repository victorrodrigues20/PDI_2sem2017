import cv2

# Lê imagem
image = cv2.imread('../../imagens/urso.jpg')

# Exibe informações da imagem (comprimento, altura, quantidade de canais)
print(image.shape)

# Armazena cada canal da imagem RGB em 3 variáveis (R, G e B)
B, G, R = cv2.split(image)

# Exibe cada canal separadamente
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

cv2.destroyAllWindows()