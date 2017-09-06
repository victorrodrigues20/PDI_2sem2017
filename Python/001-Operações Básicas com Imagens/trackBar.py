import cv2
import numpy as np

# Define um evento padrão que, nesse código, não faz nada
def eventoCallback(x):
    pass

# Lê uma imagem
imagem = cv2.imread('../../imagens/urso.jpg')

#Cria uma janela chamada "Imagem"
cv2.namedWindow('Imagem')
# Cria um trackbar chamado "Valor" para a janela "Imagem"
# Esse trackbar suportará valores entre 0 e 255
cv2.createTrackbar('Valor','Imagem',0,255, eventoCallback)

while(1):

    # Pega o valor atual do Trackbar "Valor"
    valor = cv2.getTrackbarPos('Valor','Imagem')

    # Aplica o valor na imagem usando a técnica Thresholding
    ret, thresh1 = cv2.threshold(imagem, valor, 255, cv2.THRESH_BINARY)

    # Mostra o resultado do thresholding
    cv2.imshow('Imagem',thresh1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()