import cv2
from matplotlib import pyplot as plt

# Ler documentação oficinal:
# http://docs.opencv.org/trunk/d1/db7/tutorial_py_histogram_begins.html

pathImagem = 'D:\\GitHub\\PDI_2sem2017\\Imagens\\urso.jpg'

# Valor de parametro "0" indicando que a imagem é em escala de cinza
img = cv2.imread(pathImagem, 0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)

plt.show()