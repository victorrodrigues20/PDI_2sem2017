import sys
import cv2
import time
import numpy as np

# Caminho da imagem
pathImagem = '../../imagens/rodovia.jpg'

# Carregar Imagem
img = cv2.imread(pathImagem)

# Criar nosso classificador, passando qual o modelo de classificação
car_classifier = cv2.CascadeClassifier('Haarcascades\haarcascade_car.xml')


# Converter imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Executar nosso classificador na imagem
# parâmetros: (imagem, fator de escala, vizinhança)
#cars = car_classifier.detectMultiScale(gray, 1.4, 2)
cars = car_classifier.detectMultiScale(gray, 1.1, 3)

# Extração dos boxes encontrados
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.imshow('Carro', img)




cv2.waitKey(0)
cv2.destroyAllWindows()