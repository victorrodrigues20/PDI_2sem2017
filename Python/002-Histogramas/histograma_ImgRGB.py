import cv2
import numpy as np
from matplotlib import pyplot as plt

# Caminho da Imagem
pathImagem = 'D:\\GitHub\\PDI_2sem2017\\PDI_2sem2017\\Imagens\\urso.jpg'

# Leitura da imagem
img = cv2.imread(pathImagem)

# Criação de um vetor representando cada canal da imagem RGB
color = ('b','g','r')

# FOR em cada canal
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
