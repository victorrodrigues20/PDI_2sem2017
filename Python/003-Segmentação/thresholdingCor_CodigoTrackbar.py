import cv2
import numpy as np

# Define um evento padrão que, nesse código, não faz nada
def eventoCallback(x):
    pass

# Lendo imagem
image = cv2.imread('../../imagens/Circulo_Cores.png')

# Mostrar imagem original
cv2.imshow('Original', image)

#Converte para HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Cria uma janela chamada "Imagem"
cv2.namedWindow('Imagem')

# Cria dois trackbars chamado "Min" e "Max para a janela "Imagem"
# Esses trackbars suportarão valores entre 0 e 255
cv2.createTrackbar('Min','Imagem',0,255, eventoCallback)
cv2.createTrackbar('Max','Imagem',0,255, eventoCallback)

while(1):

    # Pega os valores atuais dos Trackbars
    min = cv2.getTrackbarPos('Min','Imagem')
    max = cv2.getTrackbarPos('Max', 'Imagem')

    #Limites da mascara
    lower_blue = np.array([min,0,0])
    upper_blue = np.array([max,255,255])

    #Cria mascara
    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

    #Aplica mascara na imagem original
    res = cv2.bitwise_and(image, image, mask=mask)

    # Mostra o resultado do thresholding
    cv2.imshow('Imagem',res)
    k = cv2.waitKey(1)

    # ENTER
    if k == 13:
        break

cv2.destroyAllWindows()