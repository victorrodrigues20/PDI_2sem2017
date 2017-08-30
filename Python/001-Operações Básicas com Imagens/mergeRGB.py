import cv2

# Lê imagem
image = cv2.imread('../../imagens/urso.jpg')

# Armazena cada canal da imagem RGB em 3 variáveis (R, G e B)
B, G, R = cv2.split(image)

# Junta todos os canais em 1 imagem só: (R, G e B) para (RGB)
merged = cv2.merge([B, G, R])

# Exibe a imagem (título da janela, imagem)
cv2.imshow("Merge", merged)

# Adiciona 100 apenas no canal Blue (processo de Amplificação)
merged = cv2.merge([B+100, G, R])

# Exibe imagem com canal Azul amplificado
cv2.imshow("Merge com Amplificação canal Azul", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()